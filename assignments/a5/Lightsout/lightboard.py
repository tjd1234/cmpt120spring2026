"""
Light board: 5x5 grid of lights. Cells numbered 0–24 (row-major).
Provides set_light(cell, on), turn_on(cell), turn_off(cell), get_light(cell),
set_position(x, y), set_title(str), set_message(str), on_click(f) for light clicks,
set_button_text(n, str) and on_button_click(n, f) for the three side buttons (n=1,2,3).
"""

import tkinter as tk

ROWS = 5
COLS = 5
SIZE = 60
GAP = 4
COLOR_OFF = "#2d2d2d"
COLOR_ON = "#ffeb3b"
COLOR_OUTLINE = "#555"
TITLE_FONT = ("Arial", 18, "bold")
MESSAGE_FONT = ("Arial", 12, "normal")
BUTTON_WIDTH = 12

_state = [False] * (ROWS * COLS)
_root = None
_canvas = None
_rects = []
_click_handler = None
_window_startx = None
_window_starty = None
_title_text = ""
_message_text = ""
_title_label = None
_message_label = None
_button_texts = ["Button1", "Button2", "Button3"]
_button_widgets = [None, None, None]
_button_handlers = [None, None, None]


def _cell_to_row_col(cell):
    """Convert cell number 0–24 to (row, col)."""
    if not 0 <= cell < ROWS * COLS:
        raise ValueError(f"cell must be 0–{ROWS * COLS - 1}")
    return cell // COLS, cell % COLS


def _click_to_cell(x, y):
    """Convert canvas (x, y) to cell number 0–24, or -1 if outside the grid."""
    col = (x - GAP) // (SIZE + GAP)
    row = (y - GAP) // (SIZE + GAP)
    if 0 <= row < ROWS and 0 <= col < COLS:
        return row * COLS + col
    return -1


def _ensure_screen():
    global _root, _canvas, _rects, _title_label, _message_label, _button_widgets
    if _root is not None:
        return
    _root = tk.Tk()
    _root.title("Light Board")
    _root.configure(bg="#1a1a1a")
    width = COLS * (SIZE + GAP) + GAP
    height = ROWS * (SIZE + GAP) + GAP

    content = tk.Frame(_root, bg="#1a1a1a")
    content.pack(side=tk.LEFT, padx=(10, 0), pady=10)

    _title_label = tk.Label(
        content, text=_title_text, font=TITLE_FONT,
        fg="#e0e0e0", bg="#1a1a1a"
    )
    _title_label.pack(pady=(0, 4))

    _canvas = tk.Canvas(content, width=width, height=height, bg="#1a1a1a", highlightthickness=0)
    _canvas.pack(pady=4)

    _message_label = tk.Label(
        content, text=_message_text, font=MESSAGE_FONT,
        fg="#a0a0a0", bg="#1a1a1a"
    )
    _message_label.pack(pady=(4, 0))

    btn_frame = tk.Frame(_root, bg="#1a1a1a")
    btn_frame.pack(side=tk.RIGHT, padx=10, pady=10)
    for i in range(3):
        idx = i
        btn = tk.Button(
            btn_frame, text=_button_texts[i], width=BUTTON_WIDTH,
            command=lambda i=idx: _on_button(i)
        )
        btn.pack(pady=4)
        _button_widgets[i] = btn

    if _window_startx is not None and _window_starty is not None:
        _root.geometry(f"+{_window_startx}+{_window_starty}")
    _draw_grid()
    _canvas.bind("<Button-1>", _handle_click)


def _draw_grid():
    global _rects
    if _canvas is None:
        return
    _rects.clear()
    for cell in range(ROWS * COLS):
        row, col = _cell_to_row_col(cell)
        x1 = GAP + col * (SIZE + GAP)
        y1 = GAP + row * (SIZE + GAP)
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        color = COLOR_ON if _state[cell] else COLOR_OFF
        r = _canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color, outline=COLOR_OUTLINE, width=2
        )
        _rects.append(r)


def _handle_click(event):
    cell = _click_to_cell(event.x, event.y)
    if cell >= 0 and _click_handler is not None:
        _click_handler(cell)
    elif cell >= 0:
        print(f"Cell clicked: {cell}")


def _on_button(n):
    """Invoke the handler for button n (0, 1, or 2)."""
    if 0 <= n < 3 and _button_handlers[n] is not None:
        _button_handlers[n]()


def set_light(cell, on):
    """Turn the light at cell on (True) or off (False)."""
    if not 0 <= cell < ROWS * COLS:
        raise ValueError(f"cell must be 0–{ROWS * COLS - 1}")
    global _state
    _state[cell] = bool(on)
    _ensure_screen()
    if _rects:
        color = COLOR_ON if _state[cell] else COLOR_OFF
        _canvas.itemconfig(_rects[cell], fill=color)


def turn_on(cell):
    """Turn the light at cell on."""
    set_light(cell, True)


def turn_off(cell):
    """Turn the light at cell off."""
    set_light(cell, False)


def get_light(cell):
    """Return True if the light is on, False if off."""
    if not 0 <= cell < ROWS * COLS:
        raise ValueError(f"cell must be 0–{ROWS * COLS - 1}")
    return _state[cell]


def set_position(x, y):
    """Set the position of the board window on the screen when it is first shown.
    (x, y) is the top-left corner of the window in screen coordinates.
    Call this before any other board-displaying function to take effect."""
    global _window_startx, _window_starty
    _window_startx = x
    _window_starty = y


def set_title(s):
    """Set the title text at the top of the board (in bigger letters)."""
    global _title_text, _title_label
    _title_text = s if s is not None else ""
    _ensure_screen()
    if _title_label is not None:
        _title_label.config(text=_title_text)


def set_message(s):
    """Set the message text at the bottom of the board (slightly smaller font)."""
    global _message_text, _message_label
    _message_text = s if s is not None else ""
    _ensure_screen()
    if _message_label is not None:
        _message_label.config(text=_message_text)


def set_button_text(n, s):
    """Set the label of button n (1, 2, or 3)."""
    if n not in (1, 2, 3):
        raise ValueError("button number must be 1, 2, or 3")
    idx = n - 1
    global _button_texts, _button_widgets
    _button_texts[idx] = s if s is not None else ""
    _ensure_screen()
    if _button_widgets[idx] is not None:
        _button_widgets[idx].config(text=_button_texts[idx])


def on_button_click(n, f):
    """Register a function to run when button n (1, 2, or 3) is clicked.
    The function is called with no arguments."""
    if n not in (1, 2, 3):
        raise ValueError("button number must be 1, 2, or 3")
    global _button_handlers
    _button_handlers[n - 1] = f
    _ensure_screen()


def on_click(f):
    """Register a function to run when a light is clicked. The function will
    be called with one argument: the cell number (0–24) that was clicked."""
    global _click_handler
    _click_handler = f
    _ensure_screen()


def mainloop():
    """Enter the main loop (call this from the importing script when done)."""
    _ensure_screen()
    _root.mainloop()


if __name__ == "__main__":
    mainloop()
