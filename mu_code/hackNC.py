import pygame
import math
import numpy as np
import time
import random
reqexp = 10
winningState = False
typeOfPlant = "wheat"
gameState = "start"
firstPressed = False
nextPressed = False
organic = False
weather = 0
timer = 0
points: int = 0
level: int = 1
def increaseTimer():
    global timer
    timer += 1
clock.schedule_interval(increaseTimer, 1.0)
pygame.init()
WIDTH = 840
HEIGHT = 780
N = 100000
arr = [0]*N
index = 0

tempArr = np.zeros((8,12))
timeArr = np.zeros((8,12))
#wheat = Actor('wheat', (105,105))
#maybe we want to populate an array with wheat image objects in the appropriate location relative to the grid,
#but we can only draw them with wheat.draw() if tempArr[y][x] == 2 in the correct coordinates.
#wheat._surf = pygame.transform.scale(wheat._surf, (68, 68))
farmer2 = Actor("farmer2")
farmer2._surf = pygame.transform.scale(farmer2._surf, (75, 75))
music.play("soundtrack")
def draw():
    global timer, points, level, winningState, gameState
    screen.clear()
    if gameState == "start":
        screen.draw.text("Wheat or corn? Press w for wheat, c for corn", top = 300,left=75,fontsize=45,color = (100,150,120))
        screen.draw.text("GMO or non-GMO? Press g for GMO and o for non-GMO", top =450,left=21,fontsize=45,color = (100,150,120))
    else:
        w = 0
        h = 0
        SIZE = 68
        #SIZE_R = 48
        r_color = 50
        g_color = 180
        b_color = 8
        for x in range(0,8):
            for y in range(0,12):
                theRect = Rect((w, h), (SIZE,SIZE))
                if tempArr[x][y] == 0:
                    screen.draw.filled_rect(theRect,(168,102,50))
                    #barren soil that has yet to be tilled
                if tempArr[x][y] == 1:
                    screen.draw.filled_rect(theRect,(101, 67, 33))
                    #tilled soil
                if tempArr[x][y] == 2:
                    screen.draw.filled_rect(theRect,(50, 205, 50))
                    #pesticides added
                if tempArr[x][y] == 3:
                    screen.draw.filled_rect(theRect,(0, 128, 0))
                    #water has been added
                    #idk but make something blue
                if tempArr[x][y] == 4:
                    screen.draw.filled_rect(theRect,(173, 216, 230))
                    #GROWING PLANT, change to picture of
                if tempArr[x][y] == 5:
                    #TODO MAKE A PIC OF WHEAT
                    #TESTE
                    if typeOfPlant == "wheat":
                        wheat = Actor("wheat",(35+(70*y),35+(70*x)))
                        wheat.draw()
                    else:
                        corn = Actor("corn",(35+(70*y),35+(70*x)))
                        corn.draw()
                    #TEST
                    #screen.draw.filled_rect(theRect,(250,250,250))
                    #wheat.draw()
                w += 70
            w = 0
            h += 70
        weatherPredictor()
        if (weather == 0 or weather == 2):
            screen.draw.text("It is sunny.", top = 0, left = 400)
        elif weather == 1:
            screen.draw.text("It is raining.", top = 0, left = 400)


        on_key_down()
        farmer2.draw()
        screen.draw.text("Farmers plant, grow, and harvest all the food we eat. This game will let you work like a farmer!", top=580, left=50)
        screen.draw.text("Game Controls:", top=620, left=50)
        screen.draw.text("TIMER: " + str(timer), top = 620, left = 550)
        screen.draw.text("Press T to till the field, tilling loosens the soil and prepares it for seeding!", top=650, left=50)
        screen.draw.text("Press S to seed the field, all crops grow from seeds!", top=670, left=50)
        screen.draw.text("Press A to apply pesticide on the crops, pesticides kill dangerous insects and rival plants!", top=690, left=50)
        screen.draw.text("Press W to water the crops after applying pesticides", top=710, left=50)
        screen.draw.text("Press H to move the harvest from your farm to the farmer's market for sale!", top=730, left=50)
        #screen.draw.text("Press F to feed the animals, animals can help with labor and provide an extra source of food!", top= 750, left=50)
        screen.draw.text(f"Lvl. {level}", top = 760, left = 50)
        screen.draw.text(f"Points: {points}", top= 760, left= 550)
        if winningState == True:
            screen.fill((0,0,0))
            screen.draw.text("CONGRATS YOU REACHED LEVEL 5 AND WON THE GAME!", top =390, left= 175)

