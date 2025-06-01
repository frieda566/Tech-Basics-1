import pygame
import random
import math

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 150, 200)
NUM_FISH = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Animated Fish')
clock = pygame.time.Clock()

# Load image
original_image = pygame.image.load("fish.png").convert_alpha()
original_image = pygame.transform.scale(original_image, (80, 80))


class Fish:
    def __init__(self):
        # Random starting position
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)

        # Random speed and direction
        self.speed_x = random.uniform(1, 4)
        self.speed_y = random.uniform(-1, 1)

        # Random movement pattern
        self.pattern = random.choice(['linear', 'sine', 'circle'])

        # Random tint color
        self.color_tint = (
            random.randint(0, 100),
            random.randint(100, 255),
            random.randint(100, 255)
        )

        # Generate tinted image
        self.image = original_image.copy()
        tint_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(self.color_tint + (0,))
        self.image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        # Circle movement setup
        self.angle = random.uniform(0, math.pi * 2) # Random angle in full circle
        self.radius = random.randint(30, 100)
        self.center_x = self.x
        self.center_y = self.y

    def update(self):
        if self.pattern == 'linear':
            self.x += self.speed_x
            self.y += self.speed_y
        elif self.pattern == 'sine': # "Wave" like motion
            self.x += self.speed_x
            self.y = self.center_y + math.sin(self.x * 0.05) * 30
        elif self.pattern == 'circle':
            self.angle += 0.05
            self.x = self.center_x + math.cos(self.angle) * self.radius
            self.y = self.center_y + math.sin(self.angle) * self.radius

        # Wrap around screen - reappearing fish
        if self.x > SCREEN_WIDTH: self.x = 0
        if self.x < 0: self.x = SCREEN_WIDTH
        if self.y > SCREEN_HEIGHT: self.y = 0
        if self.y < 0: self.y = SCREEN_HEIGHT

    def draw(self, surface):
        surface.blit(self.image, (int(self.x), int(self.y)))


# Create multiple fish
fishes = [Fish() for _ in range(NUM_FISH)]

# Main
running = True
while running:
    clock.tick(60)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw all fish
    for fish in fishes:
        fish.update()
        fish.draw(screen)

    pygame.display.flip()

pygame.quit()
exit()