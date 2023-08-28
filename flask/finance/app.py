import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

from datetime import date

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0][
        "username"
    ]
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
        "cash"
    ]
    owned = db.execute("SELECT * FROM owned WHERE buyer_name = ?", name)

    return render_template("index.html", usd=usd, lookup=lookup, cash=cash, owned=owned)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares.isdigit():
            return apology("invalid shares", 400)

        if not symbol:
            return apology("must provide symbol", 400)

        info = lookup(symbol)
        if not info:
            return apology("invalid symbol", 400)

        if not shares:
            return apology("must provide shares", 400)

        shares = int(shares)
        if shares <= 0:
            return apology("enter valid share amount", 400)

        price = float(lookup(symbol)["price"])

        # SELECT returns a list of dictionaries, and there is only one session
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0][
            "cash"
        ]

        if price * shares >= cash:
            return apology("no money", 400)

        name = db.execute(
            "SELECT username FROM users WHERE id = ?", session["user_id"]
        )[0]["username"]
        # Record transaction
        db.execute(
            "INSERT INTO transactions (buyer_name, action, symbol, price, shares, purchase_date) VALUES(?, ?, ?, ?, ?, ?)",
            name,
            "buy",
            symbol,
            price,
            shares,
            date.today(),
        )
        # Update currently owned
        exist = db.execute(
            "SELECT * FROM owned WHERE buyer_name = ? AND symbol = ?", name, symbol
        )

        if exist:
            # update shares owned
            db.execute(
                "UPDATE owned SET shares = shares + ? WHERE symbol = ? AND buyer_name = ?",
                shares,
                symbol,
                name,
            )
        else:
            # first time purchase of stock
            db.execute(
                "INSERT INTO owned (buyer_name, symbol, shares) VALUES (?, ?, ?)",
                name,
                symbol,
                shares,
            )

        # update balance
        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?",
            price * shares,
            session["user_id"],
        )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0][
        "username"
    ]
    owned_list = db.execute("SELECT * FROM owned WHERE buyer_name = ?", name)
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)

        if not symbol.isalpha():
            return apology("invalid symbol", 400)

        if symbol == "Select Symbol":
            return apology("must select symbol", 400)

        if not shares:
            return apology("must provide shares", 400)

        shares = int(shares)
        if shares <= 0:
            return apology("enter valid share amount", 400)

        owned = db.execute(
            "SELECT shares FROM owned WHERE buyer_name = ? AND symbol = ?", name, symbol
        )

        if not owned or int(owned[0]["shares"]) < shares:
            return apology("not enough shares")

        price = float(lookup(symbol)["price"])

        # Record transaction
        db.execute(
            "INSERT INTO transactions (buyer_name, action, symbol, price, shares, purchase_date) VALUES(?, ?, ?, ?, ?, ?)",
            name,
            "sell",
            symbol,
            price,
            shares,
            date.today(),
        )
        # update shares owned
        db.execute(
            "UPDATE owned SET shares = shares - ? WHERE symbol = ? AND buyer_name = ?",
            shares,
            symbol,
            name,
        )
        # update balance
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            price * shares,
            session["user_id"],
        )
        # delete if 0 shares
        db.execute("DELETE FROM owned WHERE shares <= 0")

        return redirect("/")
    else:
        return render_template("sell.html", owned_list=owned_list)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    name = db.execute("SELECT username FROM users WHERE id = ?", session["user_id"])[0][
        "username"
    ]
    transactions = db.execute("SELECT * FROM transactions WHERE buyer_name = ?", name)
    return render_template("history.html", usd=usd, transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")

        if not symbol:
            return apology("must provide symbol", 400)

        info = lookup(symbol)
        if not info:
            return apology("invalid symbol", 400)

        return render_template("quoted.html", usd=usd, info=info)

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Ensure valid input
        if not name:
            return apology("must provide username", 400)

        elif not password:
            return apology("must provide password", 400)

        elif not confirmation:
            return apology("must confirm password", 400)

        elif not confirmation == password:
            return apology("passwords do not match", 400)

        exist = db.execute("SELECT * FROM users WHERE username = ?", name)

        if exist:
            return apology("username is taken", 400)

        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            name,
            generate_password_hash(password),
        )
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    if request.method == "POST":
        amount = request.form.get("amount")

        if not amount:
            return apology("must provide amount to deposit")

        amount = float(amount)
        if amount <= 0:
            return apology("must provide valid amount to deposit")

        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?", amount, session["user_id"]
        )
        return redirect("/")
    else:
        return render_template("deposit.html")
