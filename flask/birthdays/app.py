import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def insert():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        name = request.form.get("name")
        month= request.form.get("month")
        day = request.form.get("day")
        # missing input
        if not request.form.get("name") or not request.form.get("month") or not request.form.get("day"):
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?,?,?)", name, month, day)
        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        bday = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", bday=bday)

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        name = request.form.get("name")
        month= request.form.get("month")
        day = request.form.get("day")
        if not request.form.get("name") or not request.form.get("month") or not request.form.get("day"):
            return redirect("/")

        db.execute("DELETE FROM birthdays WHERE (name, month, day) = (?, ?, ?)", name, month, day)
        return redirect("/")

    else:
        bday = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", bday=bday)

@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        newmonth = request.form.get("newmonth")
        newday = request.form.get("newday")
        name = request.form.get("name")
        month= request.form.get("month")
        day = request.form.get("day")
        if not request.form.get("newmonth") or not request.form.get("newday") or not request.form.get("name") or not request.form.get("month") or not request.form.get("day"):
            return redirect("/")

        db.execute("UPDATE birthdays SET (month, day) = (?, ?) WHERE (name, month, day) = (?, ?, ?)", newmonth, newday, name, month, day)
        return redirect("/")
    else:
        bday = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", bday=bday)