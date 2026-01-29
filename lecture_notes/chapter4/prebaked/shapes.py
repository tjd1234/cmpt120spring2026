# shapes.py

import turtle
import math

def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def star(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)

def polygon(num_sides, length):
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(length)
        turtle.right(angle)

def flower(length, shape_func):
    for i in range(10):
        shape_func(length)
        turtle.right(36)
    turtle.hideturtle()

def circle(radius):
    circumference = 2 * math.pi * radius
    num_sides = 30
    length = circumference / num_sides
    polygon(num_sides, length)

def polyline(n, length, angle):
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle / 360
    n = 30
    length = arc_length / n
    step_angle = angle / n
    polyline(n, length, step_angle)

def pattern1():
    square(100)
    triangle(100)
    star(100)
    turtle.hideturtle()

def pattern2():
    for i in range(10):
        star(100)
        turtle.right(36)
    turtle.hideturtle()

# pattern2()

# turtle.done()
