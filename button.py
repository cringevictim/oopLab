import pygame.font


class Button(pygame.sprite.Sprite):

    def __init__(self, maze_game, msg, offset=(0, 0)):
        super().__init__()
        self.screen = maze_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(offset[0], offset[1], self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx + offset[0]
        self.rect.centery = self.screen_rect.centery + offset[1]

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Convert the text to an image and place it in a color of a button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.centerx = self.rect.centerx
        self.msg_image_rect.centery = self.rect.centery

    def draw_button(self, offset_x=0, offset_y=0):
        self.rect.x += offset_x
        self.rect.y += offset_y
        self.msg_image_rect.x += offset_x
        self.msg_image_rect.y += offset_y

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
