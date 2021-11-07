import pygame
pygame.init()
WIDTH = 840
HEIGHT = 780
# farmer is 512 by 500    6.8      512 * 1/75 = 6.8
# green is 350 by 350   350/x = 6.8
#brown is 1920 by 1080    282, 159
# brown is
#initialize the green stuff
farmer = Actor("farmer")
farmer._surf = pygame.transform.scale(farmer._surf, (75, 75))
listylist = []
w = 0
h = 0
for x in range(0,8):
    for y in range(0,12):
        gr = Actor("green", (w, h))
        gr._surf = pygame.transform.scale(gr._surf, (51, 51))
        listylist.append(gr)
        w += 70
    w = 0
    h += 70

#farmer = pygame.Surface(50,50)
#farmer = Actor("cow", center=(WIDTH/10,HEIGHT/10))

def draw():
    screen.clear()
    for gr in listylist:
        gr.draw()


    farmer.draw()
    screen.draw.text("Farmers plant, grow, and harvest all the food we eat. This game will let you work like a farmer!", top=580, left=50)
    screen.draw.text("Game Controls:", top=620, left=50)
    screen.draw.text("Press T to till the field, tilling loosens the soil and prepares it for seeding!", top=650, left=50)
    screen.draw.text("Press S to seed the field, all crops grow from seeds!", top=670, left=50)
    screen.draw.text("Press A to apply pesticide on the crops, pesticides kill dangerous insects and rival plants!", top=690, left=50)
    screen.draw.text("Press H to harvest the crops, gathering the ripe crops from the field!", top=710, left=50)
    screen.draw.text("Press M to move the harvest fromy your farm to the farmer's market for sale!", top=730, left=50)
    screen.draw.text("Press F to feed the animals, animals can help with labor and provide an extra source of food!", top= 750, left=50)

    #cow.draw()
#def brownPlot():

def update():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        farmer.x += 5
    if pressed[pygame.K_DOWN]:
        farmer.y += 5
    if pressed[pygame.K_LEFT]:
        farmer.x -= 5
    if pressed[pygame.K_UP]:
        farmer.y -= 5

    on_key_down()

def on_key_down():
    for gr in listylist:
        pressed = pygame.key.get_pressed()
    #w = 0
    #h = 0
    #SIZE = 68
    #for x in range(0,25):
        #for y in range(0,25):
            #object = Rect((w, h), (SIZE,SIZE))
        if (pressed[pygame.K_SPACE]) and farmer.colliderect(gr):
            gr.image = "brown"
            gr._surf = pygame.transform.scale(gr._surf, (282, 159))
                #screen.draw.filled_rect(object,(0, 0, 0))
                #changeSquareBrown(w,h)
            #w += 70
        #w = 0
        #h += 70

def changeSquareBrown(w,h):
    r_color = 50
    g_color = 50
    b_color = 50
    SIZE = 68
    object = Rect((w,h),(SIZE,SIZE))
    screen.draw.filled_rect(object, (r_color,g_color,b_color))

