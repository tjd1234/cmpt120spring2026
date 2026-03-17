# A Light Board Module

[lightboard.py](lightboard.py) is a module that draws a 5×5 grid of lights and
lets you turn them on or off. To see it in action, run  [lb_demo.py](lb_demo.py). A
window should pop up (check under other windows if it's not visible), and you
can click on the lights to toggle them. Look at the source code for
[lb_demo.py](lb_demo.py) to see how to use the module.

[lightboard.py](lightboard.py) provides the following functions.

The cells are numbered like this:

```
 0  1  2  3  4
 5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
```

**Lights (the grid)**

- `set_light(cell, on)`: Set the light at `cell` to on (`True`) or off (`False`).
- `turn_on(cell)`: Turn the light at `cell` on.
- `turn_off(cell)`: Turn the light at `cell` off.
- `get_light(cell)`: Returns `True` if the light is on, `False` if it is off.

**Title and message**

- `set_title(s)`: Set the title text at the top of the board.
- `set_message(s)`: Set the message text at the bottom.

**Window**

- `set_position(x, y)`: Set where the window appears on the screen. `(x, y)` is
  the top-left corner. Call this *before* any other function that shows the
  board (e.g. before `mainloop()`).
- `mainloop()`: Start the event loop so the window stays open and responds to
  clicks. Call this at the end of your program.

**Click handlers**

- `on_click(f)`: Call function `f` when the user clicks a light. `f` should take
  one argument, the cell number that was clicked (0 to 24). If the click is not
  on a light, the cell number is -1. For example:

  ```python
  def when_light_clicked(cell):
      print(f"Light {cell} was clicked")
  
  # make sure to register the function with the lightboard module
  lightboard.on_click(when_light_clicked)
  ```

- `set_button_text(n, s)`: Change the label on button `n` (1, 2, or 3) to the
  string `s`.
- `on_button_click(n, f)`: Call function `f` when the user clicks button `n`
  (1, 2, or 3). `f` takes no arguments. For example:

  ```python
  def button1_pressed():
      print("Button 1 was pressed")
  
  def button2_pressed():
      print("Button 2 was pressed")
  
  def button3_pressed():
      print("Button 3 was pressed")
  
  # make sure to register the functions with the lightboard module
  lightboard.on_button_click(1, button1_pressed)
  lightboard.on_button_click(2, button2_pressed)
  lightboard.on_button_click(3, button3_pressed)
  ```

See [lb_demo.py](lb_demo.py) for examples of how to use these functions.
