import pygame
import json
import sys
import math

def getThem():
    
    with open(f'data\\them\\{config("them")}.json', 'r') as file:
        them = json.load(file)

    return them

def getLang():

    pass

def config(arg):

    with open('data\\settings.json', 'r') as file:
        parameters = json.load(file)
    
    return parameters[arg]