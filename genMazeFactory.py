import classNode as cn
from abc import ABC, abstractmethod

# Generic factory method, implements everything needed to generate a blank maze, edgeWall remains as it's used everywhere

class genMazeFactory(ABC):
    def __init__(self, size: tuple):
        self.size = size
        # Mazegen only works with odd number of dimensions, so
        if size[0] % 2 == 0:
            size[0] += 1
        if size[1] % 2 == 0:
            size[1] += 1

        self.x = self.size[0]
        self.y = self.size[1]

        # Create initial maze
        self.maze = [[cn.Node((row, col)) for col in range(self.y)] for row in range(self.x)]
        self.generate()

        # Fill the edges of the maze with walls
    def edgeWall(self):
        y = self.y
        x = self.x
        for i in range(y):
            self.maze[0][i].isWall = True
            self.maze[x - 1][i].isWall = True
        for i in range(x):
            self.maze[i][0].isWall = True
            self.maze[i][y - 1].isWall = True

    @abstractmethod
    def generate(self):  # Main generation algorithm
        self.edgeWall()


