from random import randint
from dino_runner.utils.constants import SCREEN_WIDTH

from pygame.sprite import Sprite

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.type = type
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + randint(800, 1000)
        self.rect.y = randint(125, 175)
        self.star_time = 0
        self.duration = randint(5, 7)

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
            