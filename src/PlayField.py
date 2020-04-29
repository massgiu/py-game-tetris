from src.Piece import Piece
from src.Utils import Utils
import pygame
import random

class PlayField:

    @staticmethod
    def create_grid(locked_positions={}): #locked_positions is a dictionary (keys=coordinates, values=rgb colors)
        grid = [[(0, 0, 0) for x in range(Utils.COLUMNS)] for x in range(Utils.ROWS)]

        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                if (row, col) in locked_positions:
                    c = locked_positions[(row, col)]
                    grid[col][row] = c
        return grid, locked_positions

    @staticmethod
    def convert_shape_format(shape):
        pass

    @staticmethod
    def valid_space(shape, grid):
        pass

    @staticmethod
    def check_lost(positions):
        pass

    @staticmethod
    def get_shape():
        return Piece(5, 0, random.choice(Utils.SHAPES))

    @staticmethod
    def draw_text_middle(text, size, color, surface):
        pass

    @staticmethod
    def draw_grid(surface, grid):
        surface.fill((0, 0, 0)) #black background
        # Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, (255,255,255))
        surface.blit(label, (Utils.TOP_LEFT_Y + Utils.PLAY_W - (label.get_width() / 2), 30))
        # Draw grid
        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                pygame.draw.rect(surface, (100,100,100), (Utils.TOP_LEFT_X + col * 30, Utils.TOP_LEFT_Y + row * 30, 30, 30), 1)
        return surface

    @staticmethod
    def clear_rows(grid, locked):
        pass

    @staticmethod
    def draw_next_shape(shape, surface):
        pass

    @staticmethod
    def draw_window(surface):
        pass