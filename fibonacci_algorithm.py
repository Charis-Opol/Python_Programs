prev_number1 = 0
prev_number2 = 1

for i in range (0, 18):
    new_fibonacci = prev_number1 + prev_number2
    print(new_fibonacci)
    prev_number1 = prev_number2
    prev_number2 = new_fibonacci

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
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(0, 1)

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)
print(F(19))