"""juc2.stage"""

import os
import time

from juc2 import art


def _tick(FPS):
    """Sleep desired frames per second."""
    time.sleep(1/FPS)


def _clear_terminal():
    """Cross-platform terminal clear."""
    os.system('cls' if os.name == 'nt' else 'clear')
    # print("%c[2J%c[;H" % (27, 27))


class Stage:
    """juc2 Stage object"""

    def __init__(self, width=40, height=20, frame=False):
        self.width = width
        self.height = height
        self.frame = frame
        self.grid = [list(' '*width) for i in range(height)]

    @staticmethod
    def _prep_figure(figure):
        """Remove blank lines from figure."""
        return '\n'.join([row for row in figure.split('\n') if row != ''])

    def display(self):
        """Displays the grid to the terminal."""
        for row in self.grid:
            print(''.join(row))

    def stage_eraser(self):
        """Get the stage eraser."""
        return art.Eraser(width=self.width, height=self.height)

    def stage_frame(self):
        """Get the stage frame."""
        return art.Rectangle(width=self.width, height=self.height,
                             transparent=True)

    def clear_stage(self):
        """Clear the stage."""
        self.load(self.stage_eraser())

    def load_frame(self):
        """Load the frame."""
        self.load(self.stage_frame())

    def load(self, figure):
        """Loads a figure onto the grid."""
        y = figure.y
        x = initial_x = figure.x
        chars = self._prep_figure(figure.display())

        for c in chars:
            if c == '\n':
                y += 1
                x = initial_x
                continue
            if c == ' ' and figure.transparent:
                x += 1
                continue
            self.grid[y][x] = c
            x += 1

    def draw(self, art_queue=None, FPS=None):
        """Draws a figure or figures onto the terminal."""

        # 1 - Clear Terminal
        _clear_terminal()

        # 2 - Clear Stage
        self.clear_stage()

        # 3 - Load Art
        if isinstance(art_queue, list):
            for figure in art_queue:
                self.load(figure)
        else:
            if art_queue:
                figure = art_queue
                self.load(figure)
        if self.frame:
            self.load_frame()

        # 4 - Display Art
        self.display()

        # 5 - Wait
        if FPS:
            _tick(FPS)
