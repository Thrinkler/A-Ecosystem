import pygame
import sys
import random
import os
from pathlib import Path

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
            creator.robot_species(random.randint(ROBOT_MIN_SPECIES_POP,ROBOT_MAX_SPECIES_POP))
        if time > 1000000:
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
        
        if(time % 100 == 1):
            camera_offset[2] = True
        elif not camera_offset[2]:
            camera_offset[2] = False
        snapshot = creator.draw(DISPLAYSURF, camera_offset)

        #if time%5000 == 0 and random.uniform(0, 1) > 0.5:
         #   creator.robot_species(random.randint(ROBOT_MIN_SPECIES_POP,ROBOT_MAX_SPECIES_POP))

        if len(snapshot) > 0:
            log_dir = Path("logs/snapshot" + creator.file.name.split("/")[-1].split(".")[0] + "/")
            log_dir.mkdir(exist_ok=True)

            try:
                snap = open(log_dir / ("snapshot.csv"), "a")
            except Exception as e:
                snap = open(log_dir / ("snapshot.csv"), "w")

            if snap.tell() == 0:
                snap.write("frame,velocity,rot_vel,vision,prob_fail_rot\n")
            for s in snapshot:
                snap.write(str(time)+","+",".join([str(x) for x in s]) + "\n")

            snap.close()

        DISPLAYSURF.blit(pygame.font.SysFont("Verdana", 20).render("Robots: " + str(len(creator.P)) + ", Food: " + str(len(creator.F)), True, WHITE), (10,10))
        FramePerSec.tick(FPS) 
        pygame.display.update()