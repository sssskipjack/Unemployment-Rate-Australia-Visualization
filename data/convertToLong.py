import pandas as pd

# Load the CSV file
file_path = 'EmploymentInformationWide.csv'
employment_info_wide = pd.read_csv(file_path)

# Convert the 'Date' column to a proper date format
employment_info_wide['Date'] = pd.to_datetime(employment_info_wide['Date'], format='%b-%Y')

# Melt the data to convert it into long format
employment_info_long = pd.melt(employment_info_wide, id_vars=["Date"], 
                               var_name="Metric", value_name="Value")

# Save the long format data to a new CSV
output_file_path = 'EmploymentInformationLong.csv'
employment_info_long.to_csv(output_file_path, index=False)

# Show the first few rows of the long format dataframe
employment_info_long.head()

