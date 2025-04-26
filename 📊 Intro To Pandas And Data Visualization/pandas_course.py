import numpy as np
import pandas as pd

# Series
data_series = np.random.normal(0,1,100)
p_series = pd.Series(data_series)

print(p_series.head())
print(p_series.tail())

data_series_2 = np.random.normal(0,5,100)

frame = {'column1': data_series,
        'column2': data_series_2}

df = pd.DataFrame(frame)

print(df)

student_ids = [n for n in range(200, 220)]
math_scores = np.random.normal(70, 10, 20)
english_scores = np.random.normal(65, 8, 20)
history_scores = np.random.normal(80, 7, 20)

df = pd.DataFrame({
    'Student ID ': student_ids,
    'Math': math_scores,
    'English': english_scores,
    'History': history_scores
})

#print(df)

# print("Math scores: ", df['Math'])
# print(df.head())
# print(df.tail())
# print(df.describe())

# #print("Sorted by Math: ", df.sort_values(by='Math'))
# print("Sorted by English: ", df.sort_values(by='English'))
# print("Sorted by History: ", df.sort_values(by='History'))
# print("Rows 5-10: ", df.loc[5:10]) 
# print("Rows 5-10, Only Math and English: ", df.loc[5:10, ['Math', 'English']])
# print(".iloc version: ", df.iloc[5:10, 1:3])

#print(df[(df['Math'] > 75) & (df['English'] < 60)])

df['Total'] = df['Math'] + df['English'] + df['History']
print(df)

df.drop(columns = 'Total', inplace=True)
print(df)

data =  {
    'A': [1,2, np.nan, 4,5],
    'B': [np.nan, 2,3,4,5],
    'C': [1,2,3,np.nan, np.nan]
}

df = pd.DataFrame(data)
print(df.isna())
df_dropped = df.dropna()
print(df_dropped)

df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

df_filled = df.fillna(0)
print(df_filled)

df = pd.concat([df, df.iloc[2]])
print(df)

df_no_duplicates = df.drop_duplicates
print(df_no_duplicates)

# map()
def categorize(value):
    if pd.isna(value):
        return 'Missing'
    elif value < 3:
        return 'Low'
    else:
        return 'High'
df['B'] = df['B'].map(categorize)
print(df)

data = {
    'School' : ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Student ID' : [1001,1002,1003,1004,1005,1006,1007],
    'Math' : np.random.randint(60,100,8),
    'English' : np.random.randint(70,100,8),
    'History' : np.random.randint(50,100,8)
}

df = pd.DataFrame(data)
print(df)

grouped = df.groupby('School')
print(grouped)
#print('Mean scores by School: ')
#print(grouped.mean())

agg_data = grouped.agg({
    'Math': ['mean', 'median', 'std']
})

# print(agg_data)

agg_data_multi = grouped.agg({
    'Math': ['mean', 'median', 'min'],
    'English': ['mean', 'max'],
    'History': ['min', 'max']
})

# print(agg_data_multi)
df['Class'] = ['X', 'X', 'Y', 'Y', 'X', 'Y', 'Y', 'X']
grouped_multi = df.groupby(['School', 'Class'])
print(grouped_multi.mean())

# CHALLENGE
# Use grouping and aggregating to calculate the median score across all classes by school.

# AI Output
grouped_median = df.groupby('School').agg({'Math': 'median', 'English': 'median', 'History': 'median'})
print(grouped_median)

# Human Output
print(df.groupby(['School', 'Class']).median())

sports_data = {
    'Student ID': [1001, 1002, 1003, 1004, 1009, 1010],
    'Sports': ['Basketball', 'Football', 'Badminton', 'Basketball', 'Football', 'Tennis']
}

sports_df = pd.DataFrame(sports_data)

merged_df = pd.merge(df, sports_df, on='Student ID') # Defaults to Inner Join Only Join Rows where BOTH have values. 1009 and 1010 do not appear

print(merged_df)

