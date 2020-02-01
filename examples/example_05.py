#!/usr/bin/env python

"""
juc2/example/example_05.py

Display all ascii art one at a time. :O
"""

from juc2 import art, Stage

stage = Stage(height=40, width=100)

def demo(category):
    for i in dir(category):
        if not i.startswith('__'):
            figure = getattr(category, i)
            stage.draw(figure(), FPS=1)

demo(art.Animals)
demo(art.Objects)
demo(art.Symbols)