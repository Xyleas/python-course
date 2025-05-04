import matplotlib.plot as plt
import pickle

# Load data
with open('iris.pickle', 'rb'):
    iris = pickle.load(f)

#Test print(iris)

# Extract the first column from the data table
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
classes = iris['target']

plt.scatter(sepal_length, sepal_width, c=classes)
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.label('Iris data: sepal length v. width')
plt.show()