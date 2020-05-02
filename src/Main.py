import pygame

from src.PlayField import PlayField
from src.Utils import Utils
from src.Piece import Piece
import random

pygame.init()
win = pygame.display.set_mode((Utils.SCREEN_W, Utils.SCREEN_H))
pygame.display.set_caption('Tetris')
Utils.play_music()

clock = pygame.time.Clock()

def main():
    global win
    locked_positions = {}  # (x,y):(255,0,0)

    # init grid
    grid = PlayField.create_grid() #matrix that contains (r,g,b)
    win = PlayField.draw_window(win, grid, 0)
    current_piece = Piece(Utils.INIT_COL, Utils.INIT_ROW, random.choice(Utils.SHAPES))
    next_piece = Piece(Utils.INIT_COL, Utils.INIT_ROW, random.choice(Utils.SHAPES))
    change_piece = False
    fall_time = 0
    score = 0

    while Utils.run:
        grid = PlayField.create_grid(locked_positions)
        fall_time+= clock.get_rawtime()
        clock.tick()
        # Piece goes down anyway
        if fall_time / 1000 >= Utils.FALL_SPEED:
            fall_time = 0
            current_piece.row += 1
            #Check if the piece is blocked (if yes, the row can't be incremented) and we chage piece
            if not (current_piece.is_in_valid_space(grid)) and current_piece.row > 0:
                current_piece.row -= 1 #avoid piece to across other pieces
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Utils.run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.shift_left(grid)

                if event.key == pygame.K_RIGHT:
                    current_piece.shift_right(grid)

                if event.key == pygame.K_UP:
                    current_piece.rotate(grid)

                if event.key == pygame.K_DOWN:
                    current_piece.go_down(grid)

        # add color of piece to the grid for drawing
        grid = current_piece.update_grid(grid)
        shape_pos = current_piece.convert_shape_format()

        # if piece hit other pieces and is blocked
        if change_piece:
            for pos in shape_pos: #shape pos are tuple (x,y) for every block
                p = (pos[1], pos[0])
                locked_positions[p] = current_piece.color #update locked positions
            #swap piece
            current_piece = next_piece
            next_piece = Piece(Utils.INIT_COL, Utils.INIT_ROW, random.choice(Utils.SHAPES))
            change_piece = False
            grid, locked_positions, inc_score = PlayField.clear_rows(grid, locked_positions)
            score += inc_score

        #Update display
        win = PlayField.draw_window(win, grid, score)
        PlayField.draw_next_shape(next_piece, win) #piece on the right side
        pygame.display.update()

        if PlayField.check_lost(locked_positions):
            print("check_lost TRUE")
            Utils.run = False
            pygame.display.update()
            #pygame.time.delay(1500)
            Utils.run = False

main()
