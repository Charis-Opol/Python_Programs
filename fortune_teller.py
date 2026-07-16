import random
import time

responses = [
    "Today is the perfect day to start something new.",
    "Someone will ask for your help soon.",
    "Your next project will teach you an unexpected lesson.",
    "A bug you're struggling with has a simple solution.",
    "Take a break—your best idea is coming.",
    "Luck is quietly working in your favor.",
    "An opportunity will appear when you least expect it.",
    "The answer you're looking for is simpler than you think."
]

print("Consulting the AI Oracle...")
time.sleep(2)

for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.6)

print("\n")
print(random.choice(responses))