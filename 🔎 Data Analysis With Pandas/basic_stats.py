import pandas as pd

# Load the flights dataset
#flights = pd.read_csv('flights.csv', index_col=False)

# Get basic statistics for the dataframe
print(flights.describe())

# Compute the mean and standard deviation for the DISTANCE column
print(flights['DISTANCE'].mean())
print(flights['DISTANCE'].std())

# Mean of the difference of the CRS departure and the actual departure
print((flights['CRS_DEP_TIME'] - flights['DEP_TIME']).mean())