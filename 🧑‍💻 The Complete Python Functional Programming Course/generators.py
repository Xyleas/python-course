import random

def random_numbers(n):
    for _ in range(n):
        yield random.randit(1,1000000) # Yield is like a return but can be done whenever we want

rand_gen = random_numbers(1000000)
print(next(rand_gen))
print(next(rand_gen))
print(next(rand_gen))
print(next(rand_gen))