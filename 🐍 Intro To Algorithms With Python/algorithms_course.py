import timeit
import random

# Linear Search

def linear_search(array, target):

    for i in range(len(array)):
        if array[i] == target:
            return i

    return -1

test = range(1000000)
print(linear_search(test, 99999)) # Prints 99999
print(linear_search(test, -999))

test2 = [1,5,7,9,0,55,63]
print(linear_search(test2, 7))

# Binary Search

l = [1,2,3,4,5,6,7,8, 9, 10, 11, 12]
# [1,2,3,4,5,6]
# [1,2,3]

def binary_search(array, target):
    
    left = 0
    right = len(array) - 1
    mid = (left + right)//2

    while left <= right:
        if array[mid] == target: # If the target is found
            return mid
        elif target > array[mid]:
            left = mid + 1
        elif target < array[mid]:
            right = mid - 1

        mid = (left + right)//2

    return -1

sorted_list = list(range(100000))

# Test cases
target = random.randint(0, 99999)

linear_time = timeit.timeit(lambda: linear_search(sorted_list, target), number=100)
binary_time = timeit.timeit(lambda: binary_search(sorted_list, target), number=100)

print(f"Linear search execution time: {linear_time:.6f} seconds.")
print(f"Binary search execution time: {binary_time:.6f} seconds.")

# Bubble Sort
l = [5,9,3,6]
# [ 5,3,9,6]
# [5,3,6,9]
# [3,5,6,9]

def bubble_sort(array):
    n = len(array)

    for i in range(n):

        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

    return array

sorted_list = bubble_sort(l)
print("Sorted array: ", sorted_list)
print(bubble_sort(l))
l = [56, 3, 999, 2, 869, 78, 2, 2, 3, 5, 5, 5]
print(bubble_sort(l))

# Insertion Sort
l = [3,5,8,4,2]
# [3,4,5,8,2]
# [2,3,4,5,8]

def insertion_sort(array):
    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1
        while j >= 0 and current_element < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j + 1] = current_element

    return array

sorted_list = insertion_sort(l)
print("Insertion sort: ", sorted_list)

unsorted_list = [random.randint(1,1000) for n in range(10000)]

bubble_sort_time = timeit.timeit(lambda: bubble_sort(unsorted_list.copy()), number=1)
insertion_sort_time = timeit.timeit(lambda: insertion_sort(unsorted_list), number=100)

print(f"Bubble sort time: {bubble_sort_time:.6f} seconds")
print(f"Insertion sort time: {insertion_sort_time:.6f} seconds")

# Challenge
# Combine a sorting algorithm with  binary search in a function to ensure that binary search can run on any input list.
# Then, run a timed test of your function alongside linear search.
# What can we learn from this about algorithm complexity trade-offs?

def sort_and_search(array, target):
    sorted_array = bubble_sort(array)
    return binary_search(sorted_array, target)

# Solution

def binary_search_sorted(array, target):
    array = insertion_sort(array)
    result = binary_search(array, target)
    return result

unsorted_list = [random.randint(1,1000) for n in range(10000)]
target = random.randint(1,1000)

binary_time = timeit.timeit(lambda: binary_search(unsorted_list.copy(), target), number=1)
linear_time = timeit.timeit(lambda: linear_search(unsorted_list.copy(), target), number=1)

print(f"Binary search (with sorting): {binary_time:.6f} seconds")
print(f"Linear search: {linear_time:.6f} seconds")

# Binary w/ sorting: 2.907489
# Linear 0.000250
# Linear is faster, as we don't have to rely on sorting the data.