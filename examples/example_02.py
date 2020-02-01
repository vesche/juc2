#!/usr/bin/env python

"""
juc2/example/example_02.py

Move a rectangle across the terminal. <3
"""

from juc2 import art, Stage

stage = Stage(height=40, width=80, frame=True)
rectangle = art.Shapes.Rectangle(width=10, height=5, x=5, y=5)

while True:
    stage.draw(rectangle, FPS=4)

    if rectangle.x < 60:
        rectangle.x += 1