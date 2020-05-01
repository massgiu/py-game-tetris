from src import PlayField
from src.Utils import Utils
import random


class Piece:

    def __init__(self, column, row, shape):
        self.col = column
        self.row = row
        self.shape = shape
        self.color = Utils.SHAPES_COLORS[Utils.SHAPES.index(shape)]
        self.rotation = 0  # number from 0-3

    def shift_right(self, grid):
        self.col += 1
        if not PlayField.PlayField.valid_space(self, grid):
            self.col -= 1

    def shift_left(self, grid):
        self.col -= 1
        if not PlayField.PlayField.valid_space(self, grid):
            self.col += 1

    def rotate(self, grid):
        self.rotation = self.rotation + 1 % len(self.shape)
        if not PlayField.PlayField.valid_space(self, grid):
            self.rotation = self.rotation - 1 % len(self.shape)

    def go_down(self, grid):
        self.row += 1
        if not PlayField.PlayField.valid_space(self, grid):
            self.row -= 1
