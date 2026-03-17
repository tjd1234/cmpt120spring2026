# Lights Out

Using the [lightboard](lightboard.py) module, create a [Lights Out
game](https://en.wikipedia.org/wiki/Lights_Out_(game)). See the marking scheme
below for details.

## Using the lightboard Module

To use [lightboard](lightboard.py), see
[lightboardDocumentation.md](lightboardDocumentation.md) for documentation, and
[lb_demo.py](lb_demo.py) for an example of how to run it.

**Important**: Do **not** change [lightboard.py](lightboard.py) in any way.
Also, do **not** import the `turtle` module into your program. You *can* import
other modules like `math` or `random` if you need them.

## What to Submit

Put all your code in [lightsout.py](lightsout.py), and submit just that file on
Canvas. The marker will run your program with a copy of
[lightboard.py](lightboard.py) in the same folder.

## Marking Scheme

**1 mark** for displaying the title "Lights Out" at the top and the message
"Click a light to toggle it and its neighbors. Turn all off!" at the bottom.

**1 mark** for starting with all lights randomly on or off.

**4 marks** for toggling a light when the user clicks it, as well as toggling
its four neighbors above, below, to the left, and to the right. Toggling means
that if the light is on, it goes to off, and if it is off, it goes to on.

**3 marks** The three buttons on the side of the board work like this:
- Button 1 is labeled "Scramble", and when clicked it randomly sets each light
   to on or off.
- Button 2 is labeled "All Off", and when clicked it turns all lights off.
- Button 3 is labeled "All On", and when clicked it turns all lights on.

**2 marks** for recognizing when all the lights are off and printing the message
"Solved!" at the bottom when all the lights are off.

**2 marks** overall: consistent indentation and spacing (all blank lines and
spaces should have a good reason for being there)

**1 mark** overall: all variable and function names are self-descriptive
