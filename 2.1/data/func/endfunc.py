import pygame
import json
import sys
import math

def getThem(numscreen):
    
    with open(f'data\\them\\{config('them')}.json', 'r', encoding='utf-8') as file:
        them = json.load(file)
        print(them[numscreen])
        result = []
        for item in them[numscreen]:
            result.append(tuple(map(int, item.split(','))))

    return result

def getLang():

    with open(f'data\\lang\\{config('lang')}.json', 'r', encoding='utf-8') as file:
        lang = json.load(file)

    return lang

def config(arg):

    with open('data\\settings.json', 'r', encoding='utf-8') as file:
        parameters = json.load(file)
        parameters = parameters[0]
    
    return parameters[arg]

def gradient(color, color2, steps):

    gradient = []
    
    for step in range(steps):
        
        r = int(color[0] + (color2[0] - color[0]) * step / (steps - 1))
        g = int(color[1] + (color2[1] - color[1]) * step / (steps - 1))
        b = int(color[2] + (color2[2] - color[2]) * step / (steps - 1))
        
        gradient.append((r, g, b))
    
    return gradient