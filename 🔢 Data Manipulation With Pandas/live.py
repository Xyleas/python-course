import pandas as pandas

# Read a CSV file
flights = pd.read_csv('flights.csv', index_col=False)

print(flights)
print(flights.columns)
print(flights['DAY_OF_WEEK'])
print(flights['ORIGIN'])
