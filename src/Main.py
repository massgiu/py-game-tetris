import pygame
from src.PlayField import PlayField
from src.Utils import Utils

pygame.init()
win = pygame.display.set_mode((Utils.SCREEN_W, Utils.SCREEN_H))
pygame.display.set_caption('Tetris')

# grid,locked_positions = PlayField.create_grid()

clock = pygame.time.Clock()

def main():
    global win
    locked_positions = {}  # (x,y):(255,0,0)

    # init grid
    grid = PlayField.create_grid() #matrix that contains (r,g,b)
    win = PlayField.draw_window(win, grid, 0)
    current_piece = PlayField.get_shape() #this gets a Piece
    next_piece = PlayField.get_shape() #this gets another Piece
    change_piece = False
    fall_time = 0
    score = 0

    while Utils.run:
        grid = PlayField.create_grid(locked_positions)
        fall_time+= clock.get_rawtime()
        clock.tick()
        # Piece goes down anyay
        if fall_time / 1000 >= Utils.FALL_SPEED:
            fall_time = 0
            current_piece.y += 1
            if not (PlayField.valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1 #avoid piece to go out
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Utils.run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not PlayField.valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not PlayField.valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not PlayField.valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not PlayField.valid_space(current_piece, grid):
                        current_piece.y -= 1

        # add color of piece to the grid for drawing
        shape_pos = PlayField.convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i] #get position of piece
            #Update grid
            if y > -1:  # If we are not above the screen
                grid[y][x] = current_piece.color
        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos: #shape pos are tuple (x,y) for every block
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color #update locked positions
            current_piece = next_piece
            next_piece = PlayField.get_shape()
            change_piece = False
            grid, locked_positions = PlayField.clear_rows(grid, locked_positions)

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
            # update_score(score)

main()
