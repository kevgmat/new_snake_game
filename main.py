import pygame
import sys
import random
pygame.init()
display = pygame.display.set_mode((620, 720))
background = pygame.Surface((620, 720))
background.fill((0, 0, 0))
food_pos = []

i = 1
percentage = 50
while i<= int((percentage/100)*961):
    x = random.randint(1,31)
    y = random.randint(1,31)
    if (x,y) in food_pos:
        pass
    else:
        food_pos.append((x,y))
        pygame.draw.rect(display, pygame.Color((0, 0, 255)), [((x - 1) * 20), ((y - 1) * 20), 20, 20])
        i+=1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range(1, 32):
        pygame.draw.line(display, pygame.Color((255, 0, 0)), (0,(i*20)),(620,(i*20)), width = 1)
        pygame.draw.line(display, pygame.Color((255, 0, 0)), ((i*20),0),((i*20),620), width = 1)

        pygame.draw.line(display, pygame.Color((0, 255, 0)), (0, ((i+31) * 20)), (620, ((i+31) * 20)), width=1)
        pygame.draw.line(display, pygame.Color((0, 255, 0)), ((i*20),620),((i*20),720), width = 1)

    pygame.display.update()
pygame.quit()
sys.exit()