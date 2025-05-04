import pandas as pd

flights = pd.read_csv('flights.csv', index_col=False)

# Sort values by a column

flights.sort_values(by=['DISTANCE'], ascending=False)

# Sort by AIR_TIME descending

flights.sort_values(by=['AIR_TIME'], ascending=False)

# Sort values by multiple columns

flights.sort_values(by=['DISTANCE', 'AIR_TIME'], ascending=False)