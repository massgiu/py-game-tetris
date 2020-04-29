import pygame
from src.PlayField import PlayField
from src.Utils import Utils

pygame.init()
win = pygame.display.set_mode((Utils.SCREEN_W, Utils.SCREEN_H))
pygame.display.set_caption('Tetris')
# locked_positions = {}  # (x,y):(255,0,0)
grid,locked_positions = PlayField.create_grid()

current_piece = PlayField.get_shape()
next_piece = PlayField.get_shape()
clock = pygame.time.Clock()

change_piece = False
fall_time = 0


def main():

    # draw grid and border
    surface = PlayField.draw_grid(win, grid)
    pygame.draw.rect(surface, (255, 0, 0), (Utils.TOP_LEFT_X, Utils.TOP_LEFT_Y, Utils.PLAY_W, Utils.PLAY_H), 5)
    pygame.display.update()

    while Utils.run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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

        PlayField.draw_window(win)

main()
