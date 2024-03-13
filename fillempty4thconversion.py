import pandas as pd

# Read the combined CSV file
df = pd.read_csv('combined_team_data_newest.csv')

# Check for missing values in 4th down conversion percentage column and replace them with 1
df['Home Team 4th Down Conversion %'].fillna(0, inplace=True)
df['Away Team 4th Down Conversion %'].fillna(0, inplace=True)

# Save the modified DataFrame back to CSV
df.to_csv('combined_team_data_newest_filled.csv', index=False)
