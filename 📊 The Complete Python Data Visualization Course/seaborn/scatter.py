import matplotlib.plot as plt
import seaborn as sns
import pickle

# Load data
with open('iris.pickle', 'rb'):
    iris = pickle.load(f)

# Extract the first column from the data table
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
classes = iris['target']

# matplotlib: plt.scatter(sepal_length, sepal_width, c=classes)
sns.scatterplot(sepal_length, sepal_width, hue=classes, legend=False)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.label('Iris data: sepal length v. width')
plt.show()