'''
Pure vs Impure Functions
1. Self-Contained
2. No side-effects
'''

pi = 3.14159265359 # Global variable
area = 0
def area_of_circle(p, radius):
    result = p * (radius ** 2)
    return result

area = area_of_circle(pi, 5)
print("Area of circle is ", area)