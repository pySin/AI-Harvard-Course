# Tic Tac Toe logic
import copy
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
    [[available_actions.add((r, c)) for c in range(len(board[0])) if board[r][c] == EMPTY]
     for r in range(len(board))]
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("This move is not available!")
    board_deep_copy = copy.deepcopy(board)

    raise NotImplementedError
