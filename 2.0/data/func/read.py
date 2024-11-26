import pygame
import sys
import math

def getcolor(color):
    with open(f'data\\them\\{getsettings(1)}.txt', 'r', encoding='utf-8') as file:
        colors = file.readlines()
    colors = [line[:-1] for line in colors]
    colors = [i for i in colors if i != '']
    colors = [i for i in colors if not i.startswith('/')]
    colors = [line.replace(' ', '') for line in colors]
    color = tuple(map(int, colors[color].strip('()').split(',')))
    return color

def getstr(string):
    with open(f'data\\lang\\{getsettings(0)}.txt', 'r', encoding='utf-8') as file:
        strings = file.readlines()
    strings = [line[:-1] for line in strings]
    strings = [i for i in strings if i != '']
    strings = [i for i in strings if not i.startswith('/')]
    string = str(strings[string])
    return string

def getsettings(config):
    with open(f'data\\settings.txt', 'r', encoding='utf-8') as file:
        settings = file.readlines()
    settings = [line[:-1] for line in settings]
    settings = [i for i in settings if i != '']
    settings = [i for i in settings if not i.startswith('#')]
    settings = [line.replace(' ', '') for line in settings]
    return settings[config]

def gradient(color, color2, steps):

    gradient = []
    
    for step in range(steps):
        
        r = int(color[0] + (color2[0] - color[0]) * step / (steps - 1))
        g = int(color[1] + (color2[1] - color[1]) * step / (steps - 1))
        b = int(color[2] + (color2[2] - color[2]) * step / (steps - 1))
        
        gradient.append((r, g, b))
    
    return gradient