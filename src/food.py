import pygame
import random
from .settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y,color):
        self.rect = pygame.Rect(x,y,FOOD_SIZE,FOOD_SIZE)
        self.color = color
        self.time = 0
        self.child_time = FOOD_CHILD_TIME + random.randint(-100,100)
        self.death_time = FOOD_DEATH_TIME + random.randint(-450,500)
        self.can_reproduce = random.uniform(0, 1) > FOOD_CHILD_RATE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, width=0)
        self.time += 1

    def gen_new(self):
        return Food(self.rect.x + random.randint(-50,50),self.rect.y + random.randint(-50,50),self.color)
    
        