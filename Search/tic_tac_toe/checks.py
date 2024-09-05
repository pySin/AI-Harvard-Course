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

# def function1(n):
#     if n == 100:
#         return f"Target number reached: {n}"
#     n += 1
#
#     return function2(n)
#
#
# def function2(n):
#     if n == 100:
#         return f"Target number reached: {n}"
#     n += 1
#
#     return function1(n)
#
#
# n1 = 0
# print(function1(n1))

# -- Nested Function call

# def nest_1(text_1):
#     return text_1 + "ending"
#
#
# def nest_2(text_2):
#     return text_2 + "second"
#
#
# print(nest_2(nest_1("First text")))  # Return a function as an argument of another.

# -- Recursion with nested function call with Terminal returning function.
import random

numbers_set = set()


def terminal(n_set):
    three_numbers = {n for n in range(len(n_set), 0, -1)}
    if sum(three_numbers) == 9:
        return True
    return False


def initial_numbers():
    initial_n = set()
    for _ in range(3):
        initial_n.add(random.randint(1, 9))
    return initial_n


def generate_number():
    return random.randint(1, 9)


def modify_number(num):
    modifier = random.randint(-1, 1)
    return num + modifier


def number_1(num_set):
    print(f"Num Set: {num_set}")
    if terminal(num_set):
        return f"The last three digits equals to {sum(num_set[-3:])}"

    num_set.add(modify_number(generate_number() - 1))
    phrase = number_2(num_set)
    return phrase


def number_2(num_set):
    if terminal(num_set):
        return f"The last three digits equals to {sum(num_set[-3:])}"

    num_set.add(modify_number(generate_number() - 1))
    phrase = number_1(num_set)
    return phrase


first_numbers = initial_numbers()
number_1(first_numbers)
