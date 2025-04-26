## Example 1 (MAP)
numbers = list(range(1,6))
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers) # Ouptut: [2,4,6,8,10]

squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers using map ", squared_numbers)

## Example 2 (FILTER)
even_numbers = []

# Use a for loop to iterate over the numbers and 
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

even_numbers = list(filter(lambda x: x%2==0, numbers))
print("Even numbers with filter: ", even_numbers)