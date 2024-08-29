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
    current_player = player(board_deep_copy)
    board_deep_copy[action[0]][action[1]] = current_player
    return board_deep_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for row win
    for row in board:
        if all([c == "X" for c in row]):
            return "X"
        if all([c == "O" for c in row]):
            return "O"

    # Check for Column win
    for j in range(len(board[0])):
        if all([board[i][j] == "X" for i in range(len(board))]):
            return "X"
        if all([board[i][j] == "O" for i in range(len(board))]):
            return "O"

    for p in [X, O]:
        if all([board[0][0] == p, board[1][1] == p, board[2][2] == p]):
            return p
        elif all([board[2][0] == p, board[1][1] == p, board[0][2] == p]):
            return p
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    raise NotImplementedError
