import pygame
import random

# Initialize the game
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the snake
snake_size = 20
snake_speed = 10
snake_x = width // 2
snake_y = height // 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1

# Define the food
food_x = round(random.randrange(0, width - snake_size) / 20) * 20
food_y = round(random.randrange(0, height - snake_size) / 20) * 20

# Define the game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_size
                snake_x_change = 0

    # Update the snake's position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Draw the snake and food
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, [food_x, food_y, snake_size, snake_size])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_body.append(snake_head)
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_size) / 20) * 20
        food_y = round(random.randrange(0, height - snake_size) / 20) * 20
        snake_length += 1

    # Check for collision with the snake's body
    for segment in snake_body[:-1]:
        if segment == snake_head:
            running = False

    # Draw the snake's body
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_size, snake_size])

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
