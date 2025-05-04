import pandas as pandas

flights = pd.read_csv('flights.csv', index_col=False)

# View the first and last few rows and columns

flights

# Selecting a column

flights['ORIGIN']

# Select multiple columns (origin and destination airports)

flights[['ORIGIN', 'DEST']]

# Select the first few rows
flights[:3]

# Select a row and column entry in the DataFrame

flight.iloc[0,0]

# Selecting the 3rd row and 2nd col
flight.iloc[2,1]

# Mixing the row indices with string column names
flights.iloc[2, flights.columns.get_loc('DAY_OF_MONTH')]

flights.iloc[:3, flights.columns.get_loc('DAY_OF_MONTH')]
flights.iloc[0, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]]

flights.iloc[:3, [flights.columns.get_loc('ORIGIN'), flights.columns.get_loc('DEST')]]

