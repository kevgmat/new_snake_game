import pygame
import sys
import random
from threading import *
import time

pygame.init()
display = pygame.display.set_mode((620, 720))
background = pygame.Surface((620, 720))
background.fill((0, 0, 0))
pygame.display.set_caption("SNAKE_GAME")
icon = pygame.image.load("icons/logo.png")
pygame.display.set_icon(icon)

food_pos = []

game_over = [False]

start_time = [0]
end_time = []


turn_locations = []

icon_size = 50

colors = {0: (0, 0, 0), 1: (255, 0, 0), 2: (255, 255, 255), 3: (255, 255, 0),
          4: (0, 255, 0), 5: (0, 0, 255), 6: (255, 128, 0), 7: (153, 0, 153)}
# 0 = black
# 1 = red
# 2 = white
# 3 = yellow
# 4 = green                                                                                                             #
# 5 = blue
# 6 = purple

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

# print(colors[2])

def message(msg, color, width_location, height_location, size, offset):
    mesg = pygame.font.SysFont("aquakana", size).render(msg, True, color)
    # print(width_location)
    # print(size)
    # print(offset)
    if offset == True:
        width_location = width_location - (len(msg)/2)
        # width_location = width_location - (len(msg)/2)*(size/3)
        # print(len(msg))
        # print(width_location)
        # pygame.display.update()
    else:
        pass
    display.blit(mesg, (width_location, height_location))
    pygame.display.update()
def about_func():
    sub_button_intro = ("songs/sub_button.mp3")


    clean = pygame.image.load("wallpaper/wallpaper_clean.jpg")
    clean = pygame.transform.scale(clean, (620, 720))
    clean = clean.convert()

    display.blit(clean,(0,0))
    pygame.display.update()

    back = pygame.image.load("icons/back.png")
    back_dark = pygame.image.load("icons/back_dark.png")
    copyright = pygame.image.load("icons/copyright.png")

    back = pygame.transform.scale(back, (50,50))
    back_dark = pygame.transform.scale(back_dark, (50, 50))
    copyright = pygame.transform.scale(copyright, (15,15))

    message("Created by Kevin for Crux Round 3 inductions", colors[2], 310, 280, 25, True)
    message("Basilisk 2.0. All Rights Reserved", colors[2], 310, 310, 17, True)
    display.blit(copyright,(195,305))

    pygame.display.update()

    done = False
    while not done:
        for event in pygame.event.get():
            mousepos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
            back_x = 620/2 - (1/2)*200 - icon_size/2
            if back_x <= mousepos[0] <= back_x + 50 and 600 <= mousepos[1] <= 650:
                display.blit(back,(back_x, 600))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    done = True
                    sub_button_intro_sound = pygame.mixer.Sound(sub_button_intro)
                    pygame.mixer.Channel(3).set_volume(1)
                    pygame.mixer.Channel(3).play(sub_button_intro_sound)
                    display.blit(clean, (0,0))
                    # print("back")
            else:
                display.blit(back_dark, (back_x, 600))
            pygame.display.update()


def next_func():


    clean = pygame.image.load("wallpaper/wallpaper_clean.jpg")
    clean = pygame.transform.scale(clean, ( 620, 720))
    clean = clean.convert()

    display.blit(clean, (0,0))
    pygame.display.update()

    back = pygame.image.load("icons/back.png")
    back_dark = pygame.image.load("icons/back_dark.png")
    copyright = pygame.image.load("icons/copyright.png")

    back = pygame.transform.scale(back, (50, 50))
    back_dark = pygame.transform.scale(back_dark, (50, 50))

    message("this is next page", colors[2], 310,310,25, True)

    pygame.display.update()
def intro_page():


    main_button_intro = ("songs/main_button.mp3")
    main_button_intro_sound = pygame.mixer.Sound(main_button_intro)

    next_button_intro = ("songs/next_button.mp3")
    next_button_intro_sound = pygame.mixer.Sound(next_button_intro)

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

    intro_music = ("songs/intro_music.mp3")
    intro_music = pygame.mixer.Sound(intro_music)
    pygame.mixer.Channel(0).set_volume(0.2)
    pygame.mixer.Channel(0).play(intro_music)

    image = pygame.image.load("wallpaper/wallpaper_clean.jpg")
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
            # print(next_x)
            if about_x <= mousepos[0] <= about_x + 50 and 600 <= mousepos[1] <= 650:
                display.blit(about, (about_x, 600))
                pygame.display.update()
                # print("about")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print("about")
                    pygame.mixer.Channel(3).set_volume(1)
                    pygame.mixer.Channel(3).play(main_button_intro_sound)
                    about_func()
            else:
                display.blit(about_dark, (about_x, 600))
                pygame.display.update()

            if next_x <= mousepos[0] <= next_x + 50 and 600 <= mousepos[1] <= 650:
                display.blit(next, (next_x, 600))
                pygame.display.update()
                # print("next")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Channel(3).set_volume(1)
                    pygame.mixer.Channel(3).play(next_button_intro_sound)
                    # print("next")
                    done = True
            else:
                display.blit(next_dark, (next_x, 600))
                pygame.display.update()
    pygame.display.update()

