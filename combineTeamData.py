import os
import pandas as pd

def combine_team_data(folder_path):
    # Initialize combined DataFrame
    combined_data = pd.DataFrame(columns=['Date', 'Week', 'Home Team Name', 'Away Team Name',
                                          'Winner', 
                                          'Home Team Total Yards', 'Away Team Total Yards',
                                          'Home Team Passing Yards', 'Away Team Passing Yards',
                                          'Home Team Passing TD', 'Away Team Passing TD',
                                          'Home Team Rushing Yards', 'Away Team Rushing Yards',
                                          'Home Team Rushing TD', 'Away Team Rushing TD',
                                          'Home Team Turnovers Lost', 'Away Team Turnovers Lost'])

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            team_data = pd.read_csv(file_path)

            # Process each game in the team's CSV file
            for index, game in team_data.iterrows():
                # If team in question is away
                if game['Home/Away'] == '@':
                    # Determine winner based on 'Result' column and whether the team is home or away
                    if game['Result'].startswith('W'):
                        winner = 'Away'
                    elif game['Result'].startswith('L'):
                        winner = 'Home'
                    else: 
                        winner = 'Tie'

                    game_data = {
                    'Date': game['Date'],
                    'Week': game['Week'],
                    'Home Team Name': game['Opponent'],
                    'Away Team Name': game['Team'],
                    'Winner': winner,
                    'Home Team Total Yards': game['Opponent Rushing Yards'] + game['Opponent Passing Yards'],
                    'Away Team Total Yards': game['Rushing Yards'] + game['Passing Yards'],
                    'Home Team Passing Yards': game['Opponent Passing Yards'],
                    'Away Team Passing Yards': game['Passing Yards'],
                    'Home Team Passing TD': game['Opponent Passing TD'],
                    'Away Team Passing TD': game['Passings TD'],
                    'Home Team Rushing Yards': game['Opponent Rushing Yards'],
                    'Away Team Rushing Yards': game['Rushing Yards'],
                    'Home Team Rushing TD': game['Opponent Rushing TD'],
                    'Away Team Rushing TD': game['Rushing TD'],
                    'Home Team Turnovers Lost': game['Turnovers'],
                    'Away Team Turnovers Lost': game['Turnovers Lost']
                    }
                else:
                    # Determine winner based on 'Result' column and whether the team is home or away
                    if game['Result'].startswith('W'):
                        winner = 'Home'
                    elif game['Result'].startswith('L'):
                        winner = 'Away'
                    else:
                        winner = 'Tie'
                    game_data = {
                    'Date': game['Date'],
                    'Week': game['Week'],
                    'Home Team Name': game['Team'],
                    'Away Team Name': game['Opponent'],
                    'Home Team Total Yards': game['Rushing Yards'] + game['Passing Yards'],
                    'Away Team Total Yards': game['Opponent Rushing Yards'] + game['Opponent Passing Yards'],
                    'Home Team Passing Yards': game['Passing Yards'],
                    'Away Team Passing Yards': game['Opponent Passing Yards'],
                    'Home Team Passing TD': game['Passings TD'],
                    'Away Team Passing TD': game['Opponent Passing TD'],
                    'Home Team Rushing Yards': game['Rushing Yards'],
                    'Away Team Rushing Yards': game['Opponent Rushing Yards'],
                    'Home Team Rushing TD': game['Rushing TD'],
                    'Away Team Rushing TD': game['Opponent Rushing TD'],
                    'Home Team Turnovers Lost': game['Turnovers Lost'],
                    'Away Team Turnovers Lost': game['Turnovers'],
                    'Winner': winner
                    }


                # Add game data to the combined data
                combined_data = pd.concat([combined_data, pd.DataFrame([game_data])], ignore_index=True)

    return combined_data

def main():
    folder_path = './2014-2023teamData'
    combined_data = combine_team_data(folder_path)
    combined_data.to_csv('combined_team_data.csv', index=False)
    print("Combined data saved to combined_team_data.csv")

if __name__ == "__main__":
    main()
