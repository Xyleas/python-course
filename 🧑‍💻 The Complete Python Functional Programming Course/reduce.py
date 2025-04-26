from functools import reduce

# Example 1
letters = ["p", "y", "t", "h", "o", "n"]
word = reduce(lambda x,y: x+y, letters, "") # Initial value wasn't essential
print(word)
'''
x   y
["p", "y", "t", "h", "o", "n"] -> ["py", "t", "h", "o", "n"] -> ["pyt", "h", "o", "n"] -> ...
'''
# Example 2
numbers = [5,4,3,2,1]
factorial = reduce(lambda x,y: x*y, numbers, 1) # Passing initial value
print(factorial)
# [1,5,4,3,2,1]

# Example 3 (sum of all prices with 15% tax)
prices = [10.99, 24.50, 8.75, 15.25]
total_cost = reduce(lambda total, price: price+price*0.15+total, prices, 0) # 0 Is needed in this one.
'''
total price
[0 [10.99, 24.50, 8.75, 15.25]
24.50 + 24.50*0.15+10.99
0 +10.99+10.99*0.15
'''