color_inactive = pygame.Color((250, 90, 90))                                                                            # setting the color light red for regular use
color_active = pygame.Color((255, 0, 0))

# print("test")
snake_speed = -1
snake_color = -1
snake_wallpaper = -1
difficulty = [-1]


def box(x, y, box_color = color_inactive):
    box_to_use = pygame.Rect(x, y , 150, 40)
    pygame.draw.rect(display, box_color, box_to_use)

def wipe():
    display.blit(clean, (0,0))


def drop_down_button(event, options, x_location,y_location, box_name, box_value):
    b = True
    pygame.draw.rect(display, color_active, box_name)
    # print(box_value)
    if box_value != -1:
        # print("hello")
        for i in range(int(len(options)/2)):
            if box_value == options[i]:
                message(options[i + int(len(options)/2)], colors[0], x_location+30, y_location+10, 24, True)
                # print("hi")
    else:
        message("Select", colors[0], x_location+30, y_location+10, 24,True)
    sub_buttons = {}
    for i in range(int(len(options)/2)):
        sub_buttons[i] = pygame.Rect(x_location, y_location+(40*(i+1)),150,40)
    if event.type == pygame.MOUSEBUTTONDOWN:
        global a
        a = True
        w = False
        if box_name.collidepoint(event.pos):
            for i in range(int(len(options)/2)):
                box(x_location, y_location+(40*(i+1)))
                message(options[i + int(len(options) / 2)], colors[0],x_location+30,
                        y_location+10+(40*(i+1)), 20, True)
            while a:
                for event in pygame.event.get():
                    mousepos = pygame.mouse.get_pos()
                    # print(mousepos)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        a = False
                    for i in range(int(len(options) / 2)):
                        if (x_location <= mousepos[0] <=x_location+150 )and (
                                (y_location + (40*(i+1)))<= mousepos[1] <= (y_location+(40*(i+2)))):
                            # print("pressed")
                            pygame.draw.rect(display, color_active, sub_buttons[i])
                            message(options[i + int(len(options)/2)], colors[0],x_location+30,
                                    y_location + 10 + (40 * (i + 1)), 20, True)
                            if event.type==pygame.MOUSEBUTTONDOWN:
                                # print("pressed")
                                a = False
                                box_value = i
                                # print(box_value)
                                pygame.event.clear()
                                w = True
                        else:
                            pygame.draw.rect(display, color_inactive,sub_buttons[i])
                            message(options[i+int(len(options)/2)], colors[0], x_location+30,
                                    y_location + 10 + (40 * (i + 1)), 20, True)

                        if w:
                            wipe()
                    if (x_location <= mousepos[0] <= x_location + 150) and (                                            # code to make the drop down disappear when you click on another area other than the sub button
                        (y_location + (40 * (i + 1))) <= mousepos[1] <= (y_location + (40 * (i + 2)))):
                        pass
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        print("pressed outside")
                        wipe()
                        a = False
                        break
        else:
            b = False
    # print("returning:", box_value)
    pygame.display.update()
    return b,box_value

def else_drop_down_button(options, x_location, y_location, box_name, box_value):
    pygame.draw.rect(display, color_inactive, box_name)
    if box_value != -1:
        for i in range(int(len(options)/2)):
            if box_value == options[i]:
                message(options[i + int(len(options)/2)], colors[0], x_location+30, y_location+10, 24, True)
    else:
        message("Select", colors[0], x_location+30, y_location+10, 24, True)
    pygame.display.update()

def button(x_location, y_location, box_name, text):
    # pygame.draw.rect(display, color_active, box_name)

    if difficulty[0] != -1 and difficulty[0] == str(text):
        pygame.draw.rect(display, color_inactive, box_name)
    else:
        pygame.draw.rect(display, color_active, box_name)
    message(str(text), colors[0], x_location + 30, y_location + 10, 24, True)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if box_name.collidepoint(event.pos):
            difficulty[0] = str(text)

    pygame.display.update()
def else_button(x_location, y_location, box_name, text):
    if difficulty[0] != -1 and difficulty[0] == str(text):
        pygame.draw.rect(display, color_active, box_name)
    else:
        pygame.draw.rect(display, color_inactive, box_name)
    # pygame.draw.rect(display, color_inactive, box_name)
    message(str(text), colors[0], x_location + 30, y_location + 10, 24, True)
    pygame.display.update()


intro_page()

