import time
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_tree():
    tree = [
        "        *        ",
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "*****************",
        "       |||       ",
        "       |||       "
    ]
    return tree

def add_lights(tree):
    symbols = ['o', '@', '*', '+']
    lit_tree = []
    for line in tree:
        new_line = "".join(random.choice(symbols) if c == '*' else c for c in line)
        lit_tree.append(new_line)
    return lit_tree

def display_tree():
    tree = generate_tree()
    while True:
        clear_screen()
        lit_tree = add_lights(tree)
        for line in lit_tree:
            print(line)
        time.sleep(0.5)

if __name__ == "__main__":
    display_tree()
