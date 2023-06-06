import drawMaze
from generateMaze import genMazePrimm, genMazePrimmComplex, genMazeBinaryTree, genMazeBinaryTreeComplex
from pathFinder import *
import pygame

KEY_LIST_PLR = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
KEY_LIST_PLR1 = (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
KEY_LIST_PLR2 = (pygame.K_q, pygame.K_h, pygame.K_g, pygame.K_p)

SIZE_X = 67  # Only odd numbers # Not bigger than
SIZE_Y = 41

# DO NOT EDIT
FPS = 60
TILE = 16  # Square side in pixels
WIDTH = SIZE_X*TILE
HEIGHT = SIZE_Y*TILE

if __name__ == '__main__':
    while True:
        maze = generateMaze((SIZE_X, SIZE_Y))

        pathF = pathFinder(maze, (1,1), (SIZE_X-2,SIZE_Y-2))
        path = pathF.pathFinder()
        for obj in path:
           maze.maze[obj[0]][obj[1]].isPartOfPath = True
        # print(path)
        maze_game = drawMaze.MazeGame(WIDTH, HEIGHT, FPS, TILE, maze, KEY_LIST_PLR, KEY_LIST_PLR1, KEY_LIST_PLR2)
        maze_game.add_path(path)
        maze_game.run_maze()
        pygame.quit()
        try:
            maze_game.run_maze()
        except Exception:
            break
