import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load data
with open('coding-exp-by-dev-type.pickle', 'rb') as f:
    data = pickle.load(f)

#Test print(data)

# Split into two lists
dev_types, years_exp = zip(*data)
dev_types = list(dev_types)
years_exp = list(years_exp)


# matplotlib: plt.barh(bar_coords, years_exp)
axes = sns.barplot(y=dev_types, x=years_exp)
axes.set_ylabel('Developer Type')
plt.xlabel('years')
plt.title('Years of Coding Experience by Developer Type')
plt.tight_layout()
plt.show()