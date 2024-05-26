import pygame
import random
import math
from neural import neuralNetwork
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0
amount=300
food_amount=amount
blob=[]
food=[]
to_food=[]

for i in range(amount):
    to_food.append(pygame.Vector2(0,0))

# blob attributes
health_size=[]
speed=10
attack=[]
color=[]
colorp=[]
#nn
w1=[]
w2=[]
w3=[]
w4=[]
w5=[]
w6=[]
w7=[]
w8=[]
w9=[]
w10=[]
w11=[]
w12=[]
w13=[]
w14=[]
w15=[]
w16=[]
w17=[]
w18=[]
w19=[]
w20=[]
w21=[]
w22=[]
w23=[]
w24=[]
b1=[]
b2=[]
b3=[]
b4=[]
b5=[]
b6=[]
w25=[]
w26=[]
w27=[]
w28=[]
w29=[]
w30=[]
w31=[]
w32=[]
w33=[]
w34=[]
w35=[]
w36=[]
for i in range(amount):
    w1.append(random.randrange(0,1000)/1000)
    w2.append(random.randrange(0,1000)/1000)
    w3.append(random.randrange(0,1000)/1000)
    w4.append(random.randrange(0,1000)/1000)
    w5.append(random.randrange(0,1000)/1000)
    w6.append(random.randrange(0,1000)/1000)
    w7.append(random.randrange(0,1000)/1000)
    w8.append(random.randrange(0,1000)/1000)
    w9.append(random.randrange(0,1000)/1000)
    w10.append(random.randrange(0,1000)/1000)
    w11.append(random.randrange(0,1000)/1000)
    w12.append(random.randrange(0,1000)/1000)
    w13.append(random.randrange(0,1000)/1000)
    w14.append(random.randrange(0,1000)/1000)
    w15.append(random.randrange(0,1000)/1000)
    w16.append(random.randrange(0,1000)/1000)
    w17.append(random.randrange(0,1000)/1000)
    w18.append(random.randrange(0,1000)/1000)
    w19.append(random.randrange(0,1000)/1000)
    w20.append(random.randrange(0,1000)/1000)
    w21.append(random.randrange(0,1000)/1000)
    w22.append(random.randrange(0,1000)/1000)
    w23.append(random.randrange(0,1000)/1000)
    w24.append(random.randrange(0,1000)/1000)
    b1.append(random.randrange(0,1000)/1000)
    b2.append(random.randrange(0,1000)/1000)
    b3.append(random.randrange(0,1000)/1000)
    b4.append(random.randrange(0,1000)/1000)
    b5.append(random.randrange(0,1000)/1000)
    b6.append(random.randrange(0,1000)/1000)
    w25.append(random.randrange(0,1000)/1000)
    w26.append(random.randrange(0,1000)/1000)
    w27.append(random.randrange(0,1000)/1000)
    w28.append(random.randrange(0,1000)/1000)
    w29.append(random.randrange(0,1000)/1000)
    w30.append(random.randrange(0,1000)/1000)
    w31.append(random.randrange(0,1000)/1000)
    w32.append(random.randrange(0,1000)/1000)
    w33.append(random.randrange(0,1000)/1000)
    w34.append(random.randrange(0,1000)/1000)
    w35.append(random.randrange(0,1000)/1000)
    w36.append(random.randrange(0,1000)/1000)
def find_food(x,y,fx,fy):
    final=pygame.Vector2(fx-x, fy-y)
    final.x=final.x/90
    final.y=final.y/90
    #print("final:", final, "old:", x,y,fx,fy)
    return final
   
