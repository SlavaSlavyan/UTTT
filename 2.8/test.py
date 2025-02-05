import random

stage = 0
money = 0
health = 20
mana = 20
inventory = {
    "magic stick":{
        "atc":5,
        "chance":60,
        "mana":4
    },
    "sword":{
        "atc":2,
        "crit chance":10,
        "crit multiplier":2
    }
}
cave = {
    "empty":10,
    "bottle":20,
    "chest":20,
    "mouse":20
}

def start():
    
    while True:
        pass

def impediment():

    sum = 0
    for s,i in cave.items():
        sum += i
    r = random.randint(0,sum)

    sum = 0

    for key,value in cave.items():

        if r >= 0+sum and r < value+sum:
            return key, r
        sum += value

start()