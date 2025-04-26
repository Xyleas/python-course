import functools
import time

# Example 1 - Partial
def power(number, exponent):
    return number**exponent

square_2=power(2,2)
square_4=power(4,2)
square_5=power(5,2)

square = functools.partial(power, exponent = 2)
square_6 = square(6) # Power(6,2) because we square

cube = functools.partial(power, exponent=3)
cube_6 = cube(6)
print(square_6)
print(cube_6)
 
cube_2 = power(2,2)
cube_4 = power(4,2)
cube_6 = power(6,2)

# Example 2 - Caching
@functools.lru_cache(maxsize=3) # Store the result of the last 3 function calls.
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

start_time = time.time()
factorial(100)
end_time = time.time()
print("Elapsed Time= ", end_time-start_time)
start_time = time.time()
factorial(100)
end_time = time.time()
print("Elapsed Time= ", end_time-start_time)
