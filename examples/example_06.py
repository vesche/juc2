#!/usr/bin/env python

"""
juc2/examples/example_06.py

Draw a bunch of rectangles and move them around at random. ^_^
"""

import random

from juc2 import art, Stage

HEIGHT = 40
WIDTH = 100

stage = Stage(height=HEIGHT, width=WIDTH)

rectangles = list()
for i in range(30):
    d, x, y = random.randint(3, 8), random.randint(10, WIDTH-10), random.randint(10, HEIGHT-10)
    rectangles.append(art.Shapes.Rectangle(width=d, height=d//2+1, x=x, y=y))

while True:
    stage.draw(rectangles, FPS=12)

    for r in rectangles:
        if r.x >= WIDTH-8 or r.y >= HEIGHT-8:
            r.x -= 1
            r.y -= 1
        elif r.x <= 8 or r.y <= 8:
            r.x += 1
            r.y += 1
        else:
            m = random.choice([-1, 1])
            r.x += m
            r.y += m