def update():
    global typeOfPlant, firstPressed,nextPressed,organic,typeOfPlant,gameState
    if (firstPressed and nextPressed):
        gameState = "play"
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and farmer2.right < WIDTH:
        farmer2.x += 3 + (2*level)
    if pressed[pygame.K_DOWN] and farmer2.bottom < 580:
        farmer2.y += 3 + (2*level)
    if pressed[pygame.K_LEFT] and farmer2.left > 0:
        farmer2.x -= 3 + (2*level)
    if pressed[pygame.K_UP] and farmer2.top > 0:
        farmer2.y -= 3 + (2*level)
    for a in range(8):
        for b in range(12):
            if typeOfPlant == "wheat":
                if (timer - timeArr[a][b] == 10 and timeArr[a][b] != 0):
                    tempArr[a][b] = 5
            elif (timer - timeArr[a][b] == 7 and timeArr[a][b] != 0):
                    tempArr[a][b] = 5
    #MAKE it change from 4 to 5 after a period of time
    #loop through the timeArray
    #if (timer - [val in time 2d array] == 10):
        #change the val in the indicies in the tempArr to 5
    levelup()


def on_key_down():
    global index, timer, points, gameState, firstPressed, nextPressed, organic, typeOfPlant
    pressed = pygame.key.get_pressed()
    if (keyboard.c and not firstPressed):
        typeOfPlant = "corn"
        firstPressed = True
    if (keyboard.w and not firstPressed):
        typeOfPlant = "wheat"
        firstPressed = True
    if (keyboard.g and not nextPressed):
        organic = False
        nextPressed = True
    if (keyboard.o and not nextPressed):
        organic = True
        nextPressed = True
    w = 0
    h = 0

    SIZE = 68
    if (keyboard.t):
        #the farmer is tilling the soil, this will overwrite any other thing that is on the soil
        sounds.tilling.play()
        x = farmer2.x
        y = farmer2.y
        square_x_count = math.floor(x/70)
        square_y_count = math.floor(y/70)
        x = 70*square_x_count
        y = 70*square_y_count
        tempArr[square_y_count][square_x_count] = 1

    if (keyboard.s):
        #planting seeds in tilled soil
        sounds.seeds.play()
        x = farmer2.x
        y = farmer2.y
        square_x_count = math.floor(x/70)
        square_y_count = math.floor(y/70)
        x = 70*square_x_count
        y = 70*square_y_count
        if tempArr[square_y_count][square_x_count] == 1:
            tempArr[square_y_count][square_x_count] = 2

    if (keyboard.a):
        #pesiticides which can only be applied to seeded soil
        x = farmer2.x
        y = farmer2.y
        square_x_count = math.floor(x/70)
        square_y_count = math.floor(y/70)
        x = 70*square_x_count
        y = 70*square_y_count
        if tempArr[square_y_count][square_x_count] == 2:
            tempArr[square_y_count][square_x_count] = 3

    if (keyboard.w):
        #watering
        sounds.watering.play()
        x = farmer2.x
        y = farmer2.y
        square_x_count = math.floor(x/70)
        square_y_count = math.floor(y/70)
        x = 70*square_x_count
        y = 70*square_y_count
        if tempArr[square_y_count][square_x_count] == 3:
            tempArr[square_y_count][square_x_count] = 4
            timeArr[square_y_count][square_x_count] = timer
            #NOW IF ITS 4 MAKE IT
    if (keyboard.h):
        #the farmer is tilling the soil, this will overwrite any other thing that is on the soil
        sounds.tractor.play()
        x = farmer2.x
        y = farmer2.y
        square_x_count = math.floor(x/70)
        square_y_count = math.floor(y/70)
        x = 70*square_x_count
        y = 70*square_y_count
        if tempArr[square_y_count][square_x_count] == 5:
            tempArr[square_y_count][square_x_count] = 0
            if typeOfPlant == "wheat":
                if organic:
                    points += 3
                else:
                    points += 6
            else:
                if organic:
                    points +=1
                else: points += 2

def weatherPredictor():
    global weather
    randomNumber = random.randint(0,2)
    if (timer%11==0):
        if (randomNumber in [0]):
            weather = 1
        elif randomNumber in [1]:
            weather = 2
        else:
            weather = 0

def levelup():
    global points, level, reqexp, winningState
    if points >= reqexp:
        level += 1
        reqexp += (reqexp * 2)
    if level >= 5:
        winningState = True

        # 10 30 90 270

