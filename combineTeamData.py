import os
import pandas as pd

def combine_team_data(folder_path):
    # Initialize combined DataFrame
    # Time of Possession,
    # Result,Passing Completions,Passing Incompletions,
    # Interceptions,TD Percentage per Pass,Interception Percentage per Pass,Passer Rating,Sack Yards,Sack Percentage,Yards per Attempt,
    # Net Yards per Attempt,Adjusted Yards per Attempt,Adjusted Net Yards per Attempt,Yards per Completion,
    # Opponent Pass Completions,Opponent Sack Yards,
    # Opponent Interceptions,Opponent Passer Rating,Total Yardage,Offense Number of Plays,Yards per Offensive Play,
    # Turnovers Lost,Total Time,Penalty Yards,Defensive plays, Yards Allowed per Defensive Play
    # Opponent Penalty Yards,1st Downs by Rush,1st Downs by Pass,1st Downs by Pen,
    # 3rd Down Conversions,4th Down Conversions,
    # Combined Penalties,Combined Penalty Yards,Opponent XPA,Opponent XPM,
    # Opponent Field Goals Made.1,Opponent Safeties,Total Yards,Offensive Plays,Yards per Play,Defensive Plays,Defensive Yards per Play,
    # Time,Opponent 1st Downs by Rush,Opponent 1st Downs by Pass,Opponent 1st Downs by Penalty,
    # Opponent 3rd Down Conversions,Opponent 4th Down Conversions,
    # Total TD,XPA,XPM,Field Goals Attempted,Field Goals Made.1,2PA,2PM,Safeties

    # UPDATE THIS TO COMBINE WITH NEW FEATURES
    combined_data = pd.DataFrame(columns=['Date', 'Week', 'Home Team Name', 'Away Team Name',
                                          'Winner', 
                                          'Home Team Total Yards', 'Away Team Total Yards',
                                          'Home Team Passing Yards', 'Away Team Passing Yards',
                                          'Home Team Passing TD', 'Away Team Passing TD',
                                          'Home Team Rushing Yards', 'Away Team Rushing Yards',
                                          'Home Team Rushing TD', 'Away Team Rushing TD',
                                          'Home Team Turnovers Lost', 'Away Team Turnovers Lost',
                                          'Home Team Passing Attempts', 'Away Team Passing Attempts',
                                          'Home Team Passing Completion Percentage', 'Away Team Passing Completion Percentage',
                                          'Home Team Times Sacked', 'Away Team Times Sacked',
                                          'Home Team Rushing Attempts', 'Away Team Rushing Attempts',
                                          'Home Team Rushing Yards per Attempt', 'Away Team Rushing Yards per Attempt',
                                          'Home Team Penalties', 'Away Team Penalties',
                                          'Home Team Field Goals Attempted', 'Away Team Field Goals Attempted',
                                          'Home Team Field Goals Made', 'Away Team Field Goals Made',
                                          'Home Team 3rd Down Attempts', 'Away Team 3rd Down Attempts',
                                          'Home Team 3rd Down %', 'Away Team 3rd Down %',
                                          'Home Team 4th Down Attempts', 'Away Team 4th Down Attempts',
                                          'Home Team 4th Down Conversion %', 'Away Team 4th Down Conversion %',
                                          'Home Team 1st Downs', 'Away Team 1st Downs'
                                          #   'Home Team Defense Number of Plays', 'Away Team Defense Number of Plays',
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
                        winner = 1

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
                    'Away Team Turnovers Lost': game['Turnovers'],
                    'Home Team Passing Attempts': game['Opponent Pass Attempts'],
                    'Away Team Passing Attempts': game['Passing Attempts'],
                    'Home Team Passing Completion Percentage': game['Opponent Completion Percentage'], 
                    'Away Team Passing Completion Percentage': game['Passing Completion Percentage'],
                    'Home Team Times Sacked': game['Opponent Times Sacked'],
                    'Away Team Times Sacked': game['Times Sacked'],
                    'Home Team Rushing Attempts': game['Opponent Rushing Attempts'],
                    'Away Team Rushing Attempts': game['Rushing Attempts'],
                    'Home Team Rushing Yards per Attempt': game['Opponent Rushing Yards per Attempt'],
                    'Away Team Rushing Yards per Attempt': round(game['Rushing Yards'] / game['Rushing Attempts'], 2),
                    'Home Team Penalties': game['Opponent Penalties'],
                    'Away Team Penalties': game['Penalties'],
                    'Home Team Field Goals Attempted': game['Opponent Field Goals Attempted'],
                    'Away Team Field Goals Attempted': game['Field Goals Attempted'],
                    'Home Team Field Goals Made': game['Opponent Field Goals Made'],
                    'Away Team Field Goals Made': game['Field Goals Made'],
                    'Home Team 3rd Down Attempts': game['Opponent 3rd Down Attempts'],
                    'Away Team 3rd Down Attempts': game['3rd Down Attempts'],
                    'Home Team 3rd Down %': game['Opponent 3rd Down Conversion %'],
                    'Away Team 3rd Down %': game['3rd Down %'],
                    'Home Team 4th Down Attempts': game['Opponent 4th Down Attempts'],
                    'Away Team 4th Down Attempts': game['4th Down Attempts'],
                    'Home Team 4th Down Conversion %': game['Opponent 4th Down Conversion %'],
                    'Away Team 4th Down Conversion %': game['4th Down Conversion %'],
                    'Home Team 1st Downs': game['Opponent 1st Downs'],
                    'Away Team 1st Downs':game['1st Downs']
                    }
                else:
                    # Determine winner based on 'Result' column and whether the team is home or away
                    if game['Result'].startswith('W'):
                        winner = 0
                    elif game['Result'].startswith('L'):
                        winner = 1
                    else:
                        winner = 0
                    game_data = {
                    'Date': game['Date'],
                    'Week': game['Week'],
                    'Home Team Name': game['Team'],
                    'Away Team Name': game['Opponent'],
                    'Winner': winner,
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
                    'Home Team Passing Attempts': game['Passing Attempts'],
                    'Away Team Passing Attempts': game['Opponent Pass Attempts'],
                    'Home Team Passing Completion Percentage': game['Passing Completion Percentage'], 
                    'Away Team Passing Completion Percentage': game['Opponent Completion Percentage'],
                    'Home Team Times Sacked': game['Times Sacked'],
                    'Away Team Times Sacked': game['Opponent Times Sacked'],
                    'Home Team Rushing Attempts': game['Rushing Attempts'],
                    'Away Team Rushing Attempts': game['Opponent Rushing Attempts'],
                    'Home Team Rushing Yards per Attempt': round(game['Rushing Yards'] / game['Rushing Attempts'], 2),
                    'Away Team Rushing Yards per Attempt': game['Opponent Rushing Yards per Attempt'],
                    'Home Team Penalties': game['Penalties'],
                    'Away Team Penalties': game['Opponent Penalties'],
                    'Home Team Field Goals Attempted': game['Field Goals Attempted'],
                    'Away Team Field Goals Attempted': game['Opponent Field Goals Attempted'],
                    'Home Team Field Goals Made': game['Field Goals Made'],
                    'Away Team Field Goals Made': game['Opponent Field Goals Made'],
                    'Home Team 3rd Down Attempts': game['3rd Down Attempts'],
                    'Away Team 3rd Down Attempts': game['Opponent 3rd Down Attempts'],
                    'Home Team 3rd Down %': game['3rd Down %'],
                    'Away Team 3rd Down %': game['Opponent 3rd Down Conversion %'],
                    'Home Team 4th Down Attempts': game['4th Down Attempts'],
                    'Away Team 4th Down Attempts': game['Opponent 4th Down Attempts'],
                    'Home Team 4th Down Conversion %': game['4th Down Conversion %'],
                    'Away Team 4th Down Conversion %': game['Opponent 4th Down Conversion %'],
                    'Home Team 1st Downs': game['1st Downs'],
                    'Away Team 1st Downs':game['Opponent 1st Downs']
                    }


                # Add game data to the combined data
                combined_data = pd.concat([combined_data, pd.DataFrame([game_data])], ignore_index=True)

    return combined_data

def main():
    folder_path = './2014-2023teamData'
    combined_data = combine_team_data(folder_path)
    combined_data.to_csv('combined_team_data_newest.csv', index=False)
    print("Combined data saved to combined_team_data_newest.csv")

if __name__ == "__main__":
    main()
