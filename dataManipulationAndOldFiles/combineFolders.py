import os
import pandas as pd

folder1_path = '2014-2023teamData'
folder2_path = '2014-2023teamDataSECOND'

# Get list of CSV files in folder 1
folder1_files = os.listdir(folder1_path)

# Iterate through each CSV file in folder 1
for file in folder1_files:
    if file.endswith('.csv'):
        file_path_folder1 = os.path.join(folder1_path, file)
        file_path_folder2 = os.path.join(folder2_path, file)
        
        # Check if corresponding file exists in folder 2
        if os.path.exists(file_path_folder2):
            # Read CSV files into DataFrames
            df_folder1 = pd.read_csv(file_path_folder1)
            df_folder2 = pd.read_csv(file_path_folder2)
            
            # Get columns to add from folder 2
            columns_to_add = [col for col in df_folder2.columns if col not in df_folder1.columns]
            
            # Add columns from folder 2 to folder 1 DataFrame
            for column in columns_to_add:
                df_folder1[column] = df_folder2[column]
            
            # Write updated DataFrame to CSV in folder 1
            df_folder1.to_csv(file_path_folder1, index=False)
            
            print(f"Merged columns from {file} in folder 2 to {file} in folder 1.")
        else:
            print(f"File {file} does not exist in folder 2.")
