import random
from Node import Node

class generateMaze:
    def __init__(self, size: tuple):
        self.size = size
        self.maze = [1 for i in range(self.size[0] * self.size[1])]

    def EdgeWall(self):
        x = self.size[0]
        y = self.size[1]
        for i in range(y):
            self.maze[i] = 1
            self.maze[((x - 1) * y) + i] = 1
        for i in range(x):
            self.maze[i * y] = 1
            self.maze[i * y + (y - 1)] = 1

    def generate(self):
        x = self.size[0]
        y = self.size[1]
        random.seed()

        passages = []
        xr = random.randrange(1, x - 1, 2)
        yr = random.randrange(1, y - 1, 2)
        initialPassage = [yr, xr, yr, xr]
        passages.append(initialPassage)

        while len(passages) > 0:
            p = passages.pop(random.randint(0, len(passages) - 1))
            yr = p[2]
            xr = p[3]

            if (self.maze[(xr * y) + yr] == 1):
                self.maze[(p[1]*y) + p[0]] = 0
                self.maze[(xr * y) + yr] = 0

                if xr >= 2 and self.maze[((xr-2)*y) + yr] == 1:
                    newPassage = [yr, xr - 1, yr, xr - 2]
                    passages.append(newPassage)

                if yr >= 2 and self.maze[(xr*y) + (yr-2)] == 1:
                    newPassage = [yr-1, xr, yr - 2, xr]
                    passages.append(newPassage)

                if xr < x - 2 and self.maze[((xr+2)*y) + yr] == 1:
                    newPassage = [yr, xr + 1, yr, xr + 2]
                    passages.append(newPassage)

                if yr < y - 2 and self.maze[(xr * y) + (yr + 2)] == 1:
                    newPassage = [yr + 1, xr, yr + 2, xr]
                    passages.append(newPassage)

        self.EdgeWall()
        passages.clear()
