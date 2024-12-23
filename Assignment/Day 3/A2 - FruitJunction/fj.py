import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BASKET_WIDTH = 100
BASKET_HEIGHT = 100
FRUIT_SIZE = 30
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Junction")

# Load background image
background_image = pygame.image.load("images/back.jpg").convert()  # Replace with your background image

# Load fruit images (replace these with your own images)
fruit_images = {
    "apple": pygame.image.load("images/apple.png").convert_alpha(),  # Replace with your apple image
    "banana": pygame.image.load("images/banana.png").convert_alpha(),  # Replace with your banana image
}

# Load basket image (replace with your own image)
basket_image = pygame.image.load("images/basket.png").convert_alpha()  # Replace with your basket image

# Resize fruit images to fit the game
for key in fruit_images:
    fruit_images[key] = pygame.transform.scale(fruit_images[key], (FRUIT_SIZE, FRUIT_SIZE))

# Resize basket image to fit the game
basket_image = pygame.transform.scale(basket_image, (BASKET_WIDTH, BASKET_HEIGHT))

# Basket class
class Basket:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - BASKET_HEIGHT - 10, BASKET_WIDTH, BASKET_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        # Keep the basket within the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - BASKET_WIDTH:
            self.rect.x = SCREEN_WIDTH - BASKET_WIDTH

    def draw(self, surface):
        # Draw the basket using the loaded image
        surface.blit(basket_image, self.rect)

# Fruit class
class Fruit:
    def __init__(self):
        self.type = random.choice(list(fruit_images.keys()))
        self.image = fruit_images[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - FRUIT_SIZE)
        self.rect.y = 0

    def fall(self):
        self.rect.y += 5  # Speed of falling

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Main game loop
def main():
    clock = pygame.time.Clock()
    basket = Basket()
    fruits = []
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket.move(-10)
        if keys[pygame.K_RIGHT]:
            basket.move(10)

        # Add new fruit
        if random.randint(1, 30) == 1:  # Adjust frequency of fruit falling
            fruits.append(Fruit())

        # Update fruit positions
        for fruit in fruits[:]:
            fruit.fall()
            if fruit.rect.y > SCREEN_HEIGHT:
                fruits.remove(fruit)  # Remove fruit if it falls off the screen
            if fruit.rect.colliderect(basket.rect):
                score += 1
                fruits.remove(fruit)  # Remove fruit if caught

        # Drawing
        screen.blit(background_image, (0, 0))  # Draw the background
        basket.draw(screen)
        for fruit in fruits:
            fruit.draw(screen)

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()