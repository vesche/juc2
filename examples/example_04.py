#!/usr/bin/env python

"""
juc2/example/example_04.py

Move a horse back and forth across the terminal.
Change the direction of an arrow. :3
"""

from juc2 import art, Stage

stage = Stage(height=40, width=100)

horse = art.Animals.Horse(x=6)
arrow_left = art.Symbols.ArrowLeft(x=40, y=10)
arrow_right = art.Symbols.ArrowRight(x=40, y=10)

arrow = arrow_right
move_right = True

while True:
    if move_right:
        horse.x += 1
    else:
        horse.x -= 1

    stage.draw([horse, arrow], FPS=12)

    if horse.x == 5:
        arrow = arrow_right
        move_right = True
        horse.reverse()
    if horse.x == 70:
        arrow = arrow_left
        move_right = False
        horse.reverse()