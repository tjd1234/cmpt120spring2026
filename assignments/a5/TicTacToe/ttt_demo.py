#!/usr/bin/env python3
"""
Demo: import the tic-tac-toe board and call set_title, set_message,
set_X, set_O, clear_cell, set_position, and on_click to show pieces and text on the board.
"""

import ttt_display

#
# This function is automatically when the user clicks a cell. The parameter cell
# is the cell number that was clicked, or -1 if the click was outside the grid.
# The cell numbers are:
#
#  0 1 2
#  3 4 5
#  6 7 8
#
def on_cell_click(cell):
    """When the user clicks a cell, set it to O (ignore clicks outside the grid).
    """
    if cell != -1:
        ttt_display.set_O(cell)
        ttt_display.set_message(f"O place at {cell}")

# Set window position to a position on the screen that is not covered by other
# windows
# ttt_display.set_position(1500, 50)

# Set title (top) and message (bottom)
ttt_display.set_title("Demo Board")
ttt_display.set_message("Click a cell to place O. Close the window to exit.")

# Place some X's (cells 0, 4, 8)
ttt_display.set_X(0)
ttt_display.set_X(4)
ttt_display.set_X(8)

# Run the given function when the user clicks; the clicked cell is set to O
ttt_display.on_click(on_cell_click)

# Keep the window open
ttt_display.mainloop()
