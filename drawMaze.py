import pygame
from player import Player

class Sprite(pygame.sprite.Sprite):
    """Create class of wall."""

    # Initialize the data about the sprite
    def __init__(self, x, y, width, height, img, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.screen = screen

    # Draw sprite.
    def draw(self):
        self.screen.blit(self.image, (self.x * self.width, self.y * self.height))


# Method for drawing the maze.
def draw_maze(maze, fps, width, height, tile):
    pygame.init()
    pygame.display.set_caption("Maze")
    screen = pygame.display.set_mode((width, height))
    running = True
    sprites = pygame.sprite.Group()
    # Check each node in generated maze.
    for subList in maze.maze:
        for node in subList:
            if node.isWall:
                wall = Sprite(node.coordinates[0], node.coordinates[1], tile, tile, "wall.png", screen)
                sprites.add(wall)
                wall.draw()

    clock = pygame.time.Clock()

    # Moved from player.py
    objects = []
    plr = Player('yellow', 'green', tile, tile, 0, objects, tile)

    # Main loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Moved from player.py
        keys = pygame.key.get_pressed()
        plr.update(screen, keys, width, height, tile, maze)

        pygame.display.update()
        clock.tick(fps)
