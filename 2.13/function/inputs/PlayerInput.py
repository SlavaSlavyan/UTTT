import pygame

class PlayerInput:

    def __init__(self,m):
        m.Log.write("Инициализация класса ввода от пользователя.","DEBUG")

    def main(self,m):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                m.Log.write("Пользователь запустил эвент выхода.","WARNING")
                m.stop()
    
    def logic(self,m):
        pass