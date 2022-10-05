from dino_runner.components.obstable import Obstacle
import random

class Bird(Obstacle):
    BIRD_ELEVATION = [200, 290, 320]
    
    def __init__(self, image):  
        type = 0
        super().__init__(image, type)
        self.rect.y = random.choice(self.BIRD_ELEVATION)
        
    

