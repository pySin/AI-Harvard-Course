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

# def function1(n):
#     if n == 100:
#         return f"Targe number reached: {n}"
#
#     n += 1
#     return function2(n)
#
#
# def function2(n):
#     if n == 100:
#         return f"Targe number reached: {n}"
#
#     return function1(n)


# number = 0
# print(function2(number))


# -- Double Function Recursion / Recursion in middle function


# def function1(n):
#     if n == 100:
#         return f"Target number reached: {n}"
#     n += 1
#     print(f"N: {n}")
#     result = function2(n)
#     print(f"Result: {result}")
#     print(f"Post Result N: {n}")
#
#     return result
#
#
# def function2(n):
#     if n == 100:
#         return f"Targe number reached: {n}"
#     n += 1
#     print(f"N: {n}")
#     result = function1(n)
#     print(f"Result: {result}")
#     print(f"Post Result N: {n}")
#
#     return result
#
#
# n1 = 0
# function1(n1)

# Get Value From bottom recursion

def function1(n):
    if n == 100:
        return f"Target number reached: {n}"
    n += 1
    print(f"N: {n}")
    result = function2(n)
    print(f"Result: {result}")
    print(f"Post Result N: {n}")

    return result


def function2(n):
    if n == 100:
        return f"Targe number reached: {n}"
    n += 1
    print(f"N: {n}")
    result = function1(n)
    print(f"Result: {result}")
    print(f"Post Result N: {n}")

    return result


n1 = 0
function1(n1)