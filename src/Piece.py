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
        if not self.is_in_valid_space(grid):
            self.col -= 1

    def shift_left(self, grid):
        self.col -= 1
        if not self.is_in_valid_space(grid):
            self.col += 1

    def rotate(self, grid):
        self.rotation = self.rotation + 1 % len(self.shape)
        if not self.is_in_valid_space(grid):
            self.rotation = self.rotation - 1 % len(self.shape)

    def go_down(self, grid):
        self.row += 1
        if not self.is_in_valid_space(grid):
            self.row -= 1

    def is_in_valid_space(self, grid):
        # check tuple (i,j) that has color = (0,0,0)
        free_positions = []
        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                if grid[row][col] == (0, 0, 0):
                    free_positions.append((col, row))
        shape_block_pos = self.convert_shape_format()  # get the positions of every block of the shape

        for block in shape_block_pos:
            if block not in free_positions:
                if block[1] > -1:  # pos[1] is row
                    return False

        return True

    def convert_shape_format(self):  # shape ia matrix es Z=[[.....,..000,.000..],[.....,.0000,.000.]]
        # This method converts a format into a list of positions that we can then return
        positions = []
        format = self.shape[self.rotation % len(self.shape)]  # rotation increments and select row1, row2, row1,...
        # format = ['.....','...O.','..OO.','..OOO']
        for i, line in enumerate(format):
            row = list(line)  # split a string in a list of element (es '..OO.' => ['.','.','O','O','.']
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((self.col + j, self.row + i))  # positions((1,6),(2,6),(3,6))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions