import pygame
from settings import Settings


class Aline(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initialize the Alien group.

        The Alien group represents a collection of alien sprites.

        Attributes:
        - alien_grope (Group): Group containing individual alien sprites.
        - image (Surface): The image representing an individual alien sprite.
        - rect (Rect): The rectangular area of an alien sprite on the screen.
        - speed_y (int): The vertical speed of the aliens.
        """
        super().__init__()
        self.alien_grope = pygame.sprite.Group()
        self.image = Settings.img_alien
        self.rect = self.image.get_rect(midbottom=(Settings.start_position_aliens_x, Settings.start_position_aliens_y))
        self.speed_y = Settings.speed_y

    def aliens_grope(self):
        """
        Generate a group of aliens.

        Creates a grid of aliens based on specified settings and adds them to the alien group.
        """
        for j in range(Settings.length_alien_grope):
            for i in range(Settings.height_alien_grope):
                alien = Aline()
                alien.rect.x = Settings.part_of_positions_x_aliens + j * Settings.part_of_positions_x_aliens2
                alien.rect.y = Settings.positions_y_aliens + i * Settings.positions_y_aliens
                self.alien_grope.add(alien)

    def update(self, speed, speed_y):
        """
        Update the position of the alien group.

        Move the entire alien group horizontally based on the specified speed.
        If speed_y is True, move the alien group vertically.

        Parameters:
        - speed (int): The horizontal speed of the alien group.
        - speed_y (bool): Flag indicating whether the alien group should move vertically.
        """
        self.rect.x += speed
        if speed_y == 1:
            self.rect.y += self.speed_y
