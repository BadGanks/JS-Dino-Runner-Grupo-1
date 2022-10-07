from asyncio import shield
import py_compile
from random import randint

import pygame
from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0
        

    

    """def update(self, game_speed, player, score):
        count_power_ups = randint (0, 2)
        if len(self.power_ups) == 0 and count_power_ups == 1:
            self.when_appears += randint(200, 300)
            self.power_ups.append(Shield())
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                self.power_ups.remove(power_up)
    """
    def generate_power_up(self, score):
        count_rand=randint(0,1000)
        if len(self.power_ups) == 0 and count_rand==0 :
            self.when_appears += randint(200, 300)
            self.power_ups.append(Shield())

    def update(self, game_speed, player, score):
        self.generate_power_up(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.star_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up.star_time, power_up.duration, power_up.type)
                self.power_ups.remove(power_up)
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset_power_ups(self):
        self.power_ups = []
        