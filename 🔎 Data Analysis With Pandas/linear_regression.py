import pandas as pandas
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the flight dataset
#flights = pd.read_csv('flights.csv', index_col=False)

#flights_subsample = flights.sample(1000)

# Plot the data
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])
plt.show()

# The data is very x-y positively correlated.

# Perform linear regression
slope, intercept, r_value, _, _ = linregress(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME']) # Underscore to repesent varaibles we don't care about.
print('y = {}x + {}; r={}'.format(slope,intercept, r_value))

# Plot the data (again)
plt.scatter(flights_subsample['DISTANCE'], flights_subsample['CRS_ELAPSED_TIME'])

# Generate some X values to feed into the line
x = np.linspace(flights_subsample['DISTANCE'].min(), flights_subsample['DISTANCE'].max(), 1000)
# Calculate the y values using the learned slope and intercept
y = slope * x + intercept
plt.plot(x,y, 'r--')
plt.show()

# Use learned slope and intercept for prediction:
distance = 5000
flight_time = slope * distance + intercept
print(flight_time)
