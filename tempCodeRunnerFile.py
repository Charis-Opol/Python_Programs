

print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        new_fib = prev1 + prev2
        print(new_fib)
        prev1 = prev2
        prev2 = new_fib
        count += 1