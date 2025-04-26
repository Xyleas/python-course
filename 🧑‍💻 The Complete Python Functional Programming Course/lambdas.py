# Example 1
def f(x):
    return x *2

g = lambda x: x *2
print("g(x)=", g(5))

h = lambda x,y: x**y
print(h(5,2))

# Example 2
def return_calculation(operation):
    if operation == "add":
        return lambda a,b: a+b
    elif operation == "subtract":
        return lambda a,b: a-b

calculate_add = return_calculation("add")
print(calculate_add(2,3))
calculate_subtract = return_calculation("subtract")
print(calculate_subtract(5,3))