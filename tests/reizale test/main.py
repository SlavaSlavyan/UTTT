import pygame
import sys
import json

with open('config.json', 'r') as file:
    config = json.load(file)

size = config["size"]

pygame.init()

width, height = 1000, 700
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)
pygame.display.set_caption("reizable test")

square = {"offset":0,"x":None,"y":None}

def square():

    global square

    pygame.draw.polygon(screen, (0,0,0), [()])

    
    

while True:

    screen.fill((255,255,255))
    width, height = screen.get_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = event.pos
    
    pygame.display.flip()
    pygame.time.Clock().tick(120)