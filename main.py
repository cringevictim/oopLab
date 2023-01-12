import drawMaze
from generateMaze import generateMaze
from pathFinder import *

SIZE_X = 67  # Only odd numbers # Not bigger than
SIZE_Y = 41

# DO NOT EDIT
FPS = 60
TILE = 16  # Square side in pixels
WIDTH = SIZE_X * TILE
HEIGHT = SIZE_Y * TILE

if __name__ == '__main__':
    while True:
        maze = generateMaze((SIZE_X, SIZE_Y))

        pathF = pathFinder(maze, (1, 1), (SIZE_X - 2, SIZE_Y - 2))
        path = pathF.botPathFinder()
        for obj in path:
            maze.maze[obj[0]][obj[1]].isPartOfPath = True
        # print(path)

        maze_game = drawMaze.MazeGame(WIDTH, HEIGHT, FPS, TILE, maze)
        maze_game.add_path(path)
        try:
            maze_game.run_maze()
        except Exception:
            break
