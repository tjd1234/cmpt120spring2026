# A Tic Tac Toe Display Module

[ttt_display.py](ttt_display.py) is a module that draws a tic tac toe board and
lets you place X's and O's on it. To see it in action, run the
[tttDemo.py](tttDemo.py) program. A screen should pop up (check under other
windows if it's not visible), and you can click on the cells to place pieces.
Look at the source code for [tttDemo.py](tttDemo.py) to see how to use the
module.

[ttt_display](ttt_display.py) provides these functions:

- `set_X(cell)`: place an X on the given cell (0–8)
- `set_O(cell)`: place an O on the given cell (0–8)
- `clear_cell(cell)`: clear the given cell (0–8)
- `set_title(s)`: set the title of the board (at the top)
- `set_message(s)`: set the message (at the bottom)
- `set_position(x, y)`: set the position of the window on the screen
- `mainloop()`: start the event loop to wait for clicks and updates

The cells are numbered like this:

```
0 1 2
3 4 5
6 7 8
```

It also has provides the `on_click(f)` function which calls function `f` when
the user clicks a cell. The function `f` should take one argument, e.g.:

```python
def on_cell_click(cell):
    print(f"Cell {cell} clicked")
```

`cell` is the cell number that was clicked (0 to 8), or -1 if the click was
outside any cell.

- `on_click(f)`: call function `f` when the user clicks a cell

See [ttt_demo.py](ttt_demo.py) for examples of how to use these functions.