def evolvenn(i):
    w1[i]+=random.randrange(-50,50)/1000
    w2[i]+=random.randrange(-50,50)/1000
    w3[i]+=random.randrange(-50,50)/1000
    w4[i]+=random.randrange(-50,50)/1000
    w5[i]+=random.randrange(-50,50)/1000
    w6[i]+=random.randrange(-50,50)/1000
    w7[i]+=random.randrange(-50,50)/1000
    w8[i]+=random.randrange(-50,50)/1000
    w9[i]+=random.randrange(-50,50)/1000
    w10[i]+=random.randrange(-50,50)/1000
    w11[i]+=random.randrange(-50,50)/1000
    w12[i]+=random.randrange(-50,50)/1000
    w13[i]+=random.randrange(-50,50)/1000
    w14[i]+=random.randrange(-50,50)/1000
    w15[i]+=random.randrange(-50,50)/1000
    w16[i]+=random.randrange(-50,50)/1000
    w17[i]+=random.randrange(-50,50)/1000
    w18[i]+=random.randrange(-50,50)/1000
    w19[i]+=random.randrange(-50,50)/1000
    w20[i]+=random.randrange(-50,50)/1000
    w21[i]+=random.randrange(-50,50)/1000
    w22[i]+=random.randrange(-50,50)/1000
    w23[i]+=random.randrange(-50,50)/1000
    w24[i]+=random.randrange(-50,50)/1000
    b1[i]+=random.randrange(-50,50)/1000
    b2[i]+=random.randrange(-50,50)/1000
    b3[i]+=random.randrange(-50,50)/1000
    b4[i]+=random.randrange(-50,50)/1000
    b5[i]+=random.randrange(-50,50)/1000
    b6[i]+=random.randrange(-50,50)/1000
    w25[i]+=random.randrange(-50,50)/1000
    w26[i]+=random.randrange(-50,50)/1000
    w27[i]+=random.randrange(-50,50)/1000
    w28[i]+=random.randrange(-50,50)/1000
    w29[i]+=random.randrange(-50,50)/1000
    w30[i]+=random.randrange(-50,50)/1000
    w31[i]+=random.randrange(-50,50)/1000
    w32[i]+=random.randrange(-50,50)/1000
    w33[i]+=random.randrange(-50,50)/1000
    w34[i]+=random.randrange(-50,50)/1000
    w35[i]+=random.randrange(-50,50)/1000
    w36[i]+=random.randrange(-50,50)/1000
def check_collision(x1, y1, w1, h1, x2, y2, w2, h2):
    return (x1 < x2 + w2 and
            x1 + w1 > x2 and
            y1 < y2 + h2 and
            y1 + h1 > y2)

for i in range(amount):
    blob.append(pygame.Vector2(random.randrange(1920), random.randrange(1080)))
    color.append((255, 0, 0))
    colorp.append(0)
for i in range(food_amount):
    food.append(pygame.Vector2(random.randrange(1920), random.randrange(1080)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    print("running")
    screen.fill("black")
    for i in range(amount):

        if blob[i].x >= 1920:
            blob[i].x=0
        if blob[i].y >= 1080:
            blob[i].y=0
        for x in range(food_amount):
            if check_collision(blob[i].x, blob[i].y, 15, 15, food[x].x, food[x].y, 10, 10):
                food[x]=(pygame.Vector2(random.randrange(1920), random.randrange(1080)))
                evolvenn(i)
                colorp[i] += 10
                if colorp[i] == 250:
                    colorp[i] = 0
                color[i] = 255,colorp[i],0
            if (blob[i].x + 90 > food[x].x and blob[i].x - 90 < food[x].x):
                if (blob[i].y + 90 > food[x].y and blob[i].y - 90 < food[x].y):
                    #print("MEOW")
                    to_food[i]=find_food(blob[i].x,blob[i].y,food[x].x,food[x].y)
        blob[i] = neuralNetwork(speed, blob,to_food[i],i,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,b1,b2,b3,b4,b5,b6,w25,w26,w27,w28,w29,w30,w31,w32,w33,w34,w35,w36)
        print(blob[i])
        pygame.draw.circle(screen, color[i], blob[i], 10)
        pygame.draw.circle(screen, "green", food[i], 5)

    pygame.display.flip()
    print("clock!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", dt)
    dt = clock.tick(60) / 1000

pygame.quit()
