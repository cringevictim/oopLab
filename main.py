import drawMaze
from generateMaze import genMazePrimm, genMazePrimmComplex, genMazeBinaryTree, genMazeBinaryTreeComplex
from pathFinder import *
import pygame

KEY_LIST_PLR = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
KEY_LIST_PLR1 = (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)

SIZE_X = 33  # Only odd numbers # Not bigger than
SIZE_Y = 19

# DO NOT EDIT
FPS = 60
TILE = 48  # Square side in pixels
WIDTH = SIZE_X*TILE
HEIGHT = SIZE_Y*TILE

SCREEN_X, SCREEN_Y = SIZE_X * TILE, SIZE_Y * TILE

if __name__ == '__main__':

    while True:


        # print(path)
        maze_game = drawMaze.MazeGame(WIDTH, HEIGHT, FPS, TILE, KEY_LIST_PLR)
        try:
            maze_game.run_maze()
        except pygame.error as e:
            print(e)
            break