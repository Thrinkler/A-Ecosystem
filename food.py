import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y,color):
        self.rect = pygame.Rect(x,y,5,5)
        self.color = color
        self.time = 0
        self.child_time = 150+ random.randint(-100,100)
        self.death_time = 500 + random.randint(-450,500)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, width=0)
        self.time += 1

    def gen_new(self):
        return Food(self.rect.x + random.randint(-50,50),self.rect.y + random.randint(-50,50),self.color)
    
        