import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(640, 560)
shot_space_ship_pos = pygame.Vector2(660, 500)
pos = pygame.Vector2(100, 100)
ali_pos = pygame.Vector2(200, 200)
# b = a.get_rect(self=(80, 300))


class MovementAndExistence:
    def __init__(self, move, position, velocity):
        self.movement = move
        self.position = position
        self.velocity = velocity


class Alien(MovementAndExistence):
    def __init__(self):
        super().__init__()


class Shots:
    def __init__(self, shooter, location, space_ship_pos):
        self.image = pygame.image.load('pictures/pngwing.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=space_ship_pos)
        self.type = shooter
        self.shot_loc = location

    def space_ship_shot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.image.y -= 6

    def aline_shot(self):
        pass

    def move(self):
        pass


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    pygame.draw.line(screen, "green", [0, 660], [1280, 660], 6)
    a = pygame.image.load('pictures/ship.bmp').convert_alpha()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
        if player_pos.x <= 0: player_pos.x = 0
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
        if player_pos.x >= screen.get_width() - a.get_width(): player_pos.x = screen.get_width() - a.get_width()
    shot = pygame.image.load('pictures/pngwing.png').convert_alpha()

    b = pygame.transform.scale(shot, (20, 20))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        shot_space_ship_pos.y -= 6
    if shot_space_ship_pos.y <= 0 - b.get_height():
        shot_space_ship_pos.y = 500
    c = pygame.image.load('pictures/pngtree-red-game-arrow-png-image_5979586-removebg-preview.png').convert_alpha()
    c = pygame.transform.rotate(c, 270)
    c = pygame.transform.scale(c, (45, 45))
    d = pygame.image.load('pictures/alien.bmp').convert_alpha()
    screen.blit(d, ali_pos)
    screen.blit(c, pos)
    screen.blit(b, shot_space_ship_pos)
    screen.blit(a, player_pos)
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    # screen.blit(a)
pygame.quit()
