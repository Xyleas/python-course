import pandas as pandas

# Read an Excel 
tracks = pd.read_excel('Tracks.xlsx', sheet_name=0)

#print(tracks)
#print(tracks.columns)
print(tracks['Milliseconds'])

# Read a CSV file
flights = pd.read_csv('flights.csv', index_col=False)

print(flights)