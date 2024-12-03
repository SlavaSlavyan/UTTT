import pygame
import json
import sys
import math

def getThem():

    with open(f'data\\them\\{config('them')}.json', 'r', encoding='utf-8') as file:
        them = json.load(file)
    
    colors = {key: tuple(map(int, value.split(','))) for key, value in them.items()}
    
    return colors

def getLang(num):

    with open(f'data\\lang\\{config('lang')}.json', 'r', encoding='utf-8') as file:
        lang = json.load(file)

    return lang[num]

def config(arg):

    with open('data\\settings.json', 'r', encoding='utf-8') as file:
        parameters = json.load(file)
    
    return parameters[arg]

def gradient(color, color2, steps):

    gradient = []
    
    for step in range(steps):
        
        r = int(color[0] + (color2[0] - color[0]) * step / (steps - 1))
        g = int(color[1] + (color2[1] - color[1]) * step / (steps - 1))
        b = int(color[2] + (color2[2] - color[2]) * step / (steps - 1))
        
        gradient.append((r, g, b))
    
    return gradient