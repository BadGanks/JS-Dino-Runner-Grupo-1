
from .obstable import Obstacle

import random

class Cactus(Obstacle):
     
    
    def __init__(self, images, hight_catus):
        type = random.randint(0, 2)
        super().__init__(images, type)
        self.rect.y = hight_catus
        
    




        
