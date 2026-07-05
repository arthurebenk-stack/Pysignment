import pygame
pygame.init()
screen = pygame.display.set_mode((800, 750))
screen.fill((36,46,47))
pygame.display.set_caption("My Second Game🎮")

pygame.draw.polygon(screen, color, (0, 255, 255), (25,75),(320,125),(250,375))
pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()