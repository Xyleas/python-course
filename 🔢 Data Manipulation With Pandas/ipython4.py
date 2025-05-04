import pandas as pandas
import numpy as np

flights = pd.read_csv('flights.csv', index_col=False)

# Group flights by month

flights_by_month = flights.groupby('MONTH')
flights_by_month # Python representation

# Fetch all December flights
flights_by_month.get_group(12)

# Total distance travelled by all flights per month
flights_by_month['DISTANCE'].aggregate(np.sum)

# Average distance travelled by all flights per month
flights_by_month['DISTANCE'].aggregate(np.mean)

# Max distance travelled by all flights per month
flights_by_month['DISTANCE'].aggregate(np.max)

# Get the max total distance travelled and the month
flights_by_month['DISTANCE'].aggregate(np.sum).idxmax()

# Get the min total distance travelled and the month
flights_by_month['DISTANCE'].aggregate(np.sum).idxmin()

# Number of cancelled flights per month
flights_by_month['CANCELLED'].aggregate(np.sum)

