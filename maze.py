import pygame
import random
import sys
from time import sleep

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 20, 20
CELL_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FPS = 60

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator and Solver")
clock = pygame.time.Clock()

# Maze grid setup
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
stack = []

# Directions for DFS (right, left, down, up)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Player position
player_pos = [0, 0]

def generate_maze(x, y):
    visited[y][x] = True
    stack.append((x, y))

    while stack:
        x, y = stack[-1]
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and not visited[ny][nx]:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            grid[(ny + y) // 2][(nx + x) // 2] = 1
            visited[ny][nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()

def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            color = WHITE if grid[y][x] == 1 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    # Draw goal
    pygame.draw.rect(screen, GREEN, ((COLS - 1) * CELL_SIZE, (ROWS - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_player(dx, dy):
    x, y = player_pos
    nx, ny = x + dx, y + dy
    if 0 <= nx < COLS and 0 <= ny < ROWS and grid[ny][nx] == 1:
        player_pos[0], player_pos[1] = nx, ny

def main():
    generate_maze(0, 0)
    grid[0][0] = 1
    grid[ROWS - 1][COLS - 1] = 1

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(BLACK)
        draw_maze()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move_player(0, -1)
                if event.key == pygame.K_s:
                    move_player(0, 1)
                if event.key == pygame.K_a:
                    move_player(-1, 0)
                if event.key == pygame.K_d:
                    move_player(1, 0)

        # Check for win
        if player_pos == [COLS - 1, ROWS - 1]:
            print("🎉 YOU WON! 🎉")
            sleep(2)
            running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
