import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Drawing Example")

# Colors (RGB format)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white (background color)
    screen.fill(white)

    # Draw a blue rectangle
    pygame.draw.rect(screen, blue, (1, 1, 200, 100))  # (x, y, width, height)

    # Draw a red circle
    pygame.draw.circle(screen, red, (400, 300), 50)       # (center_x, center_y), radius

    # Draw a green line
    pygame.draw.line(screen, green, (100, 500), (700, 500), 5)  # (start_x, start_y), (end_x, end_y), width

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
