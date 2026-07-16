import random
import shutil
import time
import os

chars = "アイウエオカキクケコサシスセソABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

width = shutil.get_terminal_size().columns

try:
    while True:
        line = ""
        for _ in range(width):
            if random.random() > 0.93:
                line += random.choice(chars)
            else:
                line += " "
        print(line)
        time.sleep(0.05)
except KeyboardInterrupt:
    os.system("cls" if os.name == "nt" else "clear")
    print("Exited Matrix.")