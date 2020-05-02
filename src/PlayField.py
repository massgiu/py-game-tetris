from src.Utils import Utils
import pygame


class PlayField:

    @staticmethod
    def create_grid(locked_positions={}):  # locked_positions is a dictionary (keys=coordinates, values=rgb colors)
        grid = [[Utils.EMPTY_CELL_COLOR for x in range(Utils.COLUMNS)] for x in range(Utils.ROWS)]

        for row in range(Utils.ROWS):
            for col in range(Utils.COLUMNS):
                if (col, row) in locked_positions:
                    c = locked_positions[(col, row)]
                    grid[row][col] = c
        return grid


    @staticmethod
    def check_lost(positions):
        for pos in positions:
            x, y = pos
            if y < 1:  # means that a piece is over the screen height
                return True
        return False


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
            pygame.draw.line(surface, Utils.GRID_COLOR, (sx, sy + row * Utils.BLOCK_SIZE),
                             (sx + Utils.PLAY_W, sy + row * Utils.BLOCK_SIZE))
        for col in range(Utils.COLUMNS):
            # vertical lines
            pygame.draw.line(surface, Utils.GRID_COLOR, (sx + col * Utils.BLOCK_SIZE, sy),
                             (sx + col * Utils.BLOCK_SIZE, sy + Utils.PLAY_H))
        return surface

    @staticmethod
    def clear_rows(grid, locked):
        # if a row is clear then shifts other row above down one

        row_full = 0
        for i in range(len(grid) - 1, -1, -1): #from len(grid)-1 to 0 step -1 (from numColums to 0)
            row = grid[i] #grid contains (r,g,b) that is (0,0,0) if cell is empty (grid[i] is a row)
            if Utils.EMPTY_CELL_COLOR not in row:
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
        return grid,locked, row_full

    @staticmethod
    def draw_next_shape(piece, surface):
        #This method draws the next piece in the right side of the screen
        sx = Utils.TOP_LEFT_X + Utils.PLAY_W + 50
        sy = Utils.TOP_LEFT_Y + Utils.PLAY_H / 2 - 150
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, Utils.FONT_COLOR)
        surface.blit(label, (sx + 10, sy - 30))

        format = piece.shape[piece.rotation % len(piece.shape)] #select for every shape the right rotation
        #format = ['.....','...O.','..OO.','..OOO']
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, piece.color, (sx + j*Utils.BLOCK_SIZE, sy + i*Utils.BLOCK_SIZE,
                                                            Utils.BLOCK_SIZE, Utils.BLOCK_SIZE), 0)


    @staticmethod
    def draw_window(surface, grid, score=0):

        #background image
        bg = pygame.image.load("../media/bg.jpg")
        surface.blit(bg, (0, 0))

        # surface.fill(Utils.BACKGROUND_COLOR)
        # Tetris Title
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('TETRIS', 1, Utils.FONT_COLOR)
        surface.blit(label, ((Utils.TOP_LEFT_X + Utils.PLAY_W / 2 - (label.get_width() / 2), 30)))
        # Draw border
        pygame.draw.rect(surface, (0, 0, 255), (Utils.TOP_LEFT_X, Utils.TOP_LEFT_Y, Utils.PLAY_W, Utils.PLAY_H), 3)

        # current score
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Score: ' + str(score), 1, Utils.FONT_COLOR)
        surface.blit(label, (Utils.TOP_LEFT_X - 150, Utils.TOP_LEFT_Y + 110))

        #draw blocks
        for i in range(Utils.ROWS):
            for j in range(Utils.COLUMNS):
                pygame.draw.rect(surface, grid[i][j],(Utils.TOP_LEFT_X + j * Utils.BLOCK_SIZE, Utils.TOP_LEFT_Y + i * Utils.BLOCK_SIZE,
                                  Utils.BLOCK_SIZE, Utils.BLOCK_SIZE), 0)
        #draw grid
        surface = PlayField.draw_grid(surface)

        return surface
