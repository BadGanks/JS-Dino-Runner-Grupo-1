from random import randint
from dino_runner.components.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from .cactus import Cactus
import pygame
import random
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    def update(self, game):
        obstacle_random = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if obstacle_random == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            if obstacle_random == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            if obstacle_random == 2:
                self.obstacles.append(Bird(BIRD))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
