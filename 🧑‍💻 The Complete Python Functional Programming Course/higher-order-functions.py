def square(x):
    return x**2

def make_half(x):
    return x/2

def process_list(func, list):
    result = []
    for item in list:
        result.append(func(item))
    return result

numbers = [1,2,3,4,5]
squared_numbers = process_list(square, numbers)
print(squared_numbers)
halved_numbers = process_list(make_half, numbers)
print(halved_numbers)

def is_odd(x):
    return x%2 !=0

def is_even(x):
    return x%2 ==0

def filter_function(list, condition):
    result = []
    for x in list:
        if condition(x):
            result.append(x)
    return result

arr = [1,2,3,4,5,6,7,8]

result_odd = filter_function(arr, is_odd)
print(result_odd)

def return_calculation(operation):
    def add(a,b):
        return a + b
    def subtract(a,b):
        return a - b 
    if operation=="add":
        return add
    elif operation=="subtract":
        return subtract

calculate_addition   = return_calculation("add")
print(calculate_addition(5,7))

calculate_subtraction = return_calcuation("subtract")
print(calculate_subtraction(7,10))