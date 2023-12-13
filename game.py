import pygame
from manager import Manager
from settings import Settings

def game():
    """
    Main function to run the game.

    Initializes the game manager and runs the game loop, handling events, updating game state,
    and managing the display based on the game's current state.
    """
    clock = pygame.time.Clock()
    game1 = Manager()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        if game1.is_active:
            game1.run_game()
            game1.space_ship_direction()
            game1.all_aliens()
            game1.space_ship_shot_press()
            game1.all_shots()
            game1.aline_shot()
            game1.collisions()
            game1.our_king()
        elif game1.winner:
            game1.the_img()
        else:
            game1.game_over()
        pygame.display.update()
        clock.tick(Settings.clock_speed)


if __name__ == '__main__':
    game()
