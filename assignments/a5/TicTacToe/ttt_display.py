#!/usr/bin/env python3
"""
Tic-tac-toe board module. Draws a 3x3 grid with cells numbered 0–8
(row-major: 0,1,2 = first row; 3,4,5 = second; 6,7,8 = third).
Provides set_X(cell), set_O(cell), clear_cell(cell), set_title(str), set_message(str),
set_position(x, y), and on_click(f) to run a function when the mouse is clicked
(with the clicked cell 0–8, or -1 if outside the grid).
"""

import turtle

CELL_SIZE = 80
BOARD_LEFT = -CELL_SIZE * 1.5
BOARD_TOP = CELL_SIZE * 1.5

_screen = None
_pen = None
_title_pen = None
_message_pen = None
_board = [[None, None, None] for _ in range(3)]
_title_text = ""
_message_text = ""
_window_startx = None
_window_starty = None
_click_handler = None


def _cell_to_row_col(cell):
    """Convert cell number 0–8 to (row, col)."""
    if not 0 <= cell <= 8:
        raise ValueError("cell must be 0–8")
    return cell // 3, cell % 3


def _cell_center(row, col):
    x = BOARD_LEFT + col * CELL_SIZE + CELL_SIZE / 2
    y = BOARD_TOP - row * CELL_SIZE - CELL_SIZE / 2
    return x, y


def _click_to_cell(x, y):
    """Convert screen (x, y) to cell number 0–8, or -1 if outside the grid."""
    if not (BOARD_LEFT <= x <= BOARD_LEFT + 3 * CELL_SIZE):
        return -1
    if not (BOARD_TOP - 3 * CELL_SIZE <= y <= BOARD_TOP):
        return -1
    col = int((x - BOARD_LEFT) / CELL_SIZE)
    row = int((BOARD_TOP - y) / CELL_SIZE)
    if 0 <= row <= 2 and 0 <= col <= 2:
        return row * 3 + col
    return -1


def _ensure_screen():
    global _screen, _pen, _title_pen, _message_pen
    if _screen is not None:
        return
    _screen = turtle.Screen()
    _screen.setup(400, 500, startx=_window_startx, starty=_window_starty)
    _screen.title("Tic-Tac-Toe Board")
    _screen.tracer(0)

    _pen = turtle.Turtle()
    _pen.hideturtle()
    _pen.penup()
    _pen.speed(0)

    _title_pen = turtle.Turtle()
    _title_pen.hideturtle()
    _title_pen.penup()
    _title_pen.speed(0)

    _message_pen = turtle.Turtle()
    _message_pen.hideturtle()
    _message_pen.penup()
    _message_pen.speed(0)

    _draw_grid()
    _draw_title_message()
    _screen.update()


def _draw_grid():
    _pen.clear()
    _pen.color("black")
    _pen.pensize(2)
    for i in range(1, 3):
        _pen.goto(BOARD_LEFT + i * CELL_SIZE, BOARD_TOP)
        _pen.pendown()
        _pen.goto(BOARD_LEFT + i * CELL_SIZE, BOARD_TOP - 3 * CELL_SIZE)
        _pen.penup()
        _pen.goto(BOARD_LEFT, BOARD_TOP - i * CELL_SIZE)
        _pen.pendown()
        _pen.goto(BOARD_LEFT + 3 * CELL_SIZE, BOARD_TOP - i * CELL_SIZE)
        _pen.penup()
    _draw_pieces()
    _screen.update()


def _draw_x(row, col):
    x, y = _cell_center(row, col)
    margin = CELL_SIZE * 0.2
    _pen.color("blue")
    _pen.pensize(3)
    _pen.goto(x - margin, y + margin)
    _pen.pendown()
    _pen.goto(x + margin, y - margin)
    _pen.penup()
    _pen.goto(x + margin, y + margin)
    _pen.pendown()
    _pen.goto(x - margin, y - margin)
    _pen.penup()


def _draw_o(row, col):
    x, y = _cell_center(row, col)
    r = CELL_SIZE * 0.25
    _pen.color("red")
    _pen.pensize(3)
    _pen.goto(x, y - r)
    _pen.pendown()
    _pen.circle(r)
    _pen.penup()


def _draw_pieces():
    for row in range(3):
        for col in range(3):
            cell = _board[row][col]
            if cell == "X":
                _draw_x(row, col)
            elif cell == "O":
                _draw_o(row, col)


def _draw_title_message():
    _title_pen.clear()
    _message_pen.clear()
    _title_pen.goto(0, BOARD_TOP + CELL_SIZE * 0.6)
    _title_pen.color("black")
    _title_pen.write(_title_text, align="center", font=("Arial", 16, "bold"))
    _message_pen.goto(0, BOARD_TOP - 3 * CELL_SIZE - CELL_SIZE * 0.8)
    _message_pen.color("black")
    _message_pen.write(_message_text, align="center", font=("Arial", 14, "normal"))
    _screen.update()


def set_X(cell):
    """Place an X in the given cell (0–8)."""
    _ensure_screen()
    row, col = _cell_to_row_col(cell)
    _board[row][col] = "X"
    _draw_grid()
    _draw_title_message()
    _screen.update()


def set_O(cell):
    """Place an O in the given cell (0–8)."""
    _ensure_screen()
    row, col = _cell_to_row_col(cell)
    _board[row][col] = "O"
    _draw_grid()
    _draw_title_message()
    _screen.update()


def clear_cell(cell):
    """Clear the given cell (0–8)."""
    _ensure_screen()
    row, col = _cell_to_row_col(cell)
    _board[row][col] = None
    _draw_grid()
    _draw_title_message()
    _screen.update()


def set_title(s):
    """Set the title text at the top of the board."""
    global _title_text
    _title_text = s if s is not None else ""
    _ensure_screen()
    _draw_title_message()
    _screen.update()


def set_message(s):
    """Set the message text at the bottom of the board."""
    global _message_text
    _message_text = s if s is not None else ""
    _ensure_screen()
    _draw_title_message()
    _screen.update()


def set_position(x, y):
    """Set the position of the board window on the screen when it is first shown.
    (x, y) is the top-left corner of the window in screen coordinates.
    Call this before any other board-displaying function to take effect."""
    global _window_startx, _window_starty
    _window_startx = x
    _window_starty = y


def on_click(f):
    """Register a function to run when the mouse is clicked. The function will
    be called with one argument: the cell number (0–8) that was clicked, or -1
    if the click was outside the grid (e.g. in the title, message, or margin)."""
    global _click_handler
    _click_handler = f
    _ensure_screen()

    def _handle_click(x, y):
        cell = _click_to_cell(x, y)
        if _click_handler is not None:
            _click_handler(cell)

    _screen.onclick(_handle_click)


def mainloop():
    """Enter the turtle main loop (call this from the importing script when done)."""
    _ensure_screen()
    turtle.done()


if __name__ == "__main__":
    # Minimal demo when run directly
    set_title("Tic-Tac-Toe")
    set_message("Cells 0–8")
    set_X(0)
    set_O(4)
    set_X(8)
    mainloop()
