# Recursion

# 1 + 2 + 3 + 4 + 5
def sum_of_natural_numbers_iterative(n):
    sum = n
    while n > 0:
        n -= 1
        sum += n
    return sum

def sum_of_natural_numbers_recursive(n):
    if n == 1:
        return n # Base case
    else:
        return n + sum_of_natural_numbers(n-1)

print(sum_of_natural_numbers_iterative(5))
print(sum_of_natural_numbers_recursive(5))

# Fibonacci Sequence
# 0, 1, 2, 3, 5, 8, 13, 21...
# F(0) = 0
# F(1) = 1
# n > 1, F(n) = F(n - 1) + F(n - 2)

# F(3) = F(2) + F(1)
# F(2) = 1
# F(3) = 1 + 1  = 2

def fibonacci(n):
    if n <= 0:
        return n
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(3)
print(result)

# Challenge: Use recursion to calculate the factorial.
# 3! = 1 * 2 * 3
# 5! = 1 * 2 * 3 * 4 * 5

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)