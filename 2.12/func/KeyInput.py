import pygame

class KeyInput:

    def __init__(self,m):
        
        self.keys = {
            "space":False,
            "enter":False,
            "up":False,
            "down":False,
            "left":False,
            "right":False,
            "w":False,
            "s":False,
            "a":False,
            "d":False,
            "esc":False
        }

    def main(self,m,event):

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
            
            if event.key == pygame.K_SPACE:
                self.keys['space'] = True
            if event.key == pygame.K_RETURN:
                self.keys['enter'] = True
            if event.key == pygame.K_UP:
                self.keys['up'] = True
            if event.key == pygame.K_DOWN:
                self.keys['down'] = True
            if event.key == pygame.K_LEFT:
                self.keys['left'] = True
            if event.key == pygame.K_RIGHT:
                self.keys['right'] = True
            if event.key == pygame.K_w:
                self.keys['w'] = True
            if event.key == pygame.K_s:
                self.keys['s'] = True
            if event.key == pygame.K_a:
                self.keys['a'] = True
            if event.key == pygame.K_d:
                self.keys['d'] = True
            if event.key == pygame.K_ESCAPE:
                self.keys['esc'] = True
            
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_SPACE:
                self.keys['space'] = False
            if event.key == pygame.K_RETURN:
                self.keys['enter'] = False
            if event.key == pygame.K_UP:
                self.keys['up'] = False
            if event.key == pygame.K_DOWN:
                self.keys['down'] = False
            if event.key == pygame.K_LEFT:
                self.keys['left'] = False
            if event.key == pygame.K_RIGHT:
                self.keys['right'] = False
            if event.key == pygame.K_w:
                self.keys['w'] = False
            if event.key == pygame.K_s:
                self.keys['s'] = False
            if event.key == pygame.K_a:
                self.keys['a'] = False
            if event.key == pygame.K_d:
                self.keys['d'] = False
            if event.key == pygame.K_ESCAPE:
                self.keys['esc'] = False