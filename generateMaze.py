import random
import classNode as cn

class generateMaze:
    def __init__(self, size: tuple):
        self.size = size
        # Mazegen only works with odd number of dimensions, so
        if size[0] % 2 == 0:
            size[0] += 1
        if size[1] % 2 == 0:
            size[1] += 1

        x = self.size[0]
        y = self.size[1]

        # Create initial maze
        self.maze = [[cn.Node((row, col)) for col in range(y)] for row in range(x)]

        # Fill the edges of the maze with walls
        def __EdgeWall():
            for i in range(y):
                self.maze[0][i].isWall = True
                self.maze[x - 1][i].isWall = True
            for i in range(x):
                self.maze[i][0].isWall = True
                self.maze[i][y - 1].isWall = True

        def __generate():  # Main generation algorithm
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

            __EdgeWall()  # Wall off the outside of the maze
            passages.clear()  # Clear the created list

        __generate()
