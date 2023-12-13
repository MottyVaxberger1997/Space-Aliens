import pygame
from settings import Settings


class Shot(pygame.sprite.Sprite):
    def __init__(self, location, direction, test_img):
        """
        Initialize a shot object.

        The Shot class represents a projectile shot by either the space_ship or an alien.

        Parameters:
        - location (tuple): The initial coordinates (x, y) of the shot.
        - direction (int): The direction of the shot (-1 for upward, 1 for downward).
        - test_img (str): A string indicating the source of the shot ('spaceship' or 'alien').
        """
        super().__init__()
        self.rect_x = location[0]
        self.rect_y = location[1]
        if test_img == 'spaceship':
            self.image = Settings.img_space_ship_shot
        if test_img == 'alien':
            self.image = Settings.img_alien_shot
        self.rect = self.image.get_rect(midbottom=(self.rect_x, self.rect_y))
        self.direction = direction

    def update(self):
        """
        Update the position of the shot.

        Move the shot vertically based on its direction and the specified speed.
        """
        self.rect.top += Settings.speed_shot * self.direction
