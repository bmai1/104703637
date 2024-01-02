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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_cnt = 0
    o_cnt = 0
    for row in range(3):
        for col in range(3):
            x_cnt += board[row][col] == X
            o_cnt += board[row][col] == O
            
    return X if x_cnt == o_cnt else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

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

    if row < 0 or col < 0 or row >= 3 or col >= 3 or board[row][col] is not EMPTY:
        raise RuntimeError("Invalid Move.")
    new_board = deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0] 

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
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



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)
    possible = actions(board)
    optimal_move = None

    # if X takes center first, player 0 must block a corner
    if len(possible) == 8 and turn == O and board[1][1] == X:
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for move in corners:
            if move in possible:
                return move

    # minimize X, maximize O
    score_best = -math.inf if turn == X else math.inf

    for move in possible:
        res_board = result(board, move)
        score = helper(res_board, turn)
        
        if turn == X and score > score_best:
            score_best = score
            optimal_move = move
        elif turn == O and score < score_best:
            score_best = score
            optimal_move = move

    return optimal_move


def helper(board, turn):
    if terminal(board):
        return utility(board)
    
    possible = actions(board)
    score = -math.inf if turn == X else math.inf
    opponent = O if turn == X else X

    if turn == X:
        for move in possible:
            score = max(score, helper(result(board, move), opponent))
    else:
        for move in possible:
            score = min(score, helper(result(board, move), opponent))
    
    return score
