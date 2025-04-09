import pygame

class KeyInput:

    def __init__(self,m):
        self.all_keys = pygame.key.get_pressed()

    def main(self,m,event):

        self.all_keys = pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if m.config['fullscreen']:
                    m.config['fullscreen'] = False
                else:
                    m.config['fullscreen'] = True
                m.Disp.setscreen(m)
            if event.key == pygame.K_F3:
                if m.Disp.Text.f3_allow:
                    m.Disp.Text.f3_allow = False
                else:
                    m.Disp.Text.f3_allow = True
                