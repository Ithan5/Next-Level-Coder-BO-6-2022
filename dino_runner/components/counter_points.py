import pygame
import pygame.font 

#from pygame.sprite import Sprite

class Counter_points:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def update(self, points):
        self.points = points    

    def draw(self, screen):
        self.text = self.font.render("Points: " + str(self.points), True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        self.textRect.center = (1000, 40)
        screen.blit(self.text, self.textRect)