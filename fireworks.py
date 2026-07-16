import random
import os
import time

WIDTH = 80
HEIGHT = 25

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    screen = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    x = random.randint(10, WIDTH - 10)
    y = random.randint(5, HEIGHT - 5)

    for angle in range(0, 360, 20):
        r = random.randint(2, 8)

        dx = int(r * __import__("math").cos(__import__("math").radians(angle)))
        dy = int(r * __import__("math").sin(__import__("math").radians(angle)))

        if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT:
            screen[y + dy][x + dx] = random.choice("*+xo@#")

    clear()

    for row in screen:
        print("".join(row))

    time.sleep(0.4)