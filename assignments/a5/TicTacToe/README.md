# Tic Tac Toe

Using the [ttt_display](ttt_display.py) module, create a Tic Tac Toe game where
the user plays against the computer. See the marking scheme below for details.

## Using the ttt_display Module

To use the [ttt_display](ttt_display.py) module, see
[tttBoardDocumentation.md](README.md) for documentation, and
[tttDemo.py](tttDemo.py) for an example of how to run it.

**Important**: Do **not** change [ttt_display.py](ttt_display.py) in any way.
Also, do **not** import the turtle module into your program. You *can* import
other modules like `math` or `random` if you need them.

## What to Submit

Put all your code in [ttt.py](ttt.py), and submit just that file on Canvas. The
marker will run your program with a copy of [ttt_display.py](ttt_display.py) in
the same folder.

## Marking Scheme

**1 mark** for X always going first.

**1 mark** for randomly choosing at the start whether the computer or human
plays X.

**2 marks** for letting place their piece by clicking on an empty cell. Clicking
a non-empty cell, or clicking outside the grid, does nothing.

**3 mark** for the computer making its move. The computer should only make legal
moves, and it should play perfectly, i.e. it should never lose.

**2 marks** for the game ending when there is a winner or a draw and announcing
the result as a message on the board.

**2 marks** when the game is over, the use can click anywhere on the screen to
restart the game and play again.

**2 marks** overall: consistent indentation and spacing (all blank lines and
spaces should have a good reason for being there)

**1 mark** overall: all variable and function names are self-descriptive
