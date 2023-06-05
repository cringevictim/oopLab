import pygame.font

class MazeButton(pygame.sprite.Sprite):
    def __init__(self, maze_game, msg, width, height, pos_x, pos_y):
        super().__init__()
        self.screen = maze_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = width, height
        self.pos_x, self.pos_y = pos_x, pos_y
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 24)


        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert the text to an image and place it in a color of a button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class WinLossButton(pygame.sprite.Sprite):
    def __init__(self, maze_game, msg, width, height, pos_x, pos_y, color):
        super().__init__()
        self.screen = maze_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = width, height
        self.pos_x, self.pos_y = pos_x, pos_y
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)


        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert the text to an image and place it in a color of a button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class StartButton(pygame.sprite.Sprite):

    def __init__(self, maze_game, msg):
        super().__init__()
        self.screen = maze_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert the text to an image and place it in a color of a button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
