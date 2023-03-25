import pygame
import random

# Initialize Pygame
pygame.init()

# Define the game window size
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define the game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (50, WINDOW_HEIGHT / 2)
        self.speed = 5

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

# Define the obstacle sprite
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH
        self.rect.y = random.randrange(WINDOW_HEIGHT - self.rect.height)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

# Create a group for the obstacles
obstacles = pygame.sprite.Group()

# Define the game loop
def main():
    # Create the player character
    player = Player()

    # Set the game clock
    clock = pygame.time.Clock()

    # Set the initial score
    score = 0

    # Set the initial game over state
    game_over = False

    # Game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()
                elif event.key == pygame.K_DOWN:
                    player.move_down()

        # Create a new obstacle at random intervals
        if random.randrange(100) < 2:
            obstacle = Obstacle()
            obstacles.add(obstacle)

        # Update the player and obstacles
        player_rect = player.rect
        obstacles.update()

        # Check for collisions between the player and obstacles
        if pygame.sprite.spritecollide(player, obstacles, False):
            game_over = True

        # Draw the game objects
        WINDOW.fill(BLACK)
        WINDOW.blit(player.image, player.rect)
        obstacles.draw(WINDOW)

        # Display the score
        score += 1
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, WHITE)
        WINDOW.blit(text, (10, 10))

        # Update the display
        pygame.display.update()

        # Set the game clock tick rate
        clock.tick(60)

    # Quit Pygame when the game is over
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