clean = pygame.image.load("wallpaper/wallpaper_clean.jpg")
clean = pygame.transform.scale(clean, (620, 720))
clean = clean.convert()
display.blit(clean, (0,0))
pygame.display.update()
# time.sleep(3)

box_x = 110
box_y = 300

snake_color_box = pygame.Rect(box_x, box_y, 150, 40)
wallpaper_box = pygame.Rect(box_x + 250, box_y, 150, 40)
easy_box = pygame.Rect(box_x, box_y - 80, 120, 40)
medium_box = pygame.Rect(box_x + 140, box_y -80, 120, 40)
hard_box = pygame.Rect(box_x + 280, box_y- 80, 120, 40)

mousepos = ()
run = True

next = pygame.image.load("icons/next.png")                                                                              # loads in the icon for next
next_dark = pygame.image.load("icons/next_dark.png")                                                                    # loads in the icon for dark next
next = pygame.transform.scale(next, (icon_size, icon_size))                                                             # scales the next icon size to the right size
next_dark = pygame.transform.scale(next_dark, (icon_size, icon_size))                                                   # scales the dark next icon to the right size
selected = 0
# color_inactive = pygame.Color((250, 90, 90))                                                                            # setting the color light red for regular use
# color_active = pygame.Color((255, 0, 0))
#
# snake_speed = -1
# snake_color = -1
# snake_wallpaper = -1

while run:
    for event in pygame.event.get():
        mousepos = pygame.mouse.get_pos()
        a = False
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False


        if box_x <= mousepos[0] <= box_x+120 and box_y - 80 <= mousepos[1] <= box_y -40:
            # print("easy")
            x_location = box_x
            y_location = box_y - 80
            button(x_location,y_location, easy_box, "Easy")



        else:
            x_location = box_x
            y_location = box_y - 80
            else_button(x_location,y_location, easy_box, "Easy")

        if box_x + 140 <= mousepos[0] <= box_x + 260 and box_y - 80 <= mousepos[1] <= box_y -40:
            # print("medium")
            x_location = box_x + 125
            y_location = box_y - 80
            button(x_location, y_location, medium_box,"Medium")
        else:
            x_location = box_x + 125
            y_location = box_y - 80
            else_button(x_location, y_location, medium_box, "Medium")

        if box_x + 260 <= mousepos[0] <= box_x + 380 and box_y - 80 <= mousepos[1] <= box_y - 40:
            # print("hard")
            x_location = box_x + 280
            y_location = box_y - 80
            button(x_location, y_location, hard_box,"Hard")

        else:
            x_location = box_x + 280
            y_location = box_y - 80
            else_button(x_location, y_location, hard_box,"Hard")

        if box_x <= mousepos[0] <= box_x + 150 and box_y <= mousepos[1] <= box_y + 40:
            options = [0,1,2,"Red","Black", "White"]
            x_location = box_x
            y_location = box_y
            returned = drop_down_button(event, options, x_location,y_location,snake_color_box,snake_color)
            if not returned[0]:
                break
            snake_color = returned[1]
            # print("snake color = ", snake_color)
            pygame.display.update()
        else:
            options = [0,1,2,"Red","Black","White"]
            x_location = box_x
            y_location = box_y
            else_drop_down_button(options, x_location, y_location, snake_color_box,snake_color)
            pygame.display.update()

        if box_x + 250 <= mousepos[0] <= box_x + 400 and box_y <= mousepos[1] <= box_y + 40:
            options = [0,1,2,3,"Space", "Mars", "City", "Forest"]
            x_location = box_x + 250
            y_location = box_y
            returned = drop_down_button(event, options, x_location, y_location, wallpaper_box, snake_wallpaper)
            if not returned[0]:
                break
            snake_wallpaper = returned[1]
            # print("snake wallpaper = ", snake_wallpaper)
            pygame.display.update()
        else:
            options = [0,1,2,3,"Space", "Mars", "City", "Forest"]
            x_location = box_x + 250
            y_location = box_y
            else_drop_down_button(options, x_location,y_location, wallpaper_box, snake_wallpaper)
            pygame.display.update()

        if 385 <= mousepos[0] <= 435 and 600 <= mousepos[1] <= 650:
            # run = False
            display.blit(next, (385, 600))
        else:
            display.blit(next_dark, (385, 600))

        if snake_color != -1  and snake_wallpaper != -1 and difficulty[0] != -1: #and snake_speed != -1:
            selected = 1

        if event.type == pygame.MOUSEBUTTONDOWN and selected == 1:
            if 385 <= mousepos[0] <= 435 and 600 <= mousepos[1] <= 650:
                run = False

        elif selected == 0 and pygame.MOUSEBUTTONDOWN and (
            385 <= mousepos[0] <= 435 and 600 <= mousepos[1] <= 650):
            message("Please select all options", colors[0], 210, 665, 20, True)


if difficulty[0] == "Easy":
    snake_speed = 10
