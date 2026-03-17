# lb_demo.py

"""Demo: click any cell to turn it on or off."""

import lightboard

def on_click(cell):
    lightboard.set_light(cell, not lightboard.get_light(cell))

def button1_pressed():
    print("Button 1 pressed")
    
def button2_pressed():
    print("Button 2 pressed")
    
def button3_pressed():
    print("Button 3 pressed")
    


# Set window position to a position on the screen that is not covered by other
# windows
# lightboard.set_position(1500, 50)

# Set title (top) and message (bottom)
lightboard.set_title("Demo!")
lightboard.set_message("Click a cell to toggle it on or off")

# Start with a few lights on (e.g. corners and center)
lightboard.turn_on(0)
lightboard.turn_on(4)
lightboard.turn_on(12)
lightboard.turn_on(20)
lightboard.turn_on(24)

# Show what get_light returns
print("get_light(0) =", lightboard.get_light(0))   # True (we just turned it on)
print("get_light(1) =", lightboard.get_light(1))   # False (still off)

# register the toggle function to be called when a light is clicked
lightboard.on_click(on_click)

# register handlers for the three side buttons
lightboard.on_button_click(1, button1_pressed)
lightboard.on_button_click(2, button2_pressed)
lightboard.on_button_click(3, button3_pressed)

# run the main loop to display the board and wait for clicks
lightboard.mainloop()
