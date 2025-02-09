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

CELL_SIZE = 40
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Maze:
    def __init__(self):
        self.grid = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,0,1,0,1,0,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
            [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
            [1,1,1,1,0,1,0,1,0,1,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]

    def draw(self, screen):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE + 50, CELL_SIZE, CELL_SIZE))
                elif self.grid[y][x] == 0:
                    pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2 + 50), 3)

from settings import GameSettings
from characters import PacMan, Ghost
from maze import Maze
from game_state import ScoreManager, GameState
from sounds import SoundManager

pygame.init()

class Game:
    def __init__(self):
        self.settings = GameSettings()
        self.pacman = PacMan()
        self.ghosts = [Ghost(1, 13, (255, 0, 0))]
        self.maze = Maze()
        self.score_manager = ScoreManager()
        self.game_state = GameState.PLAYING
