import os
import pandas as pd

def fix_typo(folder_path):
    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)

            # Check if 'Rusing Yards per Attempt' column exists
            if 'Rusing Yards per Attempt' in df.columns:
                # Drop the column
                df.drop(columns=['Rusing Yards per Attempt'], inplace=True)
                # Save the modified DataFrame back to the same CSV file
                df.to_csv(file_path, index=False)
                print(f"Fixed typo in {filename}")

def main():
    folder_path = './2014-2023teamData'
    fix_typo(folder_path)
    print("Typo fixed in all CSV files.")

if __name__ == "__main__":
    main()
