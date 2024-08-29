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
import tictactoe

current_state = [[tictactoe.EMPTY, "X", tictactoe.EMPTY],
                 [tictactoe.EMPTY, tictactoe.EMPTY, tictactoe.EMPTY],
                 ["X", "X", "X"]]

print(tictactoe.winner(current_state))
