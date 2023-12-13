import pygame
from space_ship import Space_Ship
import random
from background import Background
from alien import Aline
from shot import Shot
from manager import Manager
# from sound import Sounds
pygame.init()

'''defined the screen'''

clock = pygame.time.Clock()
'''give all parts of the game running'''
is_active = True
'''save the class Background in a variable'''
background = Background('screen')
manager = Manager()

# sound = Sounds()
'''gives for the while running True'''
running = True
shots_space_ship = pygame.sprite.Group()
temp1 = pygame.sprite.Group()
temp = Space_Ship()
temp1.add(temp)
temp2 = Aline()
initial_aline_shot = pygame.image.load('pictures/pngtree-red-game-arrow-png-image_5979586-removebg-preview.png')
rotate_aline_shot = pygame.transform.rotate(initial_aline_shot, 270)
aline_shot = pygame.transform.scale(rotate_aline_shot, (45, 45))
aliens = pygame.sprite.Group()
space_ship_shot_timer = 0
shots_alien = pygame.sprite.Group()
'''locate the aliens and add it to a grope'''
for j in range(8):
    for i in range(3):
        x = 100 + j * 120
        y = 60 + i * 60
        aliens.add(Aline(position=(x, y)))

'''settings for movement and activity of the aliens and space_ship'''
aline_shot_timer = 0
aline_shot_delay = 60

life = 3

'''the main engine that activates the game'''
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    '''display the background images'''
    # screen.blit(background_image, (0, 0))
    background.games_background()
    background.display_bottom_line()
    # background.display_life()

    # sound.play_game_sound()
    '''defined the game keys'''
    manager.press()


    shots_space_ship.update()
    shots_space_ship.draw(screen)
    '''changes the direction of the aliens'''
    flip = False
    for alien in aliens.sprites():
        if alien.rect.x >= 1280 - alien.image.get_width() or alien.rect.x <= 0:
            flip = True
            break
    aline_shot_timer += 5

    '''game's actions'''
    if is_active:
        shots_alien.update()
        shots_alien.draw(screen)
        aliens.update(flip)
        aliens.draw(screen)
        temp1.draw(screen)
    '''shots from random aliens while they exist'''
    if aline_shot_timer >= aline_shot_delay:
        random_aline = random.choice(aliens.sprites())
        shots_alien.add(Shot(temp2, 0, aline_shot, random_aline.rect.center))
        aline_shot_timer = 0

    '''the result of an alien shot'''
    if life >= 0:
        if pygame.sprite.groupcollide(shots_alien, temp1, True, False):
            screen.fill('red')
            life -= 1

    '''the result of a space ship shot'''
    if pygame.sprite.groupcollide(shots_space_ship, aliens, True, True):
        screen.fill('blue')

    '''the result of a meeting between two shots'''
    if pygame.sprite.groupcollide(shots_space_ship, shots_alien, True, True):
        screen.fill("yellow")

    '''rate of space ship's fire'''
    if space_ship_shot_timer <= 19:
        space_ship_shot_timer += 1
    else:
        space_ship_shot_timer = 0

    '''the result of finish the game'''
    if life <= 0:
        background.display_game_over()
        temp1.empty()
        shots_space_ship.empty()

    pygame.display.flip()
    clock.tick(40)
pygame.quit()
