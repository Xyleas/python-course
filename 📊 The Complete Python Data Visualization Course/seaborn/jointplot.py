import matplotlib.plot as plt
import seaborn as sns
import pickle

# Load data
with open('iris.pickle', 'rb'):
    iris = pickle.load(f)

# Extract the first column from the data table (get all of the rows)
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
classes = iris['target']

# scatter, reg (line of best fit), kde (density), hex (density in hexagons)
axes = sns.jointplot(sepal_length, sepal_width, kind='kde') # Reg attempts to add a line of best fit, Kde gives a density graph
axes.set_axis_labels('Sepal Length (cm)', 'Sepal Width (cm)')
plt.show() #  A scatter plot w/ histograms on the outer axes.
