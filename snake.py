import pygame
pygame.init()
width=600
height=600
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (width, height) )
screen.fill( (0, 255, 0) ) # Fill screen with green
while True:
    for event in pygame.event.get():
        color = (0, 0, 255) # blue
        #rect = pygame.Rect(left, top, width, height)
        #pygame.draw.rect(screen, color, rect)
        pass # do nothing for the moment
    # Wait one second, starting from last display or now
    clock.tick(1)
pygame.quit()