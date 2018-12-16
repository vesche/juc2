#!/usr/bin/env python

'''
juc2/example/example_03.py

Draw a triangle and square to the terminal.
The square will move around at random. :D
'''

from juc2 import art, Stage
from random import randint

stage = Stage(height=40, width=80, frame=True)
rectangle = art.Rectangle(width=10, height=5, x=20, y=20)
triangle = art.Triangle(n=10, x=5, y=5)

while True:
    orders = [
        rectangle,
        triangle
    ]
    stage.draw(orders, FPS=12)

    rectangle.x += randint(-1, 1)
    rectangle.y += randint(-1, 1)
