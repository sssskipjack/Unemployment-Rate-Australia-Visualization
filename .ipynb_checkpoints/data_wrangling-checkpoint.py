import pandas as pd

path = "data/unemploymentRateTimeSeries.csv"
# Read the CSV file, skipping the first five rows
df = pd.read_csv(path, skiprows=5)
# Melt the dataframe to long format
df_long = df.melt(id_vars=['Unnamed: 0'], var_name='Metric_State', value_name='Value')
# Split the 'Metric_State' into 'Metric', 'Gender', and 'State'
df_long[['Metric', 'Gender', 'State']] = df_long['Metric_State'].str.extract(r'([^;]+); *>([^;]+); *>([^;]+);')
# Convert 'Value' to numeric, coerce errors to NaN
df_long['Value'] = pd.to_numeric(df_long['Value'], errors='coerce')

# Drop rows with NaN values in essential columns
df_long.dropna(subset=['Value', 'Metric', 'Gender', 'State'], inplace=True)
# Rename 'Unnamed: 0' to 'Time'
df_long.rename(columns={'Unnamed: 0': 'Time'}, inplace=True)

# Convert 'Time' to datetime format
df_long['Time'] = pd.to_datetime(df_long['Time'], format='%b-%Y')
# Save to CSV
df_long.to_csv('data/prepared_data.csv', index=False)
