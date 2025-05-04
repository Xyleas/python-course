import matplotlib.plot as plt
import seaborn as sns
import pickle

# Load data
with open('iris.pickle', 'rb'):
    iris = pickle.load(f)

# Extract the first column from the data table (get all of the rows)
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
petal_length = iris['data'][:, 2]
petal_width = iris['data'][:, 3]
classes = iris['target']

fig, axes = plt.subplots(2,2)
# matplotlib: axes[0,0].scatter(sepal_length, sepal_width, c=classes)
sns.scatterplot(sepal_length, sepal_width, hue=classes, legend=False, ax=axes[0,0])
axes[0,0].set_xlabel('Sepal length (cm)')
axes[0,0].set_xlabel('Sepal width (cm)')

# Petal length vs petal width
# matplotlib: axes[0,1].scatter(petal_length, petal_width, c=classes)
sns.scatterplot(petal_length, petal_width, hue=classes, legend=False, ax=axes[0,1])
axes[0,1].set_xlabel('Petal length (cm)')
axes[0,1].set_xlabel('Petal width (cm)')

# Bottom-left (2nd row, 1st col): sepal length v. petal length
# matplotlib: axes[1,1].scatter(petal_length, sepal_length, c=classes)
sns.scatterplot(petal_length, sepal_length, hue=classes, legend=False, ax=axes[1,1])
axes[1,1].set_xlabel('Petal length (cm)')
axes[1,1].set_xlabel('Sepal length (cm)')

# Bottom-right (2nd row, 2nd col): sepal width v. petal width
# matplotlib: axes[1,0].scatter(sepal_width, petal_width, c=classes)
sns.scatterplot(sepal_width, petal_width, hue=classes, legend=False, ax=axes[1,0])
axes[1,0].set_xlabel('Sepal width (cm)')
axes[1,0].set_xlabel('Petal width (cm)')

fig.subtitle('Iris dataset')
plt.show()