import pygame

pygame.init()

# Load sounds
eat_sound = pygame.mixer.Sound("./sounds/collect.wav")
lose_sound = pygame.mixer.Sound("./sounds/lose.wav")
win_sound = pygame.mixer.Sound("./sounds/win.wav")

class SoundManager:
    @staticmethod
    def play_eat_sound():
        eat_sound.play()

    @staticmethod
    def play_lose_sound():
        lose_sound.play()

    @staticmethod
    def play_win_sound():
        win_sound.play()
