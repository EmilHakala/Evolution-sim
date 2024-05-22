import pygame
import random
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True
dt = 0
amount=100
blob=[]
food=[]
to_food=[]
for i in range(amount):
    to_food.append(pygame.Vector2(0,0))

# blob attributes
health_size=[]
speed=4
attack=[]
mvdir=""
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
ow1=[]
ow2=[]
ow3=[]
ow4=[]
def find_food(x,y,fx,fy):
    final=pygame.Vector2(fx-x, fy-y)
    final.x=final.x/90
    final.y=final.y/90
    #print("final:", final, "old:", x,y,fx,fy)
    return final

def neural(dir,i):
    #print(dir.x,dir.y)
    #first hidden layer
    h1=dir.x*w1[i]+dir.y*w1[i]
    h2=dir.x*w2[i]+dir.y*w2[i]
    h3=dir.x*w3[i]+dir.y*w3[i]
    h4=dir.x*w4[i]+dir.y*w4[i]
    h5=dir.x*w5[i]+dir.y*w5[i]
    h6=dir.x*w6[i]+dir.y*w6[i]
    print(h1)
    #second hidden layer
    lh1=h1*w7[i]+h2*w7[i]+h3*w7[i]+h4*w7[i]+h5*w7[i]+h6*w7[i]
    lh2=h1*w8[i]+h2*w8[i]+h3*w8[i]+h4*w8[i]+h5*w8[i]+h6*w8[i]
    lh3=h1*w9[i]+h2*w9[i]+h3*w9[i]+h4*w9[i]+h5*w9[i]+h6*w9[i]
    lh4=h1*w10[i]+h2*w10[i]+h3*w10[i]+h4*w10[i]+h5*w10[i]+h6*w10[i]
    lh5=h1*w11[i]+h2*w11[i]+h3*w11[i]+h4*w11[i]+h5*w11[i]+h6*w11[i]
    lh6=h1*w12[i]+h2*w12[i]+h3*w12[i]+h4*w12[i]+h5*w12[i]+h6*w12[i]
    #output layer
    o1=lh1*ow1[i]+lh2*ow1[i]+lh3*ow1[i]+lh4*ow1[i]+lh5*ow1[i]+lh6*ow1[i]
    o2=lh1*ow2[i]+lh2*ow2[i]+lh3*ow2[i]+lh4*ow2[i]+lh5*ow2[i]+lh6*ow2[i]
    o3=lh1*ow3[i]+lh2*ow3[i]+lh3*ow3[i]+lh4*ow3[i]+lh5*ow3[i]+lh6*ow3[i]
    o4=lh1*ow4[i]+lh2*ow4[i]+lh3*ow4[i]+lh4*ow4[i]+lh5*ow4[i]+lh6*ow4[i]
    #what output
    print(o1,o2,o3,o4)
    if o1>o2 and o1>o3 and o1>o4:
        print(i, "up")
        return "up"
    elif o2>o1 and o1>o3 and o1>o4:
        print(i, "down")
        return "down"
    elif o3>o2 and o1>o1 and o1>o4:
        print(i, "left")
        return "left"
    elif o4>o1 and o1>o3 and o1>o2:
        print(i, "right")
        return "right"
    

for i in range(amount):
    blob.append(pygame.Vector2(random.randrange(900), random.randrange(600)))
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
    ow1.append(random.randrange(0,1000)/1000)
    ow2.append(random.randrange(0,1000)/1000)
    ow3.append(random.randrange(0,1000)/1000)
    ow4.append(random.randrange(0,1000)/1000)
for i in range(amount):
    food.append(pygame.Vector2(random.randrange(900), random.randrange(600)))

def move(dirmv,i):
    if dirmv=="left":
        blob[i].x = blob[i].x + speed
    elif dirmv=="right":
        blob[i].x = blob[i].x - speed
    elif dirmv=="up":
        blob[i].y = blob[i].y - speed
    elif dirmv=="down":
        blob[i].y = blob[i].y + speed
    return blob[i]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    for i in range(amount):
        for x in range(amount):
            #print(blob[i], food[x])
            if (blob[i].x + 90 > food[x].x and blob[i].x - 90 < food[x].x):
                if (blob[i].y + 90 > food[x].y and blob[i].y - 90 < food[x].y):
                    #print("MEOW")
                    to_food[i]=find_food(blob[i].x,blob[i].y,food[x].x,food[x].y)
        blob[i] = move(neural(to_food[i],i),i)
        pygame.draw.circle(screen, "red", blob[i], 10)
        pygame.draw.circle(screen, "green", food[i], 5)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
