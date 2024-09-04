# Check project related things

# import tictactoe
#
# current_state = [[tictactoe.EMPTY, "X", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
#                  ["X", "O", tictactoe.EMPTY]]
#
# print(tictactoe.player(current_state))

# --

# import tictactoe
#
# current_state = [[tictactoe.EMPTY, "X", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
#                  ["X", "O", tictactoe.EMPTY]]

# print(tictactoe.actions(current_state))

# import tictactoe
#
# current_state = [[tictactoe.EMPTY, "X", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
#                  ["X", "O", tictactoe.EMPTY]]
#
# print(tictactoe.result(current_state, (0, 0)))
# current_state = tictactoe.result(current_state, (0, 0))
# print(tictactoe.result(current_state, (0, 2)))

# -- Check Horizontal win
# import tictactoe
#
# current_state = [[tictactoe.EMPTY, "X", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
#                  ["X", "X", "X"]]
#
# print(tictactoe.winner(current_state))

# -- Check Vertical win
# import tictactoe
#
# current_state = [[tictactoe.EMPTY, "O", "X"],
#                  [tictactoe.EMPTY, "O", tictactoe.EMPTY],
#                  ["X", "O", "X"]]

# print(tictactoe.winner(current_state))

# import tictactoe
#
# current_state = [["O", tictactoe.EMPTY, "X"],
#                  [tictactoe.EMPTY, "O", tictactoe.EMPTY],
#                  ["X", "O", "O"]]
#
# print(tictactoe.winner(current_state))

# -- Test terminal() function

# import tictactoe

# current_state = [["O", tictactoe.EMPTY, "X"],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
#                  ["X", "O", "O"]]

# current_state = [["X", "O", "X"],
#                  ["O", "O", "X"],
#                  ["X", "X", "O"]]
#
# print(tictactoe.terminal(current_state))


# import tictactoe
#
# current_state = [["X", "O", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, "O", "X"],
#                  ["X", "O", "X"]]
#
# print(tictactoe.utility(current_state))

# --

# import tictactoe
#
# current_state = [["X", "O", tictactoe.EMPTY],
#                  [tictactoe.EMPTY, tictactoe.EMPTY, "O"],
#                  ["X", "O", "X"]]
#
# print(tictactoe.minimax(current_state))

# -- Double Function Recursion

def function1(n):
    if n == 100:
        return f"Targe number reached: {n}"




