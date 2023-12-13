import pygame

"""
A class to store all settings for the game.

Attributes:
- img_game_background (Surface): The background image of the game.
- img_alien (Surface): The image representing an alien.
- img_alien_shot (Surface): The image representing a shot fired by an alien.
- img_space_ship_shot (Surface): The image representing a shot fired by the space ship.
- img_game_over (Surface): The image displayed when the game is over.
- img_winner (Surface): The image displayed when the player wins.
- clock (Clock): Pygame clock used for controlling the frame rate.
- SCREEN_WIDTH (int): The width of the game screen.
- SCREEN_HEIGHT (int): The height of the game screen.
- test (int): A test variable.
- aliens_shots_speed (int): The speed of shots fired by aliens.
- space_ship_life (int): The initial number of lives for the space ship.
- space_ship_shot_timer (int): The timer for the space ship shots.
- speed_alien (int): The speed of alien movement.
- screen_start_point_x (int): The starting x-coordinate of the game screen.
- screen_start_point_y (int): The starting y-coordinate of the game screen.
- screen_left_side (int): The left side boundary of the game screen.
- bottom_center (int): The x-coordinate of the bottom center of the screen.
- bottom_screen_border (int): The y-coordinate of the bottom border of the screen.
- width_screen_border (int): The right side boundary of the game screen.
- space_ship_steps (int): The step size for moving the space ship.
- start_position_aliens_x (int): The starting x-coordinate for the alien group.
- start_position_aliens_y (int): The starting y-coordinate for the alien group.
- length_alien_group (int): The number of aliens in a row.
- height_alien_group (int): The number of rows of aliens.
- speed_y (int): The vertical speed of aliens.
- part_of_positions_x_aliens (int): A factor used for positioning aliens.
- part_of_positions_x_aliens2 (int): Another factor used for positioning aliens.
- positions_y_aliens (int): The initial y-coordinate for positioning aliens.
- speed_shot (int): The speed of shots fired by the space ship.
- clock_speed (int): The speed at which the game clock runs.
"""


class Settings:
    img_game_background = pygame.image.load('pictures/game-background.png')
    img_game_background = pygame.transform.scale(img_game_background, (1280, 720))
    img_alien = pygame.image.load('pictures/alien.png')
    img_alien_shot = pygame.image.load('pictures/alien_shot.png')
    img_alien_shot = pygame.transform.rotate(img_alien_shot, 270)
    img_alien_shot = pygame.transform.scale(img_alien_shot, (45, 45))
    img_space_ship_shot = pygame.image.load('pictures/space_ship shot.png')
    img_space_ship_shot = pygame.transform.scale(img_space_ship_shot, (20, 20))
    img_game_over = pygame.image.load('pictures/game_over.png')
    img_game_over = pygame.transform.scale(img_game_over, (1280, 720))
    img_winner = pygame.image.load('pictures/Winner.png')
    img_winner = pygame.transform.scale(img_winner, (1280, 720))
    clock = pygame.time.Clock()
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    test = 0
    aliens_shots_speed = 40
    space_ship_life = 3
    space_ship_shot_timer = 9
    speed_alien = 5
    screen_start_point_x = 0
    screen_start_point_y = 0
    screen_left_side = -1
    bottom_center = 640
    bottom_screen_border = 720
    width_screen_border = 1280
    space_ship_steps = 6
    start_position_aliens_x = 80
    start_position_aliens_y = 160
    length_alien_grope = 8
    height_alien_grope = 3
    speed_y = 25
    part_of_positions_x_aliens = 100
    part_of_positions_x_aliens2 = 120
    positions_y_aliens = 60
    speed_shot = 10
    clock_speed = 60
