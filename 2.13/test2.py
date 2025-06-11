import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Example")

font_size = 32
font = pygame.font.Font(None, font_size)

text = "Hello, Pygame!"
color = (255, 255, 255)
text_surface = font.render(text, True, color)

text_rect = text_surface.get_rect()
text_rect.topright = (width // 2, height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

pygame.quit()
