import re
import pandas as pd

df = pd.read_csv('sample_data/batilaptop-01.csv')

# Extract columns and their data types
column_info = pd.DataFrame(df.dtypes, columns=['Data Type'])

# Display the table
print(column_info)
