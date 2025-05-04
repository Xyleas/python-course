import matplotlib.pylot as plt
import pickle

# Load our data (rb means read binary data)
with open('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)

# Splitting a list of tuples into two lists
fruit, num_sold = zip(*data)

# matplotlub: plt.bar(bar_coords, num_sold)
plt.ylabel('Number of fruit (millions)')
plt.title('Number of fruit sold (2017)')
plt.show()