elif difficulty[0] == "Medium":
    snake_speed = 40
elif difficulty[0] == "Hard":
    snake_speed = 70

if snake_color == 0:
    snake_color = (255,0,0)
elif snake_color == 1:
    snake_color  = (0,0,0)
elif snake_color == 2:
    snake_color = (255,255,255)

if snake_wallpaper == 0:
    snake_wallpaper = "space.jpg"
elif snake_wallpaper == 1:
    snake_wallpaper = "mars.jpg"
elif snake_wallpaper == 2:
    snake_wallpaper = "city.jpg"
elif snake_wallpaper == 3:
    snake_wallpaper = "forest.jpg"
print(snake_color)
print(snake_wallpaper)
print(snake_speed)
def enter_game(snake_speed, snake_color, wallpaper):

    start_time[0] = time.time()

    snake_block = 20
    # snake_speed = 10
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
    # print(turn_locations)

    def snake(snake_block_function, snake_list_function):
        for site in snake_list_function:
            pygame.draw.rect(display, snake_color,
                             [site[0], site[1], snake_block_function, snake_block_function],
                             width=3)

    def background():
        # pygame.draw.rect(display, pygame.Color((0, 0, 0)), [0, 0, 620, 720])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # for i in range(1, 32):
        #     pass
            # pygame.draw.line(display, pygame.Color((255, 0, 0)), (0, (i * 20)), (620, (i * 20)), width=1)
            # pygame.draw.line(display, pygame.Color((255, 0, 0)), ((i * 20), 0), ((i * 20), 620), width=1)
            #
            # pygame.draw.line(display, pygame.Color((0, 255, 0)), (0, ((i + 31) * 20)), (620, ((i + 31) * 20)), width=1)
            # pygame.draw.line(display, pygame.Color((0, 255, 0)), ((i * 20), 620), ((i * 20), 720), width=1)

    def food_display():
        food = pygame.image.load("icons/apple.png")
        food = pygame.transform.scale(food, (20, 20))
        for food_item in food_pos:
            # pygame.draw.rect(display, pygame.Color((0, 0, 255)), [((food_item[0])), ((food_item[1])), 20, 20])
            display.blit(food, (((food_item[0])), ((food_item[1]))))

    def carriage_drawing(carriage_pos):
        carriage = pygame.image.load("icons/carriage.png")
        carriage = pygame.transform.scale(carriage, (60, 40))
        # carriage = carriage.convert()

        display.blit(carriage, ((carriage_pos*20-20), 640))

    def game():

        game_over[0] = False
        snake_list = []
        length_of_snake = [10]
        turning_right = [True]

        x = [-20]
        y = [0]
        carriage_x = [15]

        def carriage(snake_block):
            food = pygame.image.load("icons/apple.png")
            food = pygame.transform.scale(food,(20,20))

            while True:
                background_image = "wallpaper/"+str(wallpaper)
                clean = pygame.image.load(background_image)
                clean = pygame.transform.scale(clean, (620, 720))
                clean = clean.convert()

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

                display.blit(clean, (0,0))

                for food_item in food_pos:

                    display.blit(food, (((food_item[0])), ((food_item[1]))))
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
            bullet_icon = pygame.image.load("icons/bullet.png")
            bullet_icon = pygame.transform.scale(bullet_icon, (20, 20))
            bullet_y = 32
            i = 1

            while True:

                if bullet_state[0] == True:
                    display.blit(bullet_icon,((carriage_x[0] * 20),(bullet_y * 20)))
                    # pygame.draw.rect(display, pygame.Color((255, 0, 0)), [(carriage_x[0] * 20),
                    #                                                       (bullet_y * 20), 20, 20])
                    pygame.display.update()
                    bullet_y -= 1
                    pygame.time.Clock().tick(500)
                    if bullet_y < 0:
                        bullet_y = 32

                    for i in snake_list:

                        bullet_spot = [carriage_x[0]*20, bullet_y*20]

                        if bullet_spot in food_pos:
                            # print("hit food")
                            bullet_y = 32

                        if carriage_x[0]*20 == i[0] and bullet_y*20 == i[1]:
                            if snake_list.index(i) == (len(snake_list)-1) :

                                # print("hit", i[0], i[1])
                                bullet_y = 32
                                removed_part = snake_list[:(snake_list.index(i) + 1)]
                                del snake_list[:(snake_list.index(i) + 1)]
                                length_of_snake[0] = len(snake_list)
                                for i in removed_part:
                                    food_pos.append(i)

                                turn_locations_finder()
                                # print(turn_locations)

                                x[0] = -20
                                y[0] = 0
                                length_of_snake[0] = 1
                                bullet_state[0] = False

                            else:
                                # print("hit", i[0], i[1])
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


enter_game(snake_speed,snake_color, snake_wallpaper)
pygame.quit()
sys.exit()
