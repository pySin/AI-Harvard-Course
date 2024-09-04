# Test Tic Tac Toe AI player
import pytest as pt

import tictactoe as ttt

# The AI plays against itself

@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    return play_ai_vs_ai()

# Assisting Function

