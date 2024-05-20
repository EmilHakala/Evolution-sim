import pygame
import random
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


def neural(direction, distance):
    


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
        pygame.draw.circle(screen, "red", blob[i], 10)
        pygame.draw.circle(screen, "green", food[i], 5)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()