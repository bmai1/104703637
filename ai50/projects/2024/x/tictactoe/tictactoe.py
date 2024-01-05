"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # counts how many times each player moved
    x_cnt = 0
    o_cnt = 0
    for row in range(3):
        for col in range(3):
            x_cnt += board[row][col] == X
            o_cnt += board[row][col] == O

    # X turn if equal count
    return X if x_cnt == o_cnt else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # find empty cells in board
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]

    # check bounds and empty
    if row < 0 or col < 0 or row >= 3 or col >= 3 or board[row][col] is not EMPTY:
        raise RuntimeError("Invalid Move.")
    
    # create deepcopy (doesn't affect root board)
    new_board = deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
  
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        # check cols
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # check diags
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0] 

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    
    for row in range(3):
        for col in range(3):
            if board[row][col] is EMPTY:
                return False
    # Tied 
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    res = winner(board)
    if res == X:
        return 1
    return -1 if res == O else 0


def minimax(board, alpha=-1, beta=1):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    turn = player(board)
    possible = actions(board)
    opt_move = None

    # always optimal to take center early
    if (1, 1) in possible:
        return (1, 1)

    # maximize X (1), minimize O (-1)
    best = -1 if turn == X else 1
    for move in possible:
        res_board = result(board, move)
        score = mn(res_board, alpha, beta) if turn == X else mx(res_board, alpha, beta)
    
        # maximize X (1), minimize O (-1)
        if (turn == X and score > best) or (turn == O and score < best):
            best = score
            opt_move = move

        if turn == X:
            alpha = max(alpha, best)
        else:
            beta = min(beta, best)

        if beta <= alpha:
            break

    return opt_move


def mx(board, alpha, beta):
    if terminal(board):
        return utility(board)

    score = -1
    for action in actions(board):
        score = max(score, mn(result(board, action), alpha, beta))
        alpha = max(alpha, score)

        if beta <= alpha:
            break

    return score


def mn(board, alpha, beta):
    if terminal(board):
        return utility(board)

    score = 1
    for action in actions(board):
        score = min(score, mx(result(board, action), alpha, beta))
        beta = min(beta, score)

        if beta <= alpha:
            break

    return score