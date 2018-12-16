#!/usr/bin/env python

'''
juc2/example/example_01.py

Draws a horse to the terminal. :)
'''

from juc2 import art, Stage

stage = Stage()
horse = art.Animals.Horse()
stage.draw(horse)