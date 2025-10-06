import pygame
import sys
import random
import os

import robot
import food
import robot_creator

from pygame.locals import *
	
pygame.init()

FPS = 9000
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Game")
 
pygame.Rect((20, 50), (50, 100))


def start():
    time = 0
    creator = robot_creator.Creator(10,100)
    creator.P.append(robot.Robot(999,500,400,creator.F,velocity=10,rot_vel=10,vision=200,life=1000,prob_fail_rot=0))
    while True:
        if time == 15000:
            os.rename(creator.file.name, "logs/sp_" + creator.file.name.split("/")[-1])
        if len(creator.P)== 1:
            
            creator.file.close()
            creator = robot_creator.Creator(random.randint(1,250),random.randint(1,500))
        for event in pygame.event.get():
            if event.type == QUIT:
                creator.file.close()
                pygame.quit()
                sys.exit()
        DISPLAYSURF.fill(BLACK)
        time += 1
        creator.draw(DISPLAYSURF)
        FramePerSec.tick(FPS) 
        pygame.display.update()