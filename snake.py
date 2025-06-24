import pygame
# Fenstergröße kleiner machen
WIDTH, HEIGHT = 300, 200
CELL_SIZE = 20
import random
import sys

# Fenstergröße
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Farben
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def random_position():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return (x, y)

def draw_text(screen, text, size, color, pos):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=pos)
    screen.blit(surface, rect)

def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return

def main():
    # Fenstergröße 1.5 mal größer machen
    global WIDTH, HEIGHT
    WIDTH = 600
    HEIGHT = 400

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    # Startbildschirm
    screen.fill(BLACK)
    draw_text(screen, "Snake", 80, GREEN, (WIDTH//2, HEIGHT//2 - 60))
    draw_text(screen, "Zum Starten eine Taste drücken", 48, WHITE, (WIDTH//2, HEIGHT//2 + 40))
    pygame.display.flip()
    wait_for_key()

    while True:
        snake = [(WIDTH // 2, HEIGHT // 2)]
        direction = (0, -CELL_SIZE)
        apple = random_position()
        score = 0
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                        direction = (0, -CELL_SIZE)
                    elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                        direction = (0, CELL_SIZE)
                    elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                        direction = (-CELL_SIZE, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                        direction = (CELL_SIZE, 0)

            # Kopf bewegen
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Kollision prüfen
            if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake):
                game_over = True
                break

            snake.insert(0, new_head)

            # Apfel essen
            if new_head == apple:
                score += 1
                apple = random_position()
                while apple in snake:
                    apple = random_position()
            else:
                snake.pop()

            # Zeichnen
            screen.fill(BLACK)
            for segment in snake:
                pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, RED, (*apple, CELL_SIZE, CELL_SIZE))
            draw_text(screen, f"Score: {score}", 40, WHITE, (80, 30))
            pygame.display.flip()
            clock.tick(10)

        # Game Over Bildschirm
        screen.fill(BLACK)
        draw_text(screen, "Game Over!", 80, RED, (WIDTH//2, HEIGHT//2 - 60))
        draw_text(screen, f"Score: {score}", 48, WHITE, (WIDTH//2, HEIGHT//2 + 10))
        draw_text(screen, "Zum Neustarten eine Taste drücken", 40, WHITE, (WIDTH//2, HEIGHT//2 + 80))
        pygame.display.flip()
        wait_for_key()
