import random

class pathFinder:
    def __init__(self, maze, start, end):
        self.steps = 0
        self.start = start
        self.end = end
        self.maze = maze
        self.grid = []
        self.matrix = []
        self.path = []

    def make_step(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == self.steps:
                    if i > 0 and self.matrix[i - 1][j] == 0 and self.grid[i - 1][j] == 0:
                        self.matrix[i - 1][j] = self.steps + 1
                    if j > 0 and self.matrix[i][j - 1] == 0 and self.grid[i][j - 1] == 0:
                        self.matrix[i][j - 1] = self.steps + 1
                    if i < len(self.matrix) - 1 and self.matrix[i + 1][j] == 0 and self.grid[i + 1][j] == 0:
                        self.matrix[i + 1][j] = self.steps + 1
                    if j < len(self.matrix[i]) - 1 and self.matrix[i][j + 1] == 0 and self.grid[i][j + 1] == 0:
                        self.matrix[i][j + 1] = self.steps + 1

    def pathFinder(self):
        self.grid = []
        i = 0
        for subList in self.maze.maze:
            self.grid.append([])
            for obj in subList:
                self.grid[i].append(int(obj.isWall))
                # print(grid)
            i += 1

        self.matrix = []
        for i in range(len(self.grid)):
            self.matrix.append([])
            for j in range(len(self.grid[i])):
                self.matrix[-1].append(0)
        i, j = self.start
        self.matrix[i][j] = 1

        self.steps = 0
        while self.matrix[self.end[0]][self.end[1]] == 0:
            self.steps += 1
            pathFinder.make_step(self)

        i, j = self.end
        self.steps = self.matrix[i][j]
        self.path = [(i, j)]
        while self.steps > 1:
            if i > 0 and self.matrix[i - 1][j] == self.steps - 1:
                i, j = i - 1, j
                self.path.append((i, j))
                self.steps -= 1
            elif j > 0 and self.matrix[i][j - 1] == self.steps - 1:
                i, j = i, j - 1
                self.path.append((i, j))
                self.steps -= 1
            elif i < len(self.matrix) - 1 and self.matrix[i + 1][j] == self.steps - 1:
                i, j = i + 1, j
                self.path.append((i, j))
                self.steps -= 1
            elif j < len(self.matrix[i]) - 1 and self.matrix[i][j + 1] == self.steps - 1:
                i, j = i, j + 1
                self.path.append((i, j))
                self.steps -= 1

        return self.path

    def botPathFinder(self):
        start_tmp = self.start
        end_tmp = self.end

        non_wall_indexes = [(i,j) for i, row in enumerate(self.maze.maze) for j, val in enumerate(row) if  val.isWall == False]
        self.end =  random.choice(non_wall_indexes)

        print(self.end)

        path = self.pathFinder()
        path.pop()

        self.start = self.end
        self.end = end_tmp

        path = path + self.pathFinder()
        self.start = start_tmp

        return path