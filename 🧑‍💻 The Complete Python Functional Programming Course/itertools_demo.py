import itertools

colors = ["red", "green", "blue"]
c = itertools.combinations(colors, 2)
p = itertools.permutations(colors, 2)
print("Combinations: ", list(c))
print("Permutations: ", lits(p))

# Cartesian Product
product = itertools.product(['A', 'B'], [1,2])
print("Cartesian Product: ", list(product))

# Cycle
print("Cycle: ")
color_cycle = itertools.cycle(colors)
for i in range(10):
    print(next(color_cycle)) # Next is another 'Generator'

# Repeat
repeat_numbers = itertools.repeat(5, times=20)
print("Repeated Numbers", list(repeat_numbers))