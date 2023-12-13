import pygame
from shot import Shot
from settings import Settings


class Space_Ship(pygame.sprite.Sprite):
    def __init__(self):
        """ Initialize the Space_Ship object.

        The space_ship is represented as a sprite in the game.

        Attributes:
        - image (Surface): The image of the space_ship.
        - rect_spaceship (Rect): The rectangular area of the space_ship on the screen.
        - speed_x_spaceShip (int): The horizontal speed of the space_ship.
        """
        super().__init__()
        self.image = pygame.image.load('pictures/space_ship.bmp')
        self.rect_spaceship = self.image.get_rect(midbottom=(Settings.bottom_center, Settings.bottom_screen_border))
        self.speed_x_spaceShip = 0

    def move_right(self):
        """
        Move the space_ship to the right within the screen boundaries.

        If the space_ship reaches the right border of the screen, its position is capped.
        """
        self.rect_spaceship.x += Settings.space_ship_steps
        if self.rect_spaceship.x >= Settings.width_screen_border - self.image.get_width():
            self.rect_spaceship.x = Settings.width_screen_border - self.image.get_width()

    def move_left(self):
        """
        Move the space_ship to the left within the screen boundaries.

        If the space_ship reaches the left border of the screen, its position is capped.
        """
        self.rect_spaceship.x -= Settings.space_ship_steps
        if self.rect_spaceship.x <= Settings.screen_left_side:
            self.rect_spaceship.x = Settings.screen_left_side

    def space_ship_shot(self):
        """
        Create a shot from the space_ship.

        Returns:
        - Shot: A Shot object representing a projectile shot from the space_ship.
        """
        return Shot(self.rect_spaceship.midtop, -1, 'spaceship')
