import matplotlib.pyplot as plt
import pickle

# Load data
with open('coding-exp-by-dev-type.pickle', 'rb') as f:
    data = pickle.load(f)

#Test print(data)

# Split into two lists
dev_types, years_exp = zip(*data)

bar_coords = range(len(dev_types))

plt.barh(bar_coords, years_exp)
plt.xlabel('years')
plt.title('Years of Coding Experience by Developer Type')
plt.yticks(bar_coords, dev_types, fontsize=8)
plt.tight_layout()
plt.show()