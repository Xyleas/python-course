from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.layouts import row, column, gridplot
from bokeh.palettes import Dark2_5 as palette
import pickle

output_file('multiplot.html')

# Load data
with open('iris.pickle', 'rb'):
    iris = pickle.load(f)

# load all features for all classes
sepal_length = iris['data'][:, 0]
sepal_width = iris['data'][:, 1]
petal_length = iris['data'][:, 2]
petal_width = iris['data'][:, 3]
classes = iris['target']

# separate features via class
setosa_sepal_length = sepal_length[classes == 0]
setosa_sepal_width = sepal_width[classes == 0]
setosa_petal_length = sepal_length[classes == 0]
setosa_petal_width = sepal_width[classes == 0]

versicolor_sepal_length = sepal_length[classes == 1]
versicolor_sepal_width = sepal_width[classes == 1]
versicolor_petal_length = sepal_length[classes == 1]
versicolor_petal_width = sepal_width[classes == 1]

virginica_sepal_length = sepal_length[classes == 2]
virginica_sepal_width = sepal_width[classes == 2]
virginica_petal_length = sepal_length[classes == 2]
virginica_petal_width = sepal_width[classes == 2]

fig1 = figure(x_axis_label='Sepal length (cm)', y_axis_label='Sepal width (cm)')
fig1.circle(setosa_sepal_length, setosa_sepal_width, color=palette[0], legend='setosa')
fig1.circle(versicolor_sepal_length, versicolor_sepal_width, color=palette[1], legend='versicolor')
fig1.circle(virginica_sepal_length, virginica_sepal_width, color=palette[2], legend='verginica')

fig2 = figure(x_axis_label='Petal length (cm)', y_axis_label='Petal width (cm)', x_range=fig1.x_range) # x_range is bound to the x range of fig1
fig2.circle(setosa_petal_length, setosa_petal_width, color=palette[0], legend='setosa')
fig2.circle(versicolor_petal_length, versicolor_petal_width, color=palette[1], legend='versicolor')
fig2.circle(virginica_petal_length, virginica_petal_width, color=palette[2], legend='verginica')

show(column([fig1, fig2]))