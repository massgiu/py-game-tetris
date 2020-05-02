from src.Utils import Utils


class Piece:

    def __init__(self, column, row, shape):
        self.col = column #This value must be added to avery block that composes the piece
        self.row = row #This value must be added to avery block
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
        # check if tuple (i,j) has color of empty cells
        free_positions = []
        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                if grid[row][col] == Utils.EMPTY_CELL_COLOR: #if grid cell is empty
                    free_positions.append((row, col))
        shape_block_pos = self.convert_shape_format()  # get the positions of every block of the shape

        for block in shape_block_pos:
            if block not in free_positions:
                if block[0] > -1:  # If we are not above the playground
                    return False

        return True

    def convert_shape_format(self):  # shape ia matrix es Z=[[.....,..000,.000..],[.....,.0000,.000.]]
        # This method converts a format into a list of positions that we can then return
        positions = []
        format = self.shape[self.rotation % len(self.shape)]  # rotation increments and select row1, row2, row1,...
        # format = ['.....','...O.','..OO.','..OOO'] (for the 1st 0 it has offset_row=1, offset_col=3)
        for offset_row, line in enumerate(format):
            row = list(line)  # split a string in a list of element (es '..OO.' => ['.','.','O','O','.']
            for offset_col, column in enumerate(row):
                if column == '0':
                    positions.append((self.row + offset_row,self.col + offset_col))  # positions((1,6),(2,6),(3,6))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 4, pos[1] - 2)

        return positions

    def update_grid(self, grid):
        shape_pos = self.convert_shape_format()
        for block_pos in range(len(shape_pos)):
            row, col = shape_pos[block_pos]  # get position of piece
            # Update grid
            if row > -1:  # If we are not above the playground
                grid[row][col] = self.color
        return grid