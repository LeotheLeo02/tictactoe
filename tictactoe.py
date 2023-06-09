"""
Tic Tac Toe Player
"""

import math
import copy

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
    if initial_state == board:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = set()
    for i in range(len(board)):
        for j in range(len(board)):
           if board[i][j] is EMPTY:
               list.add((i, j))

    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board)):
           for k in range(len(action)):
               for l in range(len(action)):
                   if action[k][l] == board[i][j]:
                       new_board[i][j] = action[k][l]

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
