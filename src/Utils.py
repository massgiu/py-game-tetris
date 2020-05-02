import pygame

class Utils:
    SCREEN_W = 800
    SCREEN_H = 700
    PLAY_W = 360  # meaning 300 // 10 = 30 width per block
    PLAY_H = 600  # meaning 600 // 20 = 20 height per block
    BLOCK_SIZE = 30
    INIT_ROW = 0
    INIT_COL = 5

    ROWS = PLAY_H//BLOCK_SIZE  #20 y
    COLUMNS = PLAY_W//BLOCK_SIZE  #10 x


    TOP_LEFT_X = (SCREEN_W - PLAY_W) // 2
    TOP_LEFT_Y = SCREEN_H - PLAY_H

    FALL_SPEED = 0.27

    BACKGROUND_COLOR = (40, 40, 40) #rgb
    EMPTY_CELL_COLOR = (50, 50, 50)  # rgb
    GRID_COLOR = (128, 128, 128)  # rgb
    FONT_COLOR = (255, 255, 255)

    run = True

    # SHAPE FORMATS
    #Every matrix contains one or more vectors where every vector corresponds to a shape and its rotations
    S = [['.....',
          '......',
          '..00..',
          '.00...',
          '.....'],
         ['.....',
          '..0..',
          '..00.',
          '...0.',
          '.....']]

    Z = [['.....',
          '.....',
          '.00..',
          '..00.',
          '.....'],
         ['.....',
          '..0..',
          '.00..',
          '.0...',
          '.....']]

    I = [['..0..',
          '..0..',
          '..0..',
          '..0..',
          '.....'],
         ['.....',
          '0000.',
          '.....',
          '.....',
          '.....']]

    O = [['.....',
          '.....',
          '.00..',
          '.00..',
          '.....']]

    J = [['.....',
          '.0...',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..00.',
          '..0..',
          '..0..',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '...0.',
          '.....'],
         ['.....',
          '..0..',
          '..0..',
          '.00..',
          '.....']]

    L = [['.....',
          '...0.',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..0..',
          '..0..',
          '..00.',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '.0...',
          '.....'],
         ['.....',
          '.00..',
          '..0..',
          '..0..',
          '.....']]

    T = [['.....',
          '..0..',
          '.000.',
          '.....',
          '.....'],
         ['.....',
          '..0..',
          '..00.',
          '..0..',
          '.....'],
         ['.....',
          '.....',
          '.000.',
          '..0..',
          '.....'],
         ['.....',
          '..0..',
          '.00..',
          '..0..',
          '.....']]

    SHAPES = [S, Z, I, O, J, L, T]
    SHAPES_COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

    @staticmethod
    def play_music():
        music = pygame.mixer.music.load("../media/Tetris_Theme.mp3")
        pygame.mixer.music.play(-1)  # -1 will ensure the song keeps looping