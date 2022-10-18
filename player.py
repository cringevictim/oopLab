import pygame
from main import Node
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Player:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'player'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]


    def update(self):
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
        for obj in objects:
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def draw(self):
        pygame.draw.rect(window, self.color,  self.rect)

objects = []

Player('blue', 10, 10, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN))
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for obj in objects: obj.update()
    window.fill('black')
    for obj in objects: obj.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()