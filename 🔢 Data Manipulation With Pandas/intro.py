import pandas as pd # Import alias
import numpy as np

# DataFrame: a 2D table with rows and columns
df_data = {
    'col1': np.random.rand(5),
    'col2': np.random.rand(5),
    'col3': np.random.rand(5)
}

df = pd.DataFrame(df_data)
print(df)

# Fetch some rows
print(df[:1])
print(df[:2])

# Fetch a col
print(df['col1'])

# Fetch multiple cols
print(df[['col1', 'col2']])