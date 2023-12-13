import pygame
from settings import Settings

class Background:
    def __init__(self, screen, lives=3):
        self.life_update = pygame.font.Font(None, 100)
        self.screen = screen
        self.go_text = pygame.font.Font(None, 200)
        self.go_text_surf = self.go_text.render('Game Over ', False, 'Red')
        self.marble_image = pygame.image.load('pictures/bottom background.jpg')
        self.lives_update = self.life_update.render('life:{}'.format(lives), True, 'white')
        self.background_game = pygame.image.load('pictures/game background.jpg')
        self.background_game1 = pygame.transform.scale(self.background_game, (1280, 720))

    def games_background(self):
        self.screen.blit(self.background_game1, (0, 0))

    def display_game_over(self):
        # self.screen.fill('blue')
        self.screen.blit(self.go_text_surf, (250, 250))

    def display_bottom_line(self):
        self.screen.blit(self.marble_image, (0, 660))

    def display_green_line(self):
        pygame.draw.line(settings.screen, "green", [0, 660], [1280, 660], 6)

    # def display_life(self):
    #     self.screen.blit(self.life_update, (20, 690))

