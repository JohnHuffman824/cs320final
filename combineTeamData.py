import os
import pandas as pd

def combine_team_data(folder_path):
    # Initialize combined DataFrame
    # Game Order,Team,Date,Passing Yards,Passings TD,Rushing Yards,Rushing TD,Turnovers,Opponent Passing Yards,Opponent Rushing Yards,Time of Possession,Day of Week,Game Number,Week,Home/Away,Opponent,Result,Passing Completions,Passing Attempts,Passing Incompletions,Passing Completion Percentage,Passing TD,Interceptions,TD Percentage per Pass,Interception Percentage per Pass,Passer Rating,Times Sacked,Sack Yards,Sack Percentage,Yards per Attempt,Net Yards per Attempt,Adjusted Yards per Attempt,Adjusted Net Yards per Attempt,Yards per Completion,Opponent Rushing Attempts,Opponent Rushing Yards per Attempt,Opponent Rushing TD,Opponent Pass Completions,Opponent Pass Attempts,Opponent Completion Percentage,Opponent Passing TD,Opponent Times Sacked,Opponent Sack Yards,Opponent Interceptions,Opponent Passer Rating,Rushing Attempts,Rushing Yards per Attempt,Total Yardage,Offense Number of Plays,Yards per Offensive Play,Defense Number of Plays,Yards Allowed per Defensive Play,Turnovers Lost,Total Time,Opponent Turnovers,Penalties,Penalty Yards,Opponent Penalties,Opponent Penalty Yards,Field Goals Made,Opponent Field Goals Made,3rd Down %,Oppoenent 3rd Down %,1st Downs,1st Downs by Rush,1st Downs by Pass,1st Downs by Pen,3rd Down Attempts,3rd Down Conversions,3rd Down Conversion %,4th Down Attempts,4th Down Conversions,4th Down Conversion %,Opponent Total Yards,Opponent Turnovers.1,Penalties.1,Penalty Yards.1,Opponent Penalties.1,Opponent Penalty Yards.1,Combined Penalties,Combined Penalty Yards,Opponent TD,Opponent XPA,Opponent XPM,Opponent Field Goals Attempted,Opponent Field Goals Made.1,Opponent Safeties,Total Yards,Offensive Plays,Yards per Play,Defensive Plays,Defensive Yards per Play,Turnovers.1,Time,Opponent 1st Downs,Opponent 1st Downs by Rush,Opponent 1st Downs by Pass,Opponent 1st Downs by Penalty,Opponent 3rd Down Attempts,Opponent 3rd Down Conversions,Opponent 3rd Down Conversion %,Opponent 4th Down Attempts,Opponent 4th Down Conversions,Opponent 4th Down Conversion %,Total TD,XPA,XPM,Field Goals Attempted,Field Goals Made.1,2PA,2PM,Safeties
    # UPDATE THIS TO COMBINE WITH NEW FEATURES
    combined_data = pd.DataFrame(columns=['Date', 'Week', 'Home Team Name', 'Away Team Name',
                                          'Winner', 
                                          'Home Team Total Yards', 'Away Team Total Yards',
                                          'Home Team Passing Yards', 'Away Team Passing Yards',
                                          'Home Team Passing TD', 'Away Team Passing TD',
                                          'Home Team Rushing Yards', 'Away Team Rushing Yards',
                                          'Home Team Rushing TD', 'Away Team Rushing TD',
                                          'Home Team Turnovers Lost', 'Away Team Turnovers Lost'
                                          ])

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
                        winner = 0
                    elif game['Result'].startswith('L'):
                        winner = 1
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
                    'Home Team Turnovers Lost': game['Opponent Turnovers'],
                    'Away Team Turnovers Lost': game['Turnovers']
                    }
                else:
                    # Determine winner based on 'Result' column and whether the team is home or away
                    if game['Result'].startswith('W'):
                        winner = 0
                    elif game['Result'].startswith('L'):
                        winner = 1
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
                    'Home Team Turnovers Lost': game['Turnovers'],
                    'Away Team Turnovers Lost': game['Opponent Turnovers'],
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
