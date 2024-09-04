# Test Tic Tac Toe AI player
import pytest as pt

import tictactoe as ttt

# The AI plays against itself


@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    return play_ai_vs_ai()

# Assisting Function


def play_ai_vs_ai():
    board = ttt.initial_state()
    game_over = False

    while not game_over:
        move = ttt.minimax(board)
        board = ttt.result(board, move)
        game_over = ttt.terminal(board)

    assert ttt.winner(board) is None
