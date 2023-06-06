import pygame
from player import Player
from button import Button


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


class MazeGame:
    def __init__(self, width, height, fps, tile, maze, KL1, KL2, KL3):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.screen = pygame.display.set_mode((width, height))
        self.sprites = pygame.sprite.Group()

        self.width = width
        self.height = height

        self.fps = fps
        self.tile = tile
        self.maze = maze

        objects = []
        self.player = Player('yellow', 'green', self.tile, self.tile+608, 0, objects, self.tile, KL1)
        self.player1 = Player('blue', 'red', self.tile, self.tile, 0, objects, self.tile, KL2)
         self.playerBot = Player('white', 'orange', self.tile+1024, self.tile, 0, objects, self.tile, KL3)
        self.play_button = Button(self, "Play")
        self.restart_button = Button(self, "Restart game")

        self.game_active = False

        self.path = None

    def draw_maze(self):
        # Check each node in generated maze.
        for subList in self.maze.maze:
            for node in subList:
                if node.isWall:
                    wall = Sprite(node.coordinates[0], node.coordinates[1], self.tile, self.tile, "wall.png",
                                  self.screen)
                    self.sprites.add(wall)
                    wall.draw()

    def draw_player(self):
        keys = pygame.key.get_pressed()
        self.player.update(self.screen, keys, self.width, self.height, self.tile, self.maze)
        self.player1.update(self.screen, keys, self.width, self.height, self.tile, self.maze)
        self.playerBot.updated(self.screen, keys, self.width, self.height, self.tile, self.maze)

    def add_path(self, path):
        self.path = path

    def run_maze(self):
        clock = pygame.time.Clock()
        running = True
        show_button = True
        button_clicked = False
        restart_button_clicked = False
        restart = False
        while running:
            self.draw_maze()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise Exception
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
                    restart_button_clicked = self.restart_button.rect.collidepoint(mouse_pos)
            if not button_clicked and show_button:
                self.play_button.draw_button()
            elif show_button:
                self.screen.fill((0, 0, 0))
                show_button = False
                self.play_button.kill()
            if button_clicked and not restart:
                restart_button_clicked = None
            if self.path and self.player.rect.x == 65*self.tile and self.player.rect.y == 39*self.tile:
                self.restart_button.draw_button()
                restart = True
            if restart_button_clicked and restart:
                break

            self.draw_player()
            pygame.display.update()
            clock.tick(self.fps)
