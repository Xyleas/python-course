import pandas as pd

flights = pd.read_csv('flights.csv', index_col=False)

flights

# Things are typically evaluated using a boolean operator

# Fetch all January Flights
flights['MONTH'] == 1 # Retunrs booleans
flights[flights['MONTH'] == 1] # Return values

# Fetch all flights that happened on the first of the month
flights[flights['DAY_OF_MONTH'] == 1]

# Fetch all flgihts leaving New York
flights[flights['ORIGIN_STATE_NM'] == 'New York']

long_flights = flights[flights['Distance'] > 4000]
long_flights

long_flights[long_flights['ORIGIN_STATE_NM'] == 'Hawaii']

long_flights[(long_flights['ORIGIN_STATE_NM'] == 'Hawaii') | (long_flights['DEST_STATE_NM'] == 'Hawaii')]

# Long flights in January

flights[(flights['DISTANCE'] > 4000) & (flights['MONTH'] == 1)]

# Long flights not in January
flights[(flights['DISTANCE'] > 4000) & ~(flights['MONTH'] == 1)]