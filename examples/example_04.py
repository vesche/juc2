#!/usr/bin/env python

'''
juc2/example/example_04.py

Move a horse back and forth across the terminal.
Change the direction of an arrow. :3
'''

from juc2 import art, Stage

stage = Stage(height=40, width=100)

horse = art.Animals.Horse()
arrow_r = art.Symbols.ArrowRight(x=40, y=10)
arrow_l = art.Symbols.ArrowLeft(x=40, y= 10)

forward = True

while True:
    if forward:
        horse.x += 1
        arrow = arrow_r
    else:
        horse.x -= 1
        arrow = arrow_l

    orders = [
        horse,
        arrow
    ]
    stage.draw(orders, FPS=12)

    if horse.x == 5:
        forward = True
    if horse.x == 70:
        forward = False
