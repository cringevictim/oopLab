import random
from genMazeFactory import genMazeFactory as maze


class genMazePrimmComplex(maze):
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
        self.complexify() # Add non-trivial passages
        passages.clear()  # Clear the created list

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
    def complexify(self):
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
                    if cycles > 400:
                        return
                    xr = random.randrange(1, x - 1, 1)
                    yr = random.randrange(1, y - 1, 1)
                self.maze[xr][yr].isWall = False


