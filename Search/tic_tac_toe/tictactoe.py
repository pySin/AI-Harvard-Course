# Tic Tac Toe logic
import math

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
    x_moves = sum([m.count("X") for m in board])
    o_moves = sum([m.count("O") for m in board])

    return O if x_moves > o_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    [[available_actions.add((r, c)) for c in range(len(board[0])) if c != EMPTY]
     for r in range(len(board))]
    return available_actions
