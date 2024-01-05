import pygame

# SETUP
pygame.init()

# TODO GET RESOLUTION OF PI SCREEN
# Use non-fullscreen when coding
screen = pygame.display.set_mode((600,600))
# screen = pygame.display.set_mode((600,600), pygame.FULLSCREEN, vsync=1)

clock = pygame.time.Clock()
running = True
menu = False

# Setup base background image
screen_idle = pygame.image.load('assets/bmo_idle.jpeg').convert()
screen_idle = pygame.transform.smoothscale(screen_idle, screen.get_size())

screen_menu = pygame.image.load('assets/bmo_menu.png').convert()
screen_menu = pygame.transform.smoothscale(screen_menu, screen.get_size())

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                menu = True

    screen.fill("purple")

    if menu:
        screen.blit(screen_menu, (0,0))
    else:
        screen.blit(screen_idle, (0,0))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
