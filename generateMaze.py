import classNode as cn
import random
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

    # Simple function to check the 3x3 box around the selected cell
    def patternCheck(self, b00, b10, b20, b01, b11, b21, b02, b12, b22, x, y):
        if self.maze[x - 1][y - 1].isWall == b00 and self.maze[x][y-1].isWall == b10 and self.maze[x+1][y-1].isWall == b20 \
                and self.maze[x-1][y].isWall == b01 and self.maze[x][y].isWall == b11 and self.maze[x+1][y].isWall == b21 \
                and self.maze[x-1][y+1].isWall == b02 and self.maze[x][y+1].isWall == b12 and self.maze[x+1][y+1].isWall == b22:
            return True
        else:
            return False

    # Checks if a selected cell is one of the allowed wall configurations, if so, it's slated for removal
    def checkComplexCompliance(self, x, y):
        t = True
        f = False
        if self.patternCheck(t,t,t,
                             f,t,f,
                             t,t,t, x, y):
            return True

        if self.patternCheck(t,f,t,
                             t,t,t,
                             t,f,t, x, y):
            return True

        if self.patternCheck(t,t,f,
                             f,t,f,
                             t,t,t, x, y):
            return True

        if self.patternCheck(f,t,t,
                             f,t,f,
                             t,t,t, x, y):
            return True

        if self.patternCheck(t,f,f,
                             t,t,t,
                             t,f,t, x, y):
            return True

        if self.patternCheck(t,f,t,
                             t,t,t,
                             t,f,f, x, y):
            return True

        if self.patternCheck(t,t,t,
                             f,t,f,
                             t,t,f, x, y):
            return True

        if self.patternCheck(t,t,t,
                             f,t,f,
                             f,t,t, x, y):
            return True

        if self.patternCheck(t,f,t,
                             t,t,t,
                             f,f,t, x, y):
            return True

        if self.patternCheck(f,f,t,
                             t,t,t,
                             t,f,t, x, y):
            return True

        return False

    # Function tries to add N new passages into maze
    def complexify(self, n_cycles):
        x = self.x
        y = self.y
        random.seed()
        for i in range(x):
            xr = random.randrange(1, x - 1, 1)
            yr = random.randrange(1, y - 1, 1)
            if self.checkComplexCompliance(xr, yr):
                self.maze[xr][yr].isWall = False
            else:
                cycles = 0
                while not self.checkComplexCompliance(xr, yr):
                    cycles += 1
                    # If the maze runs out of new passages, it will attempt to generate it 400 times before failing
                    if cycles > n_cycles:
                        return
                    xr = random.randrange(1, x - 1, 1)
                    yr = random.randrange(1, y - 1, 1)
                self.maze[xr][yr].isWall = False


    @abstractmethod
    def generate(self):  # Main generation algorithm
        self.edgeWall()


# Generates a maze using the naive Primm algorithm
class genMazePrimm(genMazeFactory):
    def generate(self):  # Main generation algorithm
        x = self.x
        y = self.y
        random.seed()

        passages = []  # List that stores all available passages
        xr = random.randrange(1, x - 1, 2)  # Picking a random odd cell to start the maze generation from
        yr = random.randrange(1, y - 1, 2)
        initialPassage = [yr, xr, yr, xr]  # Initial passage to be between the starting cell and itself
        passages.append(initialPassage)  # Writing it to the list of passages

        while len(passages) > 0:
            p = passages.pop(
                random.randint(0, len(passages) - 1))  # Removing a random passage out of the list of passages
            yr = p[2]
            xr = p[3]

            if self.maze[xr][yr].isWall == True:  # If the path to the new passage is a wall, we remove the wall
                # and the cell next to it
                self.maze[p[1]][p[0]].isWall = False
                self.maze[xr][yr].isWall = False

                # This block of code determines new available passages by checking each of the 4 directions for
                # walls and adding that passage to the list of passages
                if xr >= 2 and self.maze[xr - 2][yr].isWall == True:
                    newPassage = [yr, xr - 1, yr, xr - 2]
                    passages.append(newPassage)

                if yr >= 2 and self.maze[xr][yr - 2].isWall == True:
                    newPassage = [yr - 1, xr, yr - 2, xr]
                    passages.append(newPassage)

                if xr < x - 2 and self.maze[xr + 2][yr].isWall == True:
                    newPassage = [yr, xr + 1, yr, xr + 2]
                    passages.append(newPassage)

                if yr < y - 2 and self.maze[xr][yr + 2].isWall == True:
                    newPassage = [yr + 1, xr, yr + 2, xr]
                    passages.append(newPassage)

        self.edgeWall()      # Wall off the outside of the maze
        passages.clear()  # Clear the created list


