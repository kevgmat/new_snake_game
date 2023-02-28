import pygame
import sys
import random
pygame.init()
display = pygame.display.set_mode((620, 720))
background = pygame.Surface((620, 720))
background.fill((0, 0, 0))
food_pos = []

game_over = [False]
def enter_game():

    snake_block = 20
    snake_speed = 20
    x=0
    y= 0

    i = 1
    percentage = 10
    while i <= int((percentage / 100) * 961):
        food_x = random.randint(1, 31)
        food_y = random.randint(1, 31)
        if (food_x, food_y) in food_pos:
            pass
        else:
            food_pos.append((food_x, food_y))
            i += 1
    def snake(snake_block_function, snake_list_function):
        for site in snake_list_function:
            pygame.draw.rect(display, pygame.Color((255,255,255)),
                             [site[0],site[1], snake_block_function, snake_block_function],
                             width = 3)

    def background():
        pygame.draw.rect(display, pygame.Color((0, 0, 0)), [0, 0, 620, 720])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(1, 32):
            pygame.draw.line(display, pygame.Color((255, 0, 0)), (0,(i*20)),(620,(i*20)), width = 1)
            pygame.draw.line(display, pygame.Color((255, 0, 0)), ((i*20),0),((i*20),620), width = 1)

            pygame.draw.line(display, pygame.Color((0, 255, 0)), (0, ((i+31) * 20)), (620, ((i+31) * 20)), width=1)
            pygame.draw.line(display, pygame.Color((0, 255, 0)), ((i*20),620),((i*20),720), width = 1)

    def food_display():
        for i in food_pos:
            pygame.draw.rect(display, pygame.Color((0, 0, 255)), [((i[0] - 1) * 20), ((i[1] - 1) * 20), 20, 20])

    def game():

        game_over[0] = False
        snake_list = []
        length_of_snake = 10

        x = 0
        y = 0

        while not game_over[0]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over[0]= True

            x+=10
            pygame.time.delay(50)
            # y+=10
            snake_head = [x,y]
            snake_list.append(snake_head)
            if len(snake_list)> length_of_snake:
                del snake_list[0]

            background()
            food_display()
            snake(snake_block, snake_list)

            pygame.display.update()

    game()
enter_game()
pygame.quit()
sys.exit()