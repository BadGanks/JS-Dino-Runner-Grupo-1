
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD
from .cactus import Cactus
import pygame
import random


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    def update(self, game_speed, player, on_death):
        obstacle_random = random.randint(0, 2)
        big_cactus_y = 300
        small_cactus_y = 325
        if len(self.obstacles) == 0:
            if obstacle_random == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS,big_cactus_y))

            elif obstacle_random == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS,small_cactus_y))
            else :
                obstacle_random == 2
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):
                
                if on_death() :
                    self.obstacles.remove(obstacle)
                else:
                    break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []