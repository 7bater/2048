import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (*pos, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

def random_food():
    x = random.randrange(0, WIDTH, CELL_SIZE)
    y = random.randrange(0, HEIGHT, CELL_SIZE)
    return (x, y)

def main():
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (CELL_SIZE, 0)
    food = random_food()
    score = 0

    while True:
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

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            break  

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = random_food()
            while food in snake:
                food = random_food()
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        score_text = font.render(f"Punkte: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(10)

    screen.fill(BLACK)
    msg = font.render("Game Over!", True, RED)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - msg.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == "__main__":
    main()