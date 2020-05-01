from src.Piece import Piece
from src.Utils import Utils
import pygame
import random


class PlayField:

    @staticmethod
    def create_grid(locked_positions={}):  # locked_positions is a dictionary (keys=coordinates, values=rgb colors)
        grid = [[(0, 0, 0) for x in range(Utils.COLUMNS)] for x in range(Utils.ROWS)]

        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                if (col, row) in locked_positions:
                    c = locked_positions[(col, row)]
                    grid[row][col] = c
        return grid

    @staticmethod
    def convert_shape_format(piece):  # shape ia matrix es Z=[[.....,..000,.000..],[.....,.0000,.000.]]
        # This method converts a format into a list of positions that we can then return
        positions = []
        format = piece.shape[piece.rotation % len(piece.shape)]  # rotation increments and select row1, row2, row1,...
        # format = ['.....','...O.','..OO.','..OOO']
        for i, line in enumerate(format):
            row = list(line)  # split a string in a list of element (es '..OO.' => ['.','.','O','O','.']
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((piece.x + j, piece.y + i))  # positions((1,6),(2,6),(3,6))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions

    @staticmethod
    def valid_space(piece, grid):
        # check tuple (i,j) that has color = (0,0,0)
        free_positions = []
        for i in range(Utils.ROWS):
            for j in range(Utils.COLUMNS):
               if grid[i][j] == (0, 0, 0):
                  free_positions.append((j, i))
        formatted = PlayField.convert_shape_format(piece)  # get the positions of every block of the shape

        for block in formatted:
            if block not in free_positions:
                if block[1] > -1: #pos[1] is the y
                    return False

        return True

    @staticmethod
    def check_lost(positions):
        for pos in positions:
            x, y = pos
            if y < 1:  # means that a piece is over the screen height
                return True
        return False

    @staticmethod
    def get_shape():
        return Piece(5, 0, random.choice(Utils.SHAPES))

    @staticmethod
    def draw_text_middle(text, size, color, surface):
        pass

    @staticmethod
    def draw_grid(surface):
        sx = Utils.TOP_LEFT_X
        sy = Utils.TOP_LEFT_Y
        # Draw grid
        for row in range(Utils.ROWS):
            # horizontal lines
            pygame.draw.line(surface, (128, 128, 128), (sx, sy + row * Utils.BLOCK_SIZE),
                             (sx + Utils.PLAY_W, sy + row * 30))
        for col in range(Utils.COLUMNS):
            # vertical lines
            pygame.draw.line(surface, (128, 128, 128), (sx + col * Utils.BLOCK_SIZE, sy),
                             (sx + col * Utils.BLOCK_SIZE, sy + Utils.PLAY_H))
        return surface

    @staticmethod
    def clear_rows(grid, locked):
        # if a row is clear then shifts other row above down one

        row_full = 0
        for i in range(len(grid) - 1, -1, -1): #from len(grid)-1 to 0 step -1 (from numColums to 0)
            row = grid[i] #grid contains (r,g,b) that is (0,0,0) if cell is empty (grid[i] is a row)
            if (0, 0, 0) not in row:
                row_full += 1 #this increments if the row is full
                # add positions to remove from locked
                ind = i #row i is full
                for j in range(len(row)):
                    try:
                        del locked[(j, i)] #delete row
                    except:
                        continue
        if row_full > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + row_full)
                    locked[newKey] = locked.pop(key) #add row in the top
        return grid,locked

    @staticmethod
    def draw_next_shape(piece, surface):
        #This method draws the next piece in the right side of the screen
        sx = Utils.TOP_LEFT_X + Utils.PLAY_W + 50
        sy = Utils.TOP_LEFT_Y + Utils.PLAY_H / 2 - 100
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255, 255, 255))
        surface.blit(label, (sx + 10, sy - 30))

        format = piece.shape[piece.rotation % len(piece.shape)] #select for every shape the right rotation
        #format = ['.....','...O.','..OO.','..OOO']
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, piece.color, (sx + j*Utils.BLOCK_SIZE, sy + i*Utils.BLOCK_SIZE, Utils.BLOCK_SIZE, Utils.BLOCK_SIZE), 0)


    @staticmethod
    def draw_window(surface, grid, score=0):
        surface.fill((0, 0, 0))
        # Tetris Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, (255, 255, 255))
        surface.blit(label, ((Utils.TOP_LEFT_X + Utils.PLAY_W / 2 - (label.get_width() / 2), 30)))
        # Draw border
        pygame.draw.rect(surface, (255, 0, 0), (Utils.TOP_LEFT_X, Utils.TOP_LEFT_Y, Utils.PLAY_W, Utils.PLAY_H), 3)

        # current score
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Score: ' + str(score), 1, (255, 255, 255))
        surface.blit(label, (Utils.TOP_LEFT_X - 150, Utils.TOP_LEFT_Y + 160))

        #draw blocks
        for i in range(Utils.ROWS):
            for j in range(Utils.COLUMNS):
                pygame.draw.rect(surface, grid[i][j],(Utils.TOP_LEFT_X + j * Utils.BLOCK_SIZE, Utils.TOP_LEFT_Y + i * Utils.BLOCK_SIZE,
                                  Utils.BLOCK_SIZE, Utils.BLOCK_SIZE), 0)
        #draw grid
        surface = PlayField.draw_grid(surface)

        return surface
