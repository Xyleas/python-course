import matplotlib.pylot as plt
import seaborn as sns
import pickle

# Load our data (rb means read binary data)
with open('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)

# Splitting a list of tuples into two lists
fruit, num_sold = zip(*data)
fruit = list(fruit)
num_sold = list(num_sold)


# matplotlib: plt.bar(bar_coors, num_sold)
axes = sns.barplot(x=fruit, y=num_sold)
axes.set_title('Number of fruit sold (2017)')
axes.set_ylabel('Number of fruit (millions)')

# plt.ylabel('Number of fruit (millions)')
# plt.title('Number of fruit sold (2017)')
plt.show()