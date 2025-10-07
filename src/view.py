import pygame
import sys
import random
import os

from . import camera

from . import robot
from . import food
from . import robot_creator

from pygame.locals import QUIT
from .settings import *


pygame.init()

FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("A-Ecosystem")
 


def start():
    time = 0
    creator = robot_creator.Creator(10,100)
    while True:
        
        if time == SPECIAL_MIN and SPECIAL_NAME == True:
            os.rename(creator.file.name, "logs/sp_" + creator.file.name.split("/")[-1])
        if len(creator.P)== 1:
            time = 0
            creator.file.close()
            creator = robot_creator.Creator(random.randint(1,250),random.randint(1,500))
        for event in pygame.event.get():
            if event.type == QUIT:
                creator.file.close()
                pygame.quit()
                sys.exit()
        DISPLAYSURF.fill(BLACK)
        time += 1
        camera_offset = camera.camera()
        creator.draw(DISPLAYSURF, camera_offset)
        DISPLAYSURF.blit(pygame.font.SysFont("Verdana", 20).render("Robots: " + str(len(creator.P)) + ", Food: " + str(len(creator.F)), True, WHITE), (10,10))
        FramePerSec.tick(FPS) 
        pygame.display.update()