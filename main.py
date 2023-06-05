import drawMaze
from generateMaze import genMazePrimm, genMazePrimmComplex, genMazeBinaryTree, genMazeBinaryTreeComplex
from pathFinder import *
import pygame
from exceptions import EndGameException

SIZE_X = 67  # Only odd numbers # Not bigger than
SIZE_Y = 41

# DO NOT EDIT
FPS = 60
TILE = 16  # Square side in pixels
WIDTH = SIZE_X*TILE
HEIGHT = SIZE_Y*TILE

if __name__ == '__main__':

    while True:
        maze_game = drawMaze.MazeGame(
            WIDTH, HEIGHT, FPS, TILE)
        maze_game.choose_maze()
        try:
            maze_game.run_maze()
        except EndGameException:
            break
        except Exception as ex:
            print(f"The game exited unexpectedly: {ex}")
            break
