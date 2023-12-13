import pygame


class Sounds:
    def __init__(self):
        self.chanel_1 = pygame.mixer.Channel(1)
        self.chanel_1_music = pygame.mixer.Sound('sounds/game_sound.mp3')
        pygame.mixer.Channel.set_volume(self.chanel_1, 0.4)

        self.chanel_2 = pygame.mixer.Channel(2)
        self.chanel_2_music = pygame.mixer.Sound('/home/shloimy/Documents/python - project/Space Invaders '
                                                 'Game/sounds/hit-sound-effect.mp3')
        pygame.mixer.Channel.set_volume(self.chanel_2, 0.8)

        self.chanel_3 = pygame.mixer.Channel(3)
        self.chanel_3_music = pygame.mixer.Sound('/home/shloimy/Documents/python - project/Space Invaders '
                                                 'Game/sounds/5-4-3-2-1.wav')
        # pygame.mixer.Channel.set_volume(self.chanel_3, self.chanel_3_music)

    def play_game_sound(self):
        pygame.mixer.Channel.play(self.chanel_1, self.chanel_1_music, -1)

    def continue_play_game_sound(self):
        pygame.mixer.Channel.unpause(self.chanel_1)

    def stop_game_sound(self):
        pygame.mixer.Channel.pause(self.chanel_1)

    def play_collision_sound(self):
        pygame.mixer.Channel.play(self.chanel_2, self.chanel_2_music)

    def play_start_sound(self):
        pygame.mixer.Channel.play(self.chanel_3, self.chanel_3_music)

