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
        # print(f"Current Board: {board}")
        print(f"Non Available Move: {action}")
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
    # Check if someone won the game
    if winner(board) is not None:
        return True

    # Check if there are empty cells
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
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
    """

    def max_value(mm_board):
        action_results = []
        # print("In max value")
        if terminal(mm_board):
            print(f"Max Value Terminal Section: {mm_board}")

            return utility(mm_board)
        v = -math.inf
        available_actions = actions(mm_board)
        for action in available_actions:
            # print(action)
            v = max(v, min_value(result(mm_board, action)))
            # print(f"Result function result: {result(mm_board, action)}:")
            # print(f"Value in max function: {v}")
            # print(f"Max Value Last Action: {action}")
            action_results.append([v, action])
            # print(f"Available Actions: {available_actions}")
            # print(f"Final Action results: {action_results}")
        # print(f"Available Actions: {len(available_actions)}")
        # print(f"Action results: {len(action_results)}")
        # print(f"Original Board length: {len([c for c in board if c is None])}")
        print(f"Board: {board}")
        length = sum([len([c for c in r if c is None]) for r in board])
        print(f"Board Length: {length}")

        if len(action_results) == len([c for c in board if c is None]):
            max_result = max([a[0] for a in action_results])
            best_action = (next(ba for ba in action_results if ba[0] == max_result), None)
            return best_action

        return v

    def min_value(mm_board):
        action_results = []
        if terminal(mm_board):
            print(f"Min Value Terminal Section: {board}")
            return utility(mm_board)
        v = math.inf
        # print(f"Actions mm_board: {actions(mm_board)}")
        available_actions = actions(mm_board)
        for action in available_actions:
            v = min(v, max_value(result(mm_board, action)))
            # print(f"Result function result: {result(mm_board, action)}:")
            # print(f"Value in min function: {v}")
            # print(f"Min Value Last Action: {action}")
            action_results.append([v, action])
            # print(f"Action Results: {action_results}")
        # print(f"Available Actions: {len(available_actions)}")
        # print(f"Action results: {len(action_results)}")
        # print(f"Original Board length: {len([c for c in board if c is None])}")
        print(f"Board: {board}")
        length = sum([len([c for c in r if c is None]) for r in board])
        print(f"Board Length: {length}")

        if len(action_results) == length:
            min_result = min([a[0] for a in action_results])
            best_action = (next(ba for ba in action_results if ba[0] == min_result), None)
            return best_action

        return v

    current_player = player(board)
    print(f"Current Player: {current_player}")
    if current_player == "X":
        x_value = max_value(board)
        print(f"Last X value: {x_value}")  # The script does not reach here
        return x_value  # return a move(tuple)
    else:
        o_value = min_value(board)
        print(f"Last O value: {o_value}")  # The script does not reach here
        return o_value  # return a move(tuple)
