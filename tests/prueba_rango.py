
import pygame
import sys
from pygame.locals import QUIT

def square(surface,vision,grid_size,rectx,recty):
    center_cx = rectx // grid_size
    center_cy = recty // grid_size
    
    pygame.draw.rect(surface, pygame.Color(255,255,0), pygame.Rect(center_cx*grid_size,center_cy*grid_size,grid_size,grid_size), width=0)
    
    for i in range(1,vision//(2*grid_size)):
        for j in range(-i,i+1):
            y = i+(recty//grid_size)
            x = j+(rectx//grid_size)
            pygame.draw.rect(surface, pygame.Color(255,0,255), pygame.Rect(x*grid_size,y*grid_size,grid_size,grid_size), width=0)
            y = -i+(recty//grid_size)
            x = -j+(rectx//grid_size)
            pygame.draw.rect(surface, pygame.Color(255,0,255), pygame.Rect(x*grid_size,y*grid_size,grid_size,grid_size), width=0)
        
        for j in range(-i+1,i):
            y = j+(recty//grid_size)
            x = i+(rectx//grid_size)
            pygame.draw.rect(surface, pygame.Color(255,255,255), pygame.Rect(x*grid_size,y*grid_size,grid_size,grid_size), width=0)
            y = -j+(recty//grid_size)
            x = -i+(rectx//grid_size)
            pygame.draw.rect(surface, pygame.Color(255,255,255), pygame.Rect(x*grid_size,y*grid_size,grid_size,grid_size), width=0)

from pygame.locals import QUIT
	
pygame.init()

FPS = 90
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

f = 1
time = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)

    square(DISPLAYSURF,200,f,300,300 )
    if time %50 == 0:
        print(f,200)
        f+=1
    time+=1
    FramePerSec.tick(FPS) 
    pygame.display.update()