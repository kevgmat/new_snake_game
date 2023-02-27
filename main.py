import pygame
import sys
pygame.init()
display = pygame.display.set_mode((620, 720))
background = pygame.Surface((620, 720))
background.fill((0, 0, 0))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.lines(display, pygame.Color((255,0,0)), True,  [(300,400),(400,300),(200,300)], width = 1)
    pygame.display.update()
pygame.quit()
sys.exit()