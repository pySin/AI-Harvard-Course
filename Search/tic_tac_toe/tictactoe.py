# Tic Tac Toe logic
import copy
import math

# Player Symbols
X = "X"
O = "O"
EMPTY = None


# Set Initial Tic Tac Toe state with 8 empty cells.
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


# Determine which player's move it is
# by the moves already made on the playing board.
def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_moves = sum([m.count("X") for m in board])
    o_moves = sum([m.count("O") for m in board])

    # If X moves are more than the O moves it's O's turn
    # otherwise it's X's turn.
    return O if x_moves > o_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    The cells not taken by any player.
    """
    available_actions = set()
    [[available_actions.add((r, c)) for c in range(len(board[0])) if board[r][c] == EMPTY]
     for r in range(len(board))]
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Another cell is taken(played).
    """
    if action not in actions(board):
        raise Exception("This move is not available!")

    # Make and modify a deep copy of the board, so it doesn't
    # change the main board state for the AI move calculations.
    board_deep_copy = copy.deepcopy(board)
    current_player = player(board_deep_copy)
    board_deep_copy[action[0]][action[1]] = current_player
    return board_deep_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Result of 1 means X is winner, -1 - O is winner, 0 - the game is a tie.
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

    # Check for diagonal win.
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
    # Check if someone won the game
    if winner(board) is not None:
        return True

    # Check if there are empty cells by loping
    # each cell
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    This determines the winner.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses a recursion returning finished game at the bottom recursion.
    """

    def max_value(mm_board):
        """
        Through 2 function cross recursion look for a result
        of a finished game optimal for the X player.
        :param mm_board: Tic Tac Toe play board
        :return: a tuple, move coordinates
        """

        # Store actions(moves) and their evaluations(1, -1, 0).
        action_results = []

        # At the bottom recursion level the game should finish
        # and return 1 if X won, -1 if O won and 0 if game is tie.
        if terminal(mm_board):
            return utility(mm_board)

        v = -math.inf

        # Get the empty cells from the test board
        # for the specific recursion board.
        available_actions = actions(mm_board)

        # For each test game turn go deeper into the recursion
        # and activate the antagonist function until the board is full.
        for action in available_actions:

            # Compare the biggest result so far with the result from
            # the current move and assign.
            v = max(v, min_value(result(mm_board, action)))
            action_results.append([v, action])

        # Get the original board length to compare with the best move candidates.
        length = sum([len([c for c in r if c is None]) for r in board])

        # If the move candidates are the same number as the empty cells
        # in the original board it meat that the deepest level in the
        # recursion is reached and the best move has to be picked.
        if len(action_results) == length:
            max_result = max([a[0] for a in action_results])
            # Get the first Max result. The rest of the loop is not needed.
            best_action = (next(ba for ba in action_results if ba[0] == max_result), None)
            return best_action[0][1]

        return v

    def min_value(mm_board):
        """
        Through 2 function cross recursion look for a result
        of a finished game optimal for the O player.
        :param mm_board: Tic Tac Toe play board
        :return: a tuple, move coordinates
        """

        # Store actions(moves) and their evaluations(1, -1, 0).
        action_results = []

        # At the bottom recursion level the game should finish
        # and return 1 if X won, -1 if O won and 0 if game is tie.
        if terminal(mm_board):
            return utility(mm_board)

        v = math.inf

        # Get the empty cells from the test board
        # for the specific recursion board.
        available_actions = actions(mm_board)

        # For each test game turn go deeper into the recursion
        # and activate the antagonist function until the board is full.
        for action in available_actions:

            # Compare the smallest result so far with the result from
            # the current move and assign.
            v = min(v, max_value(result(mm_board, action)))
            action_results.append([v, action])

        # Get the original board length to compare with the best move candidates.
        length = sum([len([c for c in r if c is None]) for r in board])

        # If the move candidates are the same number as the empty cells
        # in the original board it meat that the deepest level in the
        # recursion is reached and the best move has to be picked.
        if len(action_results) == length:
            min_result = min([a[0] for a in action_results])

            # Get the first Max result. The rest of the loop is not needed.
            best_action = (next(ba for ba in action_results if ba[0] == min_result), None)
            return best_action[0][1]

        return v

    current_player = player(board)
    if current_player == "X":

        # Enter the function that tries to maximise the value
        # if the player is X.
        x_value = max_value(board)
        return x_value
    else:
        # Enter the function that tries to minimise the value
        # if the player is O.
        o_value = min_value(board)
        return o_value
