from src.Utils import Utils

class Piece:

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = Utils.SHAPES_COLORS[Utils.SHAPES.index(shape)]
        self.rotation = 0  # number from 0-3

