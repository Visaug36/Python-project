# Ball Eater Game

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))

# Game title
pygame.display.set_caption("Ball Eater Game")

# Colors
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Black = (0, 0, 0)  # For score text

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player ball properties
Player_x = Width // 2
Player_y = Height // 2
player_radius = 20
Player_speed = 5

# Score
score = 0

# List to store smaller balls
small_balls = []
for _ in range(10):
    x = random.randint(0, Width)
    y = random.randint(0, Height)
    radius = random.randint(5, 15)
    small_balls.append({"x": x, "y": y, "radius": radius})

# Font for score
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Player_y -= Player_speed
    if keys[pygame.K_DOWN]:
        Player_y += Player_speed
    if keys[pygame.K_LEFT]:
        Player_x -= Player_speed
    if keys[pygame.K_RIGHT]:
        Player_x += Player_speed

    # Prevent player ball from leaving the screen
    Player_x = max(player_radius, min(Width - player_radius, Player_x))
    Player_y = max(player_radius, min(Height - player_radius, Player_y))

    # Check for collisions with small balls
    for ball in small_balls[:]:
        distance = ((Player_x - ball["x"])**2 + (Player_y - ball["y"])**2)**0.5
        if distance < player_radius + ball["radius"]:
            player_radius += 2  # Grow the player ball
            score += 1  # Increase the score
            small_balls.remove(ball)  # Remove eaten ball

    # Respawn balls if needed
    if len(small_balls) < 10:
        x = random.randint(0, Width)
        y = random.randint(0, Height)
        radius = random.randint(5, 15)  # Fixed typo from `randit`
        small_balls.append({"x": x, "y": y, "radius": radius})

    # Clear the screen
    screen.fill(White)

    # Draw player ball
    pygame.draw.circle(screen, Green, (Player_x, Player_y), player_radius)

    # Draw small balls
    for ball in small_balls:
        pygame.draw.circle(screen, Red, (ball["x"], ball["y"]), ball["radius"])  # Fixed `y` coordinate issue

    # Display the score
    score_text = font.render(f"Score: {score}", True, Black)
    screen.blit(score_text, (10, 10))  # Display score at the top-left corner

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

pygame.quit()