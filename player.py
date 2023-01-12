import pygame
import time

class Player:
    def __init__(self, playerColor, pathColor, px, py, direct, objects, tile, keyList):
        objects.append(self)
        self.type = 'player'
        self.oldX = tile
        self.oldY = tile

        self.playerColor = playerColor
        self.pathColor = pathColor
        self.rect = pygame.Rect(px, py, tile, tile)
        self.rectOld = pygame.Rect(self.oldX, self.oldY, tile, tile)
        self.direct = direct

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]

    def update(self, window, keys, width, height, tile, maze):
        timeToSleep = 0.1
        self.rectOld = pygame.Rect(self.oldX, self.oldY, tile, tile)
        if maze.maze[int(self.oldX/tile)][int(self.oldY/tile)].isPartOfPath:
            pygame.draw.rect(window, self.pathColor, self.rectOld)
        else:
            pygame.draw.rect(window, 'black', self.rectOld)

        if keys[self.keyLEFT] and self.rect.x > tile and not maze.maze[int(self.rect.x/tile-1)][int(self.rect.y/tile)].isWall:
            self.rect.x -= tile
            time.sleep(timeToSleep)
        elif keys[self.keyRIGHT] and self.rect.x < width - tile*2 and not maze.maze[int(self.rect.x/tile+1)][int(self.rect.y/tile)].isWall:
            self.rect.x += tile
            time.sleep(timeToSleep)
        elif keys[self.keyUP] and self.rect.y > tile and not maze.maze[int(self.rect.x/tile)][int(self.rect.y/tile)-1].isWall:
            self.rect.y -= tile
            time.sleep(timeToSleep)
        elif keys[self.keyDOWN] and self.rect.y < height - tile*2 and not maze.maze[int(self.rect.x/tile)][int(self.rect.y/tile)+1].isWall:
            self.rect.y += tile
            time.sleep(timeToSleep)

        self.oldX = self.rect.x
        self.oldY = self.rect.y

        pygame.draw.rect(window, self.playerColor, self.rect)
