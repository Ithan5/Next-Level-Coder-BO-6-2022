from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

import random

class Bird(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 1)
        self.step_index = 0
        super().__init__(image, self.type)
        self.rect.y = 260