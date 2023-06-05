import pygame
import pygame.font
from player import Player
from button import Button
from exceptions import EndGameException
from generateMaze import genMazePrimm, genMazePrimmComplex, genMazeBinaryTree, genMazeBinaryTreeComplex
from pathFinder import *
pygame.init()
KEY_LIST_PLR = (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
KEY_LIST_PLR1 = (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)

SIZE_X = 67  # Only odd numbers # Not bigger than
SIZE_Y = 41

TEXT_FONT = pygame.font.Font(None, 36)
TEXT_COLOR_WHITE = (255, 255, 255)


class Sprite(pygame.sprite.Sprite):
    """Create class of wall."""

    # Initialize the data about the sprite
    def __init__(self, x, y, width, height, img, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.image = pygame.transform.scale(
            pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.screen = screen

    # Draw sprite.
    def draw(self):
        self.screen.blit(
            self.image, (self.x * self.width, self.y * self.height))


class MazeGame:
    def __init__(self, width, height, fps, tile):
        pygame.init()
        pygame.display.set_caption("Maze")
        self.screen = pygame.display.set_mode((width, height))
        self.sprites = pygame.sprite.Group()

        self.width = width
        self.height = height

        self.fps = fps
        self.tile = tile

    def choose_maze(self):

        choice_primm = Button(self, "Primm's algorithm", (-250, -100))
        choice_primm_complex = Button(
            self, "Primm's algorithm complex", (250, -100))
        choice_binary_tree = Button(self, "Binary tree algorithm", (-250, 100))
        choice_binary_tree_complex = Button(
            self, "Binary tree algorithm complex", (250, 100))
        maze_choosen = False
        while True:
            clock = pygame.time.Clock()
            self.screen.fill((0, 0, 0))
            choice_primm.draw_button()
            choice_primm_complex.draw_button()
            choice_binary_tree.draw_button()
            choice_binary_tree_complex.draw_button()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if choice_primm.rect.collidepoint(mouse_pos):
                        maze = genMazePrimm((SIZE_X, SIZE_Y))
                    elif choice_primm_complex.rect.collidepoint(mouse_pos):
                        maze = genMazePrimmComplex((SIZE_X, SIZE_Y))
                    elif choice_binary_tree.rect.collidepoint(mouse_pos):
                        maze = genMazeBinaryTree((SIZE_X, SIZE_Y))
                    elif choice_binary_tree_complex.rect.collidepoint(mouse_pos):
                        maze = genMazeBinaryTreeComplex((SIZE_X, SIZE_Y))
                    else:
                        continue
                    maze_choosen = True
                    break
            if maze_choosen:
                self.screen.fill((0, 0, 0))
                break

            clock.tick(self.fps)

        self.setup_maze(maze, KEY_LIST_PLR, KEY_LIST_PLR1)

    def setup_maze(self, maze, KL1, KL2):
        pathF = pathFinder(maze, (1, (SIZE_Y-2)),
                           (SIZE_X-2, SIZE_Y-2))
        path = pathF.pathFinder()
        for obj in path:
            maze.maze[obj[0]][obj[1]].isPartOfPath = True
        self.path = path
        self.maze = maze

        objects = []
        self.player = Player('yellow', 'green', self.tile,
                             self.tile+608, 0, objects, self.tile, KL1)
        self.player1 = Player('blue', 'red', self.tile,
                              self.tile, 0, objects, self.tile, KL2)
        self.play_button = Button(self, "Play")
        self.restart_button = Button(self, "Restart game")
        self.end_button = Button(self, "End game", offset=(0, 65))

        self.game_active = False

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
        self.player.update(self.screen, keys, self.width,
                           self.height, self.tile, self.maze)
        self.player1.update(self.screen, keys, self.width,
                            self.height, self.tile, self.maze)

    def add_path(self, path):
        self.path = path

    def run_maze(self):
        clock = pygame.time.Clock()
        running = True
        show_button = True
        button_clicked = False
        restart_button_clicked = False
        end_game_button_clicked = False
        restart = False
        elapsed_time = 0  # Track elapsed time

        # Customize the font and size as desired
        timer_font = pygame.font.Font(None, 36)

        def format_time(milliseconds):
            seconds = milliseconds // 1000
            minutes = seconds // 60
            seconds %= 60
            return f"{minutes:02d}:{seconds:02d}"

        while running:
            self.screen.fill((0, 0, 0))
            self.draw_maze()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise EndGameException()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    button_clicked = self.play_button.rect.collidepoint(
                        mouse_pos)
                    restart_button_clicked = self.restart_button.rect.collidepoint(
                        mouse_pos)
                    end_game_button_clicked = self.end_button.rect.collidepoint(
                        mouse_pos)
            if not button_clicked and show_button:
                self.play_button.draw_button()
                self.end_button.draw_button()
            elif show_button:
                self.screen.fill((0, 0, 0))
                show_button = False
                self.play_button.kill()
            if button_clicked and not restart:
                restart_button_clicked = None
            if self.path and self.player.rect.x == (SIZE_X-2)*self.tile and self.player.rect.y == (SIZE_Y-2)*self.tile:
                self.restart_button.draw_button()
                self.end_button.draw_button()
                new_highscore = False
                try:
                    with open('highscore.txt', 'r') as f:
                        highscore = int(f.read())
                except:
                    highscore = elapsed_time + 1
                if elapsed_time < highscore:
                    new_highscore = True
                    with open('highscore.txt', 'w') as f:
                        f.write(str(elapsed_time))
                    highscore = elapsed_time
                if new_highscore:
                    highscore_text = timer_font.render(
                        f"NEW HIGHSCORE: {format_time(highscore)}.", True, TEXT_COLOR_WHITE)
                else:
                    highscore_text = timer_font.render(
                        f"Your HIGHSCORE: {format_time(highscore)}.", True, TEXT_COLOR_WHITE)
                self.screen.blit(highscore_text, (10, 10))

                restart = True
            if restart_button_clicked and restart:
                break

            if end_game_button_clicked != False:
                raise EndGameException()
            self.draw_player()
            if not restart:
                elapsed_time += clock.tick(self.fps)  # Update elapsed time
                # Customize the color as desired
                timer_text = timer_font.render(
                    format_time(elapsed_time), True, TEXT_COLOR_WHITE)
                # Adjust the position as desired
                self.screen.blit(timer_text, (10, 10))

            pygame.display.flip()