# Same as Primm, but added complex passages, so that there is more than one solution to the maze
class genMazePrimmComplex(genMazeFactory):
    def generate(self):  # Main generation algorithm
        x = self.x
        y = self.y
        random.seed()

        passages = []  # List that stores all available passages
        xr = random.randrange(1, x - 1, 2)  # Picking a random odd cell to start the maze generation from
        yr = random.randrange(1, y - 1, 2)
        initialPassage = [yr, xr, yr, xr]  # Initial passage to be between the starting cell and itself
        passages.append(initialPassage)  # Writing it to the list of passages

        while len(passages) > 0:
            p = passages.pop(
                random.randint(0, len(passages) - 1))  # Removing a random passage out of the list of passages
            yr = p[2]
            xr = p[3]

            if self.maze[xr][yr].isWall == True:  # If the path to the new passage is a wall, we remove the wall
                # and the cell next to it
                self.maze[p[1]][p[0]].isWall = False
                self.maze[xr][yr].isWall = False

                # This block of code determines new available passages by checking each of the 4 directions for
                # walls and adding that passage to the list of passages
                if xr >= 2 and self.maze[xr - 2][yr].isWall == True:
                    newPassage = [yr, xr - 1, yr, xr - 2]
                    passages.append(newPassage)

                if yr >= 2 and self.maze[xr][yr - 2].isWall == True:
                    newPassage = [yr - 1, xr, yr - 2, xr]
                    passages.append(newPassage)

                if xr < x - 2 and self.maze[xr + 2][yr].isWall == True:
                    newPassage = [yr, xr + 1, yr, xr + 2]
                    passages.append(newPassage)

                if yr < y - 2 and self.maze[xr][yr + 2].isWall == True:
                    newPassage = [yr + 1, xr, yr + 2, xr]
                    passages.append(newPassage)

        self.edgeWall()   # Wall off the outside of the maze
        self.complexify(400) # Add non-trivial passages
        passages.clear()  # Clear the created list


# Generates a maze which visually resembles a binary tree, usually simple to solve
class genMazeBinaryTree(genMazeFactory):
    def generate(self):  # Main generation algorithm
        x = self.x
        y = self.y

        biases = {
            "NW": [(1, 0), (0, -1)],
            "NE": [(1, 0), (0, 1)],
            "SW": [(-1, 0), (0, -1)],
            "SE": [(-1, 0), (0, 1)]}
        key = random.choice(list(biases.keys()))
        bias = biases[key]

        for i in range(1, x, 2):
            for j in range(1, y, 2):
                self.maze[i][j].isWall = False
                neighbor_i, neighbor_j = self.find_neighbor(i,j, bias)
                self.maze[neighbor_i][neighbor_j].isWall = False
        self.edgeWall()
    def find_neighbor(self, row, col, bias):
        x = self.x
        y = self.y
        neighbors = []
        for b_row, b_col in bias:
            n_row = row + b_row
            n_col = col + b_col
            if 0 < n_row < (x - 1) and 0 < n_col < (y - 1):
                neighbors.append((n_row, n_col))
        if len(neighbors) == 0:
            return row, col
        else:
            return random.choice(neighbors)

# Generates a maze which visually resembles a binary tree, complexed up
class genMazeBinaryTreeComplex(genMazeFactory):
    def generate(self):  # Main generation algorithm
        x = self.x
        y = self.y

        biases = {
            "NW": [(1, 0), (0, -1)],
            "NE": [(1, 0), (0, 1)],
            "SW": [(-1, 0), (0, -1)],
            "SE": [(-1, 0), (0, 1)]}
        key = random.choice(list(biases.keys()))
        bias = biases[key]

        for i in range(1, x, 2):
            for j in range(1, y, 2):
                self.maze[i][j].isWall = False
                neighbor_i, neighbor_j = self.find_neighbor(i,j, bias)
                self.maze[neighbor_i][neighbor_j].isWall = False

        self.complexify(10000)
        self.edgeWall()
    def find_neighbor(self, row, col, bias):
        x = self.x
        y = self.y
        neighbors = []
        for b_row, b_col in bias:
            n_row = row + b_row
            n_col = col + b_col
            if 0 < n_row < (x - 1) and 0 < n_col < (y - 1):
                neighbors.append((n_row, n_col))
        if len(neighbors) == 0:
            return row, col
        else:
            return random.choice(neighbors)
