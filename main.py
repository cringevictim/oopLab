import drawMaze
from generateMaze import generateMaze
from pathFinder import *

SIZE_X = 67# Only odd numbers # Not bigger than
SIZE_Y = 41

# DO NOT EDIT
FPS = 60
TILE = 16  # Square side in pixels
WIDTH = SIZE_X*TILE
HEIGHT = SIZE_Y*TILE

if __name__ == '__main__':
    maze = generateMaze((SIZE_X, SIZE_Y))  # Odd numbers only

    path = pathFinder(maze, (1,1), (SIZE_X-2,SIZE_Y-2))
    for obj in path:
       maze.maze[obj[0]][obj[1]].isPartOfPath = True
    print(path)

    drawMaze.draw_maze(maze, FPS, WIDTH, HEIGHT, TILE)
