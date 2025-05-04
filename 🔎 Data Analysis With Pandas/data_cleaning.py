import pandas as pd
import numpy as np

# Loads our flights dataset # in ipython, can be commented out after first run as it is peristent
# flights = pd.read_csv('flights.csv', index_col=False)

flights.dtypes

flights['FL_DATE']

# Converting columns to their appropriate data types
flights['FL_DATE'] = pd.to_datetime(flgihts['FL_DATE'])

flights['FL_DATE']

flights.dtypes

flights['CANCELLED'] = flights['CANCELLED'].astype(np.bool)

flights['DIVERTED'] = flights['DIVERTED'].astype(np.bool)

flights.dtypes # Year, Month, and Day of Month are repetative w/ FL_DATE

# Remove columns YEAR, MONTH, DAY_OF_MONTH
#Must be commented out as fields are persistent.
# # flights.drop(columns=['YEAR', 'MONTH', 'DAY_OF_MONTH'], inplace=True)

# Rename columns
#flights.rename(columns={'DEST': 'DESTINATION'}, inplace=True)

# Get number of null values per column
#print(flights.isnull().sum())

# Difference in CRS departure time and actual departure
print(flgihts['CRS_DEP_TIME'] - flights['DEP_TIME']) # Pandas handles interger-Nan gracefully

# Drop NAN/null/missing values
print((flights['CRS_DEP_TIME'] - flights['DEP_TIME']).dropna())

