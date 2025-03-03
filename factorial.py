def factorial(n):
    product = n
    for i in range (1, n):
        product = product * (n - i)
    return product

print(factorial(5))


def factorial_recursion(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n - 1)
    
print(factorial_recursion(5))