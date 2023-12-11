import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("fighting game")




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()


    if keys[pygame.K_a]:
        print("Key A Pressed")

    if keys[pygame.K_d]:
        print("Key D Pressed")