import random
import classNode as cn


class generateMaze:
    def __init__(self, size: tuple):
        self.size = size
        self.maze = [cn.Node((-1, -1)) for i in range(self.size[0] * self.size[1])] #Create initial maze, for now all cells have their coords set to -1, -1

    def EdgeWall(self): #Fills the edges of the maze with walls
        x = self.size[0]
        y = self.size[1]
        for i in range(y):
            self.maze[i].isWall = 1
            self.maze[((x - 1) * y) + i].isWall = 1
        for i in range(x):
            self.maze[i * y].isWall = 1
            self.maze[i * y + (y - 1)].isWall = 1

    def generate(self): #Main generation algorithm
        x = self.size[0]
        y = self.size[1]
        random.seed()

        passages = [] #List that stores all available passages
        xr = random.randrange(1, x - 1, 2) #Picking a random odd cell to start the maze generation from
        yr = random.randrange(1, y - 1, 2)
        initialPassage = [yr, xr, yr, xr] #Initial passage to be between the starting cell and itself
        passages.append(initialPassage) #Writing it to the list of passages

        while len(passages) > 0: 
            p = passages.pop(random.randint(0, len(passages) - 1)) #Removing a random passage out of the list of passages
            yr = p[2]
            xr = p[3]

            if self.maze[(xr * y) + yr].isWall == 1: #If the path to the new passage is a wall, we remove the wall and the cell next to it
                self.maze[(p[1] * y) + p[0]].isWall = 0
                self.maze[(xr * y) + yr].isWall = 0
                
                #This block of code determines new available passages by checking each of the 4 directions for walls and adding that passage to the list of passages
                if xr >= 2 and self.maze[((xr - 2) * y) + yr].isWall == 1:
                    newPassage = [yr, xr - 1, yr, xr - 2]
                    passages.append(newPassage)

                if yr >= 2 and self.maze[(xr * y) + (yr - 2)].isWall == 1:
                    newPassage = [yr - 1, xr, yr - 2, xr]
                    passages.append(newPassage)

                if xr < x - 2 and self.maze[((xr + 2) * y) + yr].isWall == 1:
                    newPassage = [yr, xr + 1, yr, xr + 2]
                    passages.append(newPassage)

                if yr < y - 2 and self.maze[(xr * y) + (yr + 2)].isWall == 1:
                    newPassage = [yr + 1, xr, yr + 2, xr]
                    passages.append(newPassage)
        
        self.EdgeWall() #Wall off the outside of the maze
        passages.clear() #Clear the created list
