import pandas as pandas
import numpy as np

# Load the flights dataset
#flights = pd.read_csv('flights.csv', index_col=False)

# Load the mapping CSV file (mapping from Integer => Day of Week)
#days_of_week = pd.read_csv('L_WEEKDAYS.csv', index_col=False)

flights['DAY_OF_WEEK']

merged = pd.merge(flights, days_of_week, left_on='DAY_OF_WEEK', right_on='CODE')

merged.columns()
merged

# Remove the DAY_OF_WEEK and Code columns (inplace = True)
#merged.drop(columns=['DAY_OF_WEEK', 'CODE'], inplace=True)
# Rename Description -> DAY_OF_WEEK
#merged.rename(columns={'Description': 'DAY_OF_WEEK'}, inplace=True)
merged.head()