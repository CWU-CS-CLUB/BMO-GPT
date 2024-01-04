import pygame

# SETUP
pygame.init()

# TODO GET RESOLUTION OF PI SCREEN
# Use non-fullscreen when coding
screen = pygame.display.set_mode((600,600))
# screen = pygame.display.set_mode((600,600), pygame.FULLSCREEN, vsync=1)

clock = pygame.time.Clock()
running = True

# Setup base background image
background = pygame.image.load('assets/bmo_idle.jpeg').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESC:
                running = False

    screen.fill("purple")
    screen.blit(background, (0,0))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
