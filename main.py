import pygame
import sys
import random
from threading import *
import time

pygame.init()
display = pygame.display.set_mode((620, 720))
background = pygame.Surface((620, 720))
background.fill((0, 0, 0))
food_pos = []

game_over = [False]

start_time = [0]
end_time = []


turn_locations = []

icon_size = 50
def turn_locations_finder():
    i = 1
    turn_locations.clear()
    turn_location_right = random.randint(1, 30)
    turn_location_left = 0
    turn_locations.append(turn_location_right)

    while i <= 15:
        turn_location_left = random.randint(0, turn_location_right)
        turn_locations.append(turn_location_left)
        turn_location_right = random.randint(turn_location_left, 30)
        turn_locations.append(turn_location_right)
        i += 1


def intro_page():
    display = pygame.display.set_mode((620,720))

    about = pygame.image.load("icons/about.png")
    about_dark = pygame.image.load("icons/about_dark.png")
    next = pygame.image.load("icons/next.png")
    next_dark = pygame.image.load("icons/next_dark.png")

    about = pygame.transform.scale(about, (icon_size, icon_size))
    about_dark = pygame.transform.scale(about_dark, (icon_size, icon_size))
    next = pygame.transform.scale(next, (icon_size, icon_size))
    next_dark = pygame.transform.scale(next_dark, (icon_size, icon_size))

    font = pygame.font.SysFont('Corbel', 32)

    pygame.display.update()
    background = pygame.Surface((620, 720))
    background.fill((255, 255, 255))

    image = pygame.image.load("wallpaper/sky_test.jpg")
    image = pygame.transform.scale(image, (620, 720))
    image = image.convert()

    rect = image.get_rect()

    # display.fill(0,0,0)


    offset = 200
    done = False

    display.blit(image,rect)
    pygame.display.update()
    # time.sleep(2000)


    while not done:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            # if event.type == pygame.MOUSEBUTTONDOWN and a != 1:
            # if event.type == pygame.KEYDOWN:
            #     display.blit()
            about_x = 620/2 - (1/2)*offset - icon_size/2
            next_x = 620/2 + (1/2)*offset - icon_size/2
            if about_x <= mousepos[0] <= about_x + 50 and 600 <= mousepos[1] <= 650:
                display.blit(about, (about_x, 600))
                pygame.display.update()
                print("about")
            else:
                display.blit(about_dark, (about_x, 600))
                pygame.display.update()

            if next_x <= mousepos[0] <= next_x + 50 and 600 <= mousepos[1] <= 650:
                display.blit(next, (next_x, 600))
                pygame.display.update()
                print("next")
            else:
                display.blit(next_dark, (next_x, 600))
                pygame.display.update()
    pygame.display.update()

intro_page()

