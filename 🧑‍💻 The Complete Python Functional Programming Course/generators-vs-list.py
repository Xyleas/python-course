import time
import sys
import random

# Function to generate a list of random numbers using a list
def generate_random_numbers_list(n):
    return [random.randint(1,100) for _ in range(n)]

# Function to generate random numbers using a generator
def generate_random_numbers_generator(n):
    for _ in range(n):
        yield random.randint(1,100)

# Measure time and memory usage for generating a list of random numbers
start_time_list = time.time()
random_numbers_list = generate_random_number_list
end_time_list = time.time()
memory_usage_list = sys.getsizeof(random_numbers_list)

# Measure time and memory usage for generating a random list of numbers using a generator
start_time_generator = time.time()
random_numbers_list = generate_random_numbers_generator
end_time_generator = time.time()
memory_usage_list = sys.getsizeof(random_numbers_generator)

# Calculate time taken
time_taken_list = end_time_list - start_time_list
time_taken_generator = end_time_generator - start_time_generator