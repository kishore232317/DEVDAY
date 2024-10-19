import pygame
import sys
import random

# Initialize the pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
PACMAN_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the Pac-Man class
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.color = YELLOW
        self.direction = "RIGHT"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + BLOCK_SIZE // 2, self.y + BLOCK_SIZE // 2), BLOCK_SIZE // 2)

    def move(self):
        if self.direction == "RIGHT":
            self.x += PACMAN_SPEED
        elif self.direction == "LEFT":
            self.x -= PACMAN_SPEED
        elif self.direction == "UP":
            self.y -= PACMAN_SPEED
        elif self.direction == "DOWN":
            self.y += PACMAN_SPEED

        # Wrap around the screen edges
        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

# Define the Ghost class
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.color = RED

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Define the main game loop
def game_loop():
    pacman = Pacman(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ghost = Ghost(random.randint(0, SCREEN_WIDTH - BLOCK_SIZE), random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE))
    clock = pygame.time.Clock()

    # Main game loop
    while True:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pacman.direction = "RIGHT"
                if event.key == pygame.K_LEFT:
                    pacman.direction = "LEFT"
                if event.key == pygame.K_UP:
                    pacman.direction = "UP"
                if event.key == pygame.K_DOWN:
                    pacman.direction = "DOWN"

        # Move Pac-Man
        pacman.move()

        # Draw Pac-Man and Ghost
        pacman.draw(screen)
        ghost.draw(screen)

        # Collision detection between Pac-Man and Ghost
        if abs(pacman.x - ghost.x) < BLOCK_SIZE and abs(pacman.y - ghost.y) < BLOCK_SIZE:
            print("Pac-Man was caught by a ghost! Game Over.")
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    game_loop()
