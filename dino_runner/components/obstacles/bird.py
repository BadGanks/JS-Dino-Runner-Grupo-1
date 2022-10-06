from dino_runner.components.obstacles.obstable import Obstacle
import random

class Bird(Obstacle):
    BIRD_ELEVATION = [200, 290, 330]
    
    def __init__(self, image):  
        type = 0
        super().__init__(image, type)
        self.rect.y = random.choice(self.BIRD_ELEVATION)
        self.index = 0
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)        
        self.index += 1

