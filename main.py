import pygame
import random
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True
dt = 0
amount=10
blob=[]
food=[]


# blob attributes
health_size=[]
speed=[]
attack=[]
#nn
def find_food(x,y,fx,fy):
    final=pygame.Vector2(fx-x, fy-y)
    print("final:", final, "old:", x,y,fx,fy)
    return x

def neural(direction):
    
    return

for i in range(amount):
    blob.append(pygame.Vector2(random.randrange(900), random.randrange(600)))

for i in range(amount):
    food.append(pygame.Vector2(random.randrange(900), random.randrange(600)))


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
                    to_food=find_food(blob[i].x,blob[i].y,food[x].x,food[x].y)

        pygame.draw.circle(screen, "red", blob[i], 10)
        pygame.draw.circle(screen, "green", food[i], 5)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
