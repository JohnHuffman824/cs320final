import os
import csv

# Define a function to replace team abbreviations
def replace_team_abbreviations(file_path):
    # Define mapping of old abbreviations to new ones
    abbreviation_mapping = {'SDG': 'LAC', 'OAK': 'LVR', 'STL': 'LAR'}
    
    # Read the CSV file and replace abbreviations
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for row in rows:
            if len(row) > 1:
                # Replace team abbreviation in 'Team' column
                if row[1] in abbreviation_mapping:
                    row[1] = abbreviation_mapping[row[1]]
                # Replace team abbreviation in 'Opponent' column
                if row[15] in abbreviation_mapping:
                    row[15] = abbreviation_mapping[row[15]]
    
    # Write the modified data back to the CSV file
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Specify the folder containing CSV files
folder_path = './2014-2023teamData'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        replace_team_abbreviations(file_path)
        print(f"Processed: {filename}")

print("All CSV files processed.")
