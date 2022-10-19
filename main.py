import drawMaze
from generateMaze import generateMaze

SIZE_X = 47  # Only odd numbers
SIZE_Y = 29

# DO NOT EDIT
FPS = 60
TILE = 32  # Square side in pixels
WIDTH = SIZE_X*TILE
HEIGHT = SIZE_Y*TILE

if __name__ == '__main__':
    maze = generateMaze((SIZE_X, SIZE_Y))  # Odd numbers only
    maze.maze[1][1].isPartOfPath = True
    drawMaze.draw_maze(maze, FPS, WIDTH, HEIGHT, TILE)
