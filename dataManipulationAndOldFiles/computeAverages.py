import pandas as pd


read_file = '2014-2023teamData\SFO.csv'
# Read the CSV file
df = pd.read_csv(read_file)

# Exclude the header and select the first 15 rows
data_rows = df.iloc[1:16]

# Calculate the average of numerical columns
numeric_cols = data_rows.select_dtypes(include=['number']).columns
average_values = data_rows[numeric_cols].mean()

# Create a new DataFrame with the average values
average_df = pd.DataFrame(average_values, columns=['Average'])

# Write the average values to a new CSV file
average_df.to_csv('SFO_average_values.csv', index=True)
