## Example 1

numbersdoubled = []
for i in numbers:
    doubled.append(i * 2)
doubled = [i*2 for i in numbers if i >=5]
print("Doubled with comprehension: ", doubled)

## Example 2

numbers=range(1,11)
odd_numbers =[]
for i in numbers:
    if i % 2 != 0:
        odd_numbers.append(i)

odd_numbers = [i for i in numbers if i%2!=0]
print("Odd numbers with comprehension: ", odd_numbers)

## Example 3

exam_scores = [85, 72, 90, 60, 45, 78, 82]

# Threshold for passing score
passing_threshold = 70

# Using list comprehension to filter scores above threshold
passing_scores = [score for score in exam_scores if score >= passing_threshold]
print("Passing scores with comprehension: ", passing_scores)

## Example 4
list1 = [1,2,3]
list2 = [5,6,7]
products = []
for x in list2:
    for y in list2:
        products.append(x*y)

products = [x*y for x in list1 for y in list2]
print("Products using comprehension ", products)
# Output
# 1*5, 1*6, 1*7, 2*5, 2*6, 2*7, 3*5, 3*6, 3*7
# => 5,6,7,10,12,13,14,15,18,21

