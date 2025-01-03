compnum = 50
guess = int (input("I am thinkng if a number, Can you guess the number: "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Have another guess: "))
    count= count + 1
print(f"Well done it took you {count} attempts")