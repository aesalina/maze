import sys
import pygame
import random
import algorithm_De

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабиринт")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Размеры клеток и лабиринта
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Генерация случайного лабиринта
def create_maze():
    maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    back_field = [['' for _ in range(COLS)] for _ in range(ROWS)]



    stack = [(0, 0)]
    while stack:
        current_cell = stack[-1]
        x, y = current_cell

        maze[y][x] = 1


        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)


        found = False
        for nx, ny in neighbors:
            if 0 <= nx < COLS and 0 <= ny < ROWS and maze[ny][nx] == 0:
                stack.append((nx, ny))
                maze[(y + ny) // 2][(x + nx) // 2] = 1
                found = True
                break

        if not found:
            stack.pop()

    return maze

maze_grid = create_maze()

# Отрисовка лабиринта
def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            if maze_grid[y][x] == 1:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_maze()
    pygame.display.flip()