import pygame
import sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
isJump = False
jumpCount = 10

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if player_pos.x > 0:
            player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        if player_pos.x < 1280 :  # Assuming screen width is 1280
            player_pos.x += 300 * dt
    if not(isJump): 
        if keys[pygame.K_w]:
            if player_pos.y > 0:
                player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            if player_pos.y < 720 :  
                player_pos.y += 300 * dt

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            player_pos.y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()