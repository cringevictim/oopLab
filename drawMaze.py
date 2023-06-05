import time

import pygame
from generateMaze import genMazePrimm, genMazePrimmComplex, genMazeBinaryTree, genMazeBinaryTreeComplex
from pathFinder import PathFinder
from player import Player, Bot
from ui import StartButton, MazeButton, WinLossButton
from main import SCREEN_X, SCREEN_Y, SIZE_X, SIZE_Y



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
    def __init__(self, width, height, fps, tile, KL1):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.screen = pygame.display.set_mode((width, height))
        self.sprites = pygame.sprite.Group()
        self.locked = True

        self.slowed_tick_counter = 1

        self.width = width
        self.height = height

        self.fps = fps
        self.tile = tile
        self.maze = genMazePrimm((SIZE_X, SIZE_Y))
        self.player = Player('yellow', 'black', self.tile, self.tile, KL1)
        self.bot = Bot('red')
        self.play_button = StartButton(self, "Play")
        self.restart_button = StartButton(self, "Restart")

        self.maze_button_width, self.maze_button_height = 150, 50
        self.maze_type_buttons = [
            MazeButton(self, "Maze 1", self.maze_button_width, self.maze_button_height, SCREEN_X * 1 / 5 - self.maze_button_width / 2,
                       SCREEN_Y * 4 / 8 - self.maze_button_height / 2),
            MazeButton(self, "Maze 2", self.maze_button_width, self.maze_button_height, SCREEN_X * 2 / 5 - self.maze_button_width / 2,
                       SCREEN_Y * 4 / 8 - self.maze_button_height / 2),
            MazeButton(self, "Maze 3", self.maze_button_width, self.maze_button_height, SCREEN_X * 3 / 5 - self.maze_button_width / 2,
                       SCREEN_Y * 4 / 8 - self.maze_button_height / 2),
            MazeButton(self, "Maze 4", self.maze_button_width, self.maze_button_height, SCREEN_X * 4 / 5 - self.maze_button_width / 2,
                       SCREEN_Y * 4 / 8 - self.maze_button_height / 2)
        ]
        self.loss_button = WinLossButton(self, "You Lost", self.maze_button_width,
                                         self.maze_button_height, SCREEN_X/2 - self.maze_button_width/2,
                                         SCREEN_Y/2 - self.maze_button_height*2, (255, 0, 0))
        self.win_button = WinLossButton(self, "You Win", self.maze_button_width,
                                         self.maze_button_height, SCREEN_X / 2 - self.maze_button_width / 2,
                                         SCREEN_Y / 2 - self.maze_button_height * 2, (0, 255, 0))

        self.game_active = False

        self.path = None

    def generate_maze(self, choice):
        if choice == 1:
            self.maze = genMazePrimm((SIZE_X, SIZE_Y))
        elif choice == 2:
            self.maze = genMazePrimmComplex((SIZE_X, SIZE_Y))
        elif choice == 3:
            self.maze = genMazeBinaryTree((SIZE_X, SIZE_Y))
        elif choice == 4:
            self.maze = genMazeBinaryTreeComplex((SIZE_X, SIZE_Y))
        player_path = PathFinder(self.maze, (1, 1), (SIZE_X - 2, SIZE_Y - 2)).pathFinder()
        self.bot.add_path(PathFinder(self.maze, (1, 1), (SIZE_X - 2, SIZE_Y - 2)).botPathFinder())
        for obj in player_path:
            self.maze.maze[obj[0]][obj[1]].isPartOfPath = True

    def draw_maze(self):
        # Check each node in generated maze.
        for subList in self.maze.maze:
            for node in subList:
                if node.isWall:
                    wall = Sprite(node.coordinates[0], node.coordinates[1], self.tile, self.tile, "wall.png",
                                  self.screen)
                    self.sprites.add(wall)
                    wall.draw()

    def draw_entity(self, locked):
        if locked: return
        time.sleep(0.05)
        self.slowed_tick_counter+=1
        keys = pygame.key.get_pressed()
        self.player.update(self.screen, keys, self.width, self.height, self.maze)
        if self.slowed_tick_counter == 2:
            self.bot.update(self.screen)
            self.slowed_tick_counter = 0

    def run_maze(self):
        clock = pygame.time.Clock()
        running = True
        show_start_button = True
        show_maze_buttons = False
        start_button_clicked = False
        restart_button_clicked = False
        maze1_clicked, maze2_clicked, maze3_clicked, maze4_clicked = False, False, False, False
        restart = False
        while running:
            if restart and restart_button_clicked:
                restart = False
                restart_button_clicked = False
            self.draw_maze()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise Exception
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    start_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
                    if restart:
                        restart_button_clicked = self.restart_button.rect.collidepoint(mouse_pos)
                    if show_maze_buttons:
                        maze1_clicked = self.maze_type_buttons[0].rect.collidepoint(mouse_pos)
                        maze2_clicked = self.maze_type_buttons[1].rect.collidepoint(mouse_pos)
                        maze3_clicked = self.maze_type_buttons[2].rect.collidepoint(mouse_pos)
                        maze4_clicked = self.maze_type_buttons[3].rect.collidepoint(mouse_pos)
            if not start_button_clicked and show_start_button:
                self.play_button.draw_button()
            elif show_start_button and start_button_clicked:
                show_start_button = False
                show_maze_buttons = True
                self.screen.fill((0, 0, 0))
                self.play_button.kill()
            elif show_maze_buttons:
                self.maze_type_buttons[0].draw_button()
                self.maze_type_buttons[1].draw_button()
                self.maze_type_buttons[2].draw_button()
                self.maze_type_buttons[3].draw_button()

            if maze1_clicked and show_maze_buttons:
                self.generate_maze(1)
                show_maze_buttons = False
                self.screen.fill((0, 0, 0))
                self.locked = False
            elif maze2_clicked and show_maze_buttons:
                self.generate_maze(2)
                show_maze_buttons = False
                self.screen.fill((0, 0, 0))
                self.locked = False
            elif maze3_clicked and show_maze_buttons:
                self.generate_maze(3)
                show_maze_buttons = False
                self.screen.fill((0, 0, 0))
                self.locked = False
            elif maze4_clicked and show_maze_buttons:
                self.generate_maze(4)
                show_maze_buttons = False
                self.screen.fill((0, 0, 0))
                self.locked = False

            if self.player.rect.x == (SIZE_X-2)*self.tile and self.player.rect.y == (SIZE_Y-2)*self.tile:
                self.locked = True
                self.win_button.draw_button()
                self.restart_button.draw_button()
                restart = True

            if self.bot.px == (SIZE_X-2) and self.bot.py == (SIZE_Y-2):
                self.locked = True
                self.loss_button.draw_button()
                self.restart_button.draw_button()
                restart = True

            if restart_button_clicked and restart:
                break


            self.draw_entity(self.locked)
            pygame.display.update()
            clock.tick(self.fps)

