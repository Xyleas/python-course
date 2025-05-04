import pandas as pandas
import numpy as np

# Load the flights dataset
#flights = pd.read_csv('flights.csv', index_col=False)

# Plot a histogram of expected CRS departure times
flights['CRS_DEP_TIME'].hist()

# Plot a histogram of CRS arrival times
flights['CRS_ARR_TIME'].hist()

# Plot average distance that flights travel by month
flights_by_month = flights.groupby('MONTH')
flights_by_month['DISTANCE'].aggregate(np.mean).plot()

# Plot average distance that flights travel by day of the week
flights_by_day_of_week = flights.groupby('DAY_OF_WEEK')
flights_by_day_of_week['DISTANCE'].aggregate(np.mean).plot()