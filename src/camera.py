import pygame
x = 0
y = 0
snapshot = False
keypressed = False
def camera():
    global x, y, snapshot, keypressed
    keys = pygame.key.get_pressed()
    snapshot = False
    
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    if keys[pygame.K_r]:
        x = 0
        y = 0
    if keys[pygame.K_s] and not snapshot and not keypressed:
        snapshot = True
        keypressed = True
    if not keys[pygame.K_s]:   
        keypressed = False

    return [x, y, snapshot]
