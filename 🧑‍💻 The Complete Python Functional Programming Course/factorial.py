def factorial(n):
    if n ==1:
        return 1
    else:
        return n* factorial(n-1)

result = factorial(5)
print(result)

'''
5*factorial(4)
4*factorial(3)
3*factorial(2)
2*factorial(1)
1*factorial(0) =>
0*factorial(-1)
0*factorial(-1)
'''