def enter_game():

    start_time[0] = time.time()

    snake_block = 20
    snake_speed = 10
    bullet_state =[False]

    i = 1
    percentage = 10
    while i <= int((percentage / 100) * 961):
        food_x = random.randint(0, 30)*20
        food_y = random.randint(0, 30)*20

        if (food_x, food_y) in food_pos:
            pass
        else:
            food_pos.append([food_x, food_y])
            i += 1


    turn_locations_finder()
    print(turn_locations)

    def snake(snake_block_function, snake_list_function):
        for site in snake_list_function:
            pygame.draw.rect(display, pygame.Color((255, 255, 255)),
                             [site[0], site[1], snake_block_function, snake_block_function],
                             width=3)

    def background():
        # pygame.draw.rect(display, pygame.Color((0, 0, 0)), [0, 0, 620, 720])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for i in range(1, 32):
            pass
            # pygame.draw.line(display, pygame.Color((255, 0, 0)), (0, (i * 20)), (620, (i * 20)), width=1)
            # pygame.draw.line(display, pygame.Color((255, 0, 0)), ((i * 20), 0), ((i * 20), 620), width=1)
            #
            # pygame.draw.line(display, pygame.Color((0, 255, 0)), (0, ((i + 31) * 20)), (620, ((i + 31) * 20)), width=1)
            # pygame.draw.line(display, pygame.Color((0, 255, 0)), ((i * 20), 620), ((i * 20), 720), width=1)

    def food_display():
        for food_item in food_pos:
            pygame.draw.rect(display, pygame.Color((0, 0, 255)), [((food_item[0])), ((food_item[1])), 20, 20])

    def carriage_drawing(carriage_pos):
        pygame.draw.rect(display, pygame.Color((255, 0, 0)), ((carriage_pos*20-20), 660, 60, 20))
        pygame.draw.rect(display, pygame.Color((255, 0, 0)), ((carriage_pos*20), 640, 20, 20))

    def game():

        game_over[0] = False
        snake_list = []
        length_of_snake = [10]
        turning_right = [True]

        x = [-20]
        y = [0]
        carriage_x = [15]

        def carriage(snake_block):
            while True:
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    carriage_x[0] = carriage_x[0] - 1
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    carriage_x[0] = carriage_x[0] + 1
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    pass
                    bullet_state[0] = True
                else:
                    bullet_state[0] = False

                pygame.time.Clock().tick(50)

                pygame.draw.rect(display, pygame.Color((0, 0, 0)), [0, 0, 620, 720])

                for i in range(1, 32):
                    pygame.draw.line(display, pygame.Color((255, 0, 0)), (0, (i * 20)), (620, (i * 20)), width=1)
                    pygame.draw.line(display, pygame.Color((255, 0, 0)), ((i * 20), 0), ((i * 20), 620), width=1)

                    pygame.draw.line(display, pygame.Color((0, 255, 0)), (0, ((i + 31) * 20)), (620, ((i + 31) * 20)),
                                     width=1)
                    pygame.draw.line(display, pygame.Color((0, 255, 0)), ((i * 20), 620), ((i * 20), 720), width=1)

                for food_item in food_pos:
                    pygame.draw.rect(display, pygame.Color((0, 0, 255)),
                                     [((food_item[0])), ((food_item[1])), 20, 20])
                if carriage_x[0] >30:
                    carriage_x[0] -= 30
                elif carriage_x[0] <0:
                    carriage_x[0] += 30

                carriage_drawing(carriage_x[0])

                snake(snake_block, snake_list)
                # pygame.display.update()
        T = Thread(target=carriage, args = (snake_block, ), daemon= True)
        T.start()

        def bullet():

            bullet_y = 32
            i = 1

            while True:

                if bullet_state[0] == True:
                    pygame.draw.rect(display, pygame.Color((255, 0, 0)), [(carriage_x[0] * 20),
                                                                          (bullet_y * 20), 20, 20])
                    pygame.display.update()
                    bullet_y -= 1
                    pygame.time.Clock().tick(500)
                    if bullet_y < 0:
                        bullet_y = 32

                    for i in snake_list:

                        bullet_spot = [carriage_x[0]*20, bullet_y*20]

                        if bullet_spot in food_pos:
                            print("hit food")
                            bullet_y = 32

                        if carriage_x[0]*20 == i[0] and bullet_y*20 == i[1]:
                            if snake_list.index(i) == (len(snake_list)-1) :

                                print("hit", i[0], i[1])
                                bullet_y = 32
                                removed_part = snake_list[:(snake_list.index(i) + 1)]
                                del snake_list[:(snake_list.index(i) + 1)]
                                length_of_snake[0] = len(snake_list)
                                for i in removed_part:
                                    food_pos.append(i)

                                turn_locations_finder()
                                print(turn_locations)

                                x[0] = -20
                                y[0] = 0
                                length_of_snake[0] = 1
                                bullet_state[0] = False

                            else:
                                print("hit", i[0], i[1])
                                bullet_y = 32
                                removed_part = snake_list[:(snake_list.index(i)+1)]
                                del snake_list[:(snake_list.index(i) + 1)]
                                length_of_snake[0] = len(snake_list)
                                # print(removed_part)
                                for i in removed_part:
                                    food_pos.append(i)


                else:
                    pygame.display.update()

        T_2 = Thread(target=bullet, daemon= True)
        T_2.start()


        while not game_over[0]:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over[0] = True
            while y[0] < 600:

                for i in range(0, 31):

                    flag = [False, False]

                    if i%2 == 0:
                        turning_right[0] = True
                    else:
                        turning_right[0] = False

                    if i == 30:
                        end_time.append(time.time())

                        elapsed = end_time[len(end_time)-1]-start_time[0]
                        print(elapsed)


                    def motion(turning_right):

                        pygame.time.Clock().tick(snake_speed)

                        if x[0] == turn_locations[i] * 20:
                            y[0] += 20
                            flag[0] = True
                            length_of_snake[0] += 1
                        else:
                            if turning_right:
                                x[0] += 20
                            else:
                                x[0] -=20
                        if y[0] > 600:
                            return 0
                        snake_head = [x[0], y[0]]
                        snake_list.append(snake_head)
                        if len(snake_list) > length_of_snake[0]:
                            del snake_list[0]

                        background()
                        food_display()
                        # print(snake_list)
                        for j in food_pos:
                            if (x[0] == (j[0])) and (y[0] == (j[1])):
                                length_of_snake[0] += 1
                                food_pos.remove(j)

                        if flag[0]:
                            return 0


                    if i % 2 == 0:
                        while x[0] <= (turn_locations[i] * 20):
                            ref = motion(True)
                            if ref == 0:
                                break
                    else:
                        while x[0] >= (turn_locations[i] * 20):
                            ref = motion(False)
                            if ref == 0:
                                break
    game()


enter_game()
pygame.quit()
sys.exit()
