import pygame

from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.components.obstacles.cactus import Cactus

from dino_runner.utils.constants import LARGE_CACTUS

from dino_runner.components.obstacles.large_cactus import Large_cactus

from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.bird import Bird

from dino_runner.utils.constants import GAMEOVER, RESET


import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
 
    def update(self, game_speed, game):
        if len(self.obstacles) == 0:
            self.a = random.randint(0, 2)
            if self.a == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))

            elif self.a == 1:
                self.obstacles.append(Large_cactus(LARGE_CACTUS))

            elif self.a == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(300)
                    game.playing = False
                    break
                else:
                    self.obstacles.pop()

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


def Menu():
    gameover_img = GAMEOVER
    reset_img = RESET
    rect_game_over = gameover_img.get_rect()
    rext_x = 550
    pass

