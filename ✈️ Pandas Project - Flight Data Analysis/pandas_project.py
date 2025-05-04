import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flgihts.csv')
#Test print(df.head(10))
#Test print(df.info())
#Test print(df.isnull().sum())
#Test print(df.describe().round(2)) # Rounding, because otherwise it outputs in scientific notation.
#Test print(df['Origin'].value_counts())
#Test print(df['Origin'].unique())

#Test df['Year'] = df['Fly Date'].astype(str).str.slice(0,4).astype(int)
#Test print(df['Year'])
#Test flights_in_2000 = df[df['Year'] == 2000]
#Test print(flights_in_2000.head())
#Test print(flights_in_2000.info())

#Test non_lax_flights = df[~df['Origin'].isin(['LAX'])]
#Test print(non_lax_flights.head())
#Test print('LAX' in non_lax_flights['Origin'].unque())

#Test only_lax_flights = df[df['Origin'].isin(['LAX'])]
#Test print(only_lax_flights['Origin'].unique())

#Test passengers_and_distance = df[(df['Passengers'] > 100) & (df['Distance']) < 1000]
#Test print(passengers_and_distance[['Passengers', Distance]])

# la_ny = df[(df['Origin City']).str.contains('New York|Los Angeles')| (df['Destination City']).str.contains('New York|Los Angeles')]
# print(la_ny[['Origin City', 'Destination City']].head())
# print(la_ny.info())

# large_origin = df[df['Origin Population'] > 1000000]
# print(large_origin[['Origin City', 'Origin Population']])

# underbooked = df.query('Seats > Passengers')
# print(underbooked[['Seats', 'Passengers']])

# busy_shorthaul = df.query('Distance < 500 & Flights > 10')
# print(busy_shorthaul[['Distance', 'Flights']])

# Write to a CSV.
# busy_shorthaul.to_csv('shorthaul.csv')

# busiest_routes = df.groupby(['Origin', 'Destination']).agg({'Passengers': 'sum', 'Flights': 'sum'})
# busiest_routes = busiest_routes.sort_values(by=['Passengers', 'Flights'],ascending = [False, False])

# print(busiest_routes.head())

# df['Month'] = pd.to_datetime(df['Fly Date'], format = '%Y%m').dt.to_period('M')
# monthly_trends = df.groupby('Month').agg({'Flights': 'sum'})
# #Test monthly_trends = monthly_trends.sort_values(by='Month')

# #Test print(monthly_trends.head())

# distance_bins = pd.cut(df['Distance'], bins=[0, 500, 1000, 2000, 3000, 4000, df['Distance'].max()])
# distance_group = df.groupby(distance_bins).agg({'Flights': 'sum', 'Passengers': 'sum'})
# print(distance_group.sort_values(by='Distance', ascending = False))

# busiest_airports = df.groupby('Origin').agg({'Flights': 'sum'}).nlargest(10, 'Flights')
# busiest_airports = busiest_airports.sort_values(by=['Passengers', 'Flights'], ascending = [False, False])

# busiest_airports.plot(kind='bar')
# plt.title('Top 10 Busiest Airports by Outgoing Flights')
# plt.xlabel('Airport')
# plt.ylabel('Number of Flights')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# busiest_routes = df.groupby(['Origin', 'Destination']).agg({'Passengers': 'sum'}).nlargest(10, 'Passengers')
# busiest_routes.plot(kind='bar', color='darkblue')
# plt.title('Top 10 Busiest Routes by Passengers')
# plt.xlabel('Route')
# plt.ylabel('Number of Passengers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # Challenge: Create a bar chart showing the top 10 routes by flight numbers.

# busiest_flights = df.groupby(['Origin City', 'Destination City']).agg({'Flights': 'sum'}).nlargest(10, 'Flights')
# busiest_routes.plot(kind='bar', color='green')
# plt.title('Top 10 Routes by Flight Numbers')
# plt.xlabel('Route')
# plt.ylabel('Flights')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# df['Year'] = df['Fly Date'].astype(str).str.slice(0,4)
# year_groups = df.groupby('Year')
# year_groups.agg({'Passengers': 'sum'}).plot(kind='line')
# plt.title('Total Number of Flights per Year')
# plt.xlabel('Year')
# plt.ylabel('Passengers')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# distance_bins = pd.cut(df['Distance'], bins=[0, 500, 1000, 2000, 3000, 4000, df['Distance'].max()])
# distance_groups = df.groupby(distance_bins).agg({'Flights': 'sum'})
# distance_groups.plot(kind='pie', y='Flights')
# plt.title('Distribution of Flights by Distance')
# plt.tight_layout()
# plt.show()

# top_50_routes = df.groupby(['Origin City', 'Destination City']).agg({'Passengers': 'sum'}).nlargest(50, 'Passengers')
# top_50_routes.plot(kind='pie', y='Passengers')
# plt.title('Distribution of Passengers by Route')
# plt.tight_layout()
# plt.show()

# route_groups = df.groupby(['Origin', 'Destination']).agg({'Distance': 'mean', 'Passengers': 'sum' }).nlargest(50, 'Passengers')
# route_groups.plot(kind='scatter', x='Distance', y='Passengers')
# plt.title('Distance vs Passengers')
# plt.tight_layout()
# plt.show()

# df['Distance'].plot(kind='hist')
# plt.title('Distribution of Distances')
# plt.xlabel('Distance')
# plt.ylabel('Frequency')
# plt.tight_layout()
# plt.show()

df['Total City Population'] = df['Origin Population'] + df['Destination Population']
df['Year'] = df['Fly Date'].astype(str).str.slice(0,4)
city_populations = df.groupby(['Origin', 'Destination', 'Year']).agg({'Passengers': 'sum', 'Total City Population ': 'sum'}).sort_values(by='Year')
city_populations.plot(kind='scatter', x='Total City Population', y='Passengers')
plt.title('Number of Passengers by Total City Population')
plt.xlabel('Total City Population')
plt.ylabel('Number of Passengers')
plt.tight_layout()
plt.show()