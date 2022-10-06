from .obstable import Obstacle
import random
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS

class Cactus(Obstacle):
    CACTUS = {
            "LARGUE" : (LARGE_CACTUS, 300),
            "SMALL" : (SMALL_CACTUS, 300)
    }               
    def __init__(self, images):
        type = random.randint(0, 2)
        super().__init__(images, type)
        self.rect.y = 325


        
