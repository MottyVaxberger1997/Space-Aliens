import pygame
from alien import Aline
from space_ship import Space_Ship
from shot import Shot
from settings import Settings
import random


class Manager(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initialize the game manager.

        The manager controls the game state, including the player's space_ship, aliens, and shots.

        Attributes:
        - is_active (bool): Flag indicating whether the game is currently active.
        - space_ship (Space_Ship): The player's space_ship.
        - alien (Aline): The alien enemy.
        - shots_space_ship (Group): Group of shots fired by the space_ship.
        - shots_alien (Group): Group of shots fired by the aliens.
        - screen (Surface): The game screen.
        - space_ship_shot_timer (int): Timer for the space_ship shots.
        - aliens (Group): Group containing all aliens.
        - speed_alien (int): Speed of alien movement.
        - speed_alien_y (bool): Flag indicating whether aliens should move vertically.
        - test (int): Test variable.
        - space_ship_life (int): Number of lives for the space_ship.
        - winner (bool): Flag indicating whether the player has won.
        - loss (bool): Flag indicating whether the player has lost.
        """
        super().__init__()
        self.is_active = True
        self.space_ship = Space_Ship()
        self.alien = Aline()
        self.shots_space_ship = pygame.sprite.Group()
        self.shots_alien = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
        self.space_ship_shot_timer = Settings.space_ship_shot_timer
        self.aliens = pygame.sprite.Group()
        self.speed_alien = Settings.speed_alien
        self.speed_alien_y = False
        self.alien.aliens_grope()
        self.aliens_shots_speed = Settings.aliens_shots_speed
        self.test = Settings.test
        self.space_ship_life = Settings.space_ship_life
        self.winner = False
        self.loss = False

    def run_game(self):
        """
        Run the game loop and update the game state.

        Draws the game background, space_ship, and initializes the game state.
        """
        self.screen.blit(Settings.img_game_background,
                         (Settings.screen_start_point_x, Settings.screen_start_point_y))
        self.screen.blit(self.space_ship.image, self.space_ship.rect_spaceship)
        self.is_active = True

    def space_ship_direction(self):
        """
        Handle the direction of the space_ship based on user input.

        Moves the space_ship right or left based on user key presses.
        """
        all_key = pygame.key.get_pressed()
        if all_key[pygame.K_RIGHT]:
            self.space_ship.move_right()
        if all_key[pygame.K_LEFT]:
            self.space_ship.move_left()

    def aliens_direction(self):
        """
        Handle the direction of the aliens.

        Checks if the aliens have reached the screen boundaries and adjusts their movement accordingly.
        """
        for alien in self.alien.alien_grope:
            if Settings.screen_left_side >= alien.rect.left or alien.rect.right >= Settings.SCREEN_WIDTH:
                self.speed_alien_y = True
                self.speed_alien *= -1
                break
            else:
                self.speed_alien_y = False

    def all_aliens(self):
        """
        Update and draw all aliens on the screen.

        Calls the necessary methods to update and draw the alien group.
        """
        self.aliens_direction()
        self.alien.alien_grope.draw(self.screen)
        self.alien.alien_grope.update(self.speed_alien, self.speed_alien_y)

    def space_ship_shot_press(self):
        """
        Handle space_ship shot events.

        Detects space bar press events and adds space_ship shots to the group.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shots_space_ship.add(self.space_ship.space_ship_shot())

    def all_shots(self):
        """
        Update and draw all shots on the screen.

        Draws both space_ship and alien shots on the screen and updates their positions.
        """
        self.shots_space_ship.draw(self.screen)
        self.shots_alien.draw(self.screen)
        self.shots_space_ship.update()
        self.shots_alien.update()

    def aline_shot(self):
        """
        Handle alien shot events.

        Randomly selects an alien and adds a shot to the alien shots group based on a timer.
        """
        alien_list = list(self.alien.alien_grope)
        if alien_list:
            one_alien = random.choice(alien_list)
            shot = Shot(one_alien.rect.midbottom, 1, 'alien')
            if self.test == 0:
                self.shots_alien.add(shot)
                self.test = (self.test + 1) % self.aliens_shots_speed
            else:
                self.test = (self.test + 1) % self.aliens_shots_speed

    def collisions(self):
        """
        Handle collisions between game objects.

        Checks for collisions between space_ship and alien shots, space_ship and aliens,
         and space_ship shots and aliens.
        """
        if self.space_ship_life > 0:
            for shot in self.shots_alien:
                if self.space_ship.rect_spaceship.colliderect(shot):
                    self.screen.fill('red')
                    shot.kill()
                    self.space_ship_life -= 1
        else:
            self.is_active = False
        if pygame.sprite.groupcollide(self.shots_space_ship, self.alien.alien_grope, True, True):
            self.screen.fill('blue')
        if pygame.sprite.groupcollide(self.shots_space_ship, self.shots_alien, True, True):
            self.screen.fill("yellow")
        for alien in self.alien.alien_grope:
            if self.space_ship.rect_spaceship.colliderect(alien):
                self.is_active = False

    def our_king(self):
        """
        Check for victory conditions.

        Check if all aliens are eliminated, and set the game state accordingly.
        """
        if len(self.alien.alien_grope) == 0:
            self.is_active = False
            self.winner = True

    def the_img(self):
        """
        Draw the winner image on the screen.
        """
        self.screen.blit(Settings.img_winner, (Settings.screen_start_point_x, Settings.screen_start_point_y))

    def game_over(self):
        """
        Draw the game over image on the screen.
        """
        self.screen.blit(Settings.img_game_over, (Settings.screen_start_point_x, Settings.screen_start_point_y))
