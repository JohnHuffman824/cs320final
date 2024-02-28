import os
import csv

# Function to remove duplicate columns
def remove_duplicate_columns(file_path):
    # Read the CSV file and identify duplicate columns
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read the header row
        unique_headers = []
        columns_to_keep = []
        for header in headers:
            if header not in unique_headers:
                unique_headers.append(header)
                columns_to_keep.append(True)
            else:
                columns_to_keep.append(False)

    # Read the data and keep only the non-duplicate columns
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        for row in rows:
            row[:] = [cell for cell, keep_column in zip(row, columns_to_keep) if keep_column]

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
        remove_duplicate_columns(file_path)
        print(f"Processed: {filename}")

print("All CSV files processed.")
