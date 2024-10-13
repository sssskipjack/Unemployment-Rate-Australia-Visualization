import pandas as pd
import numpy as np 

df = pd.read_csv("UnemploymentReasonsCleaned.csv")

# Identify classification rows (non-indented)
df['Is_Class'] = ~df['Category'].str.startswith(' ')

# Initialize 'Classification' column with NaN
df['Classification'] = np.nan

# Assign classification names to the 'Classification' column where 'Is_Class' is True
df.loc[df['Is_Class'], 'Classification'] = df.loc[df['Is_Class'], 'Category']

# Forward fill the 'Classification' column to propagate classifications to subcategories
df['Classification'] = df['Classification'].ffill()

# Assign 'Other' classification to specific categories
df.loc[df['Category'].isin(['Other reasons', 'Did not know']), 'Classification'] = 'Other'

# Strip leading and trailing spaces from 'Category'
df['Category'] = df['Category'].str.strip()

# Reorder columns to have 'Classification' before 'Category'
cols = df.columns.tolist()
category_idx = cols.index('Category')
cols.insert(category_idx, cols.pop(cols.index('Classification')))
df = df[cols]

# Drop the temporary 'Is_Class' column
df.drop('Is_Class', axis=1, inplace=True)

# Display the transformed data
print(df.head(20))

# Optionally, save to CSV
df.to_csv('wrangledReasons.csv', index=False)

