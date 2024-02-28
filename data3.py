import os
import csv

# Function to replace the first two lines with the specified header
def replace_header(file_path):
    new_lines = []
    header_line = "Game Order,Team,Date,Passing Yards,Passings TD,Rushing Yards,Rushing TD,Turnovers,Opponent Passing Yards,Opponent Rushing Yards,Time of Possession,Day of Week,Game Number,Week,Home/Away,Opponent,Result,Passing Completions,Passing Attempts,Passing Incompletions,Passing Completion Percentage,Passing Yards,Passing TD,Interceptions,TD Percentage per Pass,Interception Percentage per Pass,Passer Rating,Times Sacked,Sack Yards,Sack Percentage,Yards per Attempt,Net Yards per Attempt,Adjusted Yards per Attempt,Adjusted Net Yards per Attempt,Yards per Completion,Opponent Rushing Attempts,Opponent Rushing Yards,Opponent Rushing Yards per Attempt,Opponent Rushing TD,Opponent Pass Completions,Opponent Pass Attempts,Opponent Completion Percentage,Opponent Passing Yards,Opponent Passing TD,Opponent Times Sacked,Opponent Sack Yards,Opponent Interceptions,Opponent Passer Rating,Rushing Attempts,Rushing Yards,Rusing Yards per Attempt,Rushing TD,Total Yardage,Offense Number of Plays,Yards per Offensive Play,Defense Number of Plays,Yards Allowed per Defensive Play,Turnovers Lost,Time of Possession,Total Time\n"
    
    # Read lines from the file, excluding the first two lines
    with open(file_path, 'r') as file:
        lines = file.readlines()[2:]
    
    # Insert the new header line at the beginning
    new_lines.append(header_line)
    new_lines.extend(lines)
    
    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# Specify the folder containing CSV files
folder_path = './2014-2023teamData'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        replace_header(file_path)
        print(f"Processed: {filename}")

print("All CSV files processed.")
