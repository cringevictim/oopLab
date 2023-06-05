import pygame
import time
from main import SIZE_X, SIZE_Y, TILE
class Bot:
    def __init__(self, botColor):
        self.type = 'bot'
        self.oldX = TILE
        self.oldY = TILE
        self.px = None
        self.py = None

        self.bot_path = None

        self.botColor = botColor
        self.rect = pygame.Rect((SIZE_X - 2)*TILE, (SIZE_Y - 2)*TILE, TILE, TILE)
        self.old_rect = pygame.Rect((SIZE_X - 2)*TILE, (SIZE_Y - 2)*TILE, TILE, TILE)

    def add_path(self, path):
        print(path)
        self.bot_path = path
    def update(self, window):
        element = self.bot_path.pop(0)
        self.old_rect = self.rect
        self.rect = pygame.Rect(((element[0]) * TILE, (element[1]) * TILE), (TILE, TILE))
        self.px, self.py = element[0], element[1]
        pygame.draw.rect(window, self.botColor, self.rect)
        pygame.draw.rect(window, 'black', self.old_rect)


class Player:
    def __init__(self, playerColor, pathColor, px, py, keyList):
        self.type = 'player'
        self.oldX = TILE
        self.oldY = TILE

        self.playerColor = playerColor
        self.pathColor = pathColor
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.rectOld = pygame.Rect(self.oldX, self.oldY, TILE, TILE)


        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]

    def update(self, window, keys, width, height, maze):
        self.rectOld = pygame.Rect(self.oldX, self.oldY, TILE, TILE)
        if maze.maze[int(self.oldX/TILE)][int(self.oldY/TILE)].isPartOfPath:
            pygame.draw.rect(window, self.pathColor, self.rectOld)
        else:
            pygame.draw.rect(window, 'black', self.rectOld)

        if keys[self.keyLEFT] and self.rect.x > TILE and not maze.maze[int(self.rect.x/TILE-1)][int(self.rect.y/TILE)].isWall:
            self.rect.x -= TILE
        elif keys[self.keyRIGHT] and self.rect.x < width - TILE*2 and not maze.maze[int(self.rect.x/TILE+1)][int(self.rect.y/TILE)].isWall:
            self.rect.x += TILE
        elif keys[self.keyUP] and self.rect.y > TILE and not maze.maze[int(self.rect.x/TILE)][int(self.rect.y/TILE)-1].isWall:
            self.rect.y -= TILE
        elif keys[self.keyDOWN] and self.rect.y < height - TILE*2 and not maze.maze[int(self.rect.x/TILE)][int(self.rect.y/TILE)+1].isWall:
            self.rect.y += TILE

        self.oldX = self.rect.x
        self.oldY = self.rect.y

        pygame.draw.rect(window, self.playerColor, self.rect)
