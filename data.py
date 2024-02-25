import pandas as pd


def rawSeasonDataToRestructuredSeasonData(input_csv, output_csv):

    # Read the CSV file
    df = pd.read_csv(input_csv)

    # This code takes in our seasonScheduleData and reformats it to a Home/Away format with some basic stats as well associated with the team winners and losers

    # Process the data
    df['Home Team Name'] = df.apply(lambda row: row['Loser/tie'] if row['Home/Away'] == '@' else row['Winner/tie'], axis=1)
    df['Away Team Name'] = df.apply(lambda row: row['Loser/tie'] if row['Home/Away'] != '@' else row['Winner/tie'], axis=1)
    df['Winner'] = df.apply(lambda row: 0 if row['Home/Away'] == '@' else 1, axis=1)
    df['Home Team Total Yards'] = df.apply(lambda row: row['YdsL'] if row['Home/Away'] == '@' else row['YdsW'], axis=1)
    df['Away Team Total Yards'] = df.apply(lambda row: row['YdsW'] if row['Home/Away'] == '@' else row['YdsL'], axis=1)
    df['Home Team Turnovers'] = df.apply(lambda row: row['TOL'] if row['Home/Away'] == '@' else row['TOW'], axis=1)
    df['Away Team Turnovers'] = df.apply(lambda row: row['TOW'] if row['Home/Away'] == '@' else row['TOL'], axis=1)

    # Restructure the data
    restructured_df = df[['Home Team Name', 'Away Team Name', 'Winner', 'Home Team Total Yards', 'Away Team Total Yards', 'Home Team Turnovers', 'Away Team Turnovers']]

    # Write the restructured data to a new CSV file
    restructured_df.to_csv(output_csv, index=False)


def main():
    raw_season_data = './seasonScheduleData/2023seasonSchedule.csv'
    restructured_file_name = 'restructured_2023_season_data.csv'
    rawSeasonDataToRestructuredSeasonData(raw_season_data, restructured_file_name)

if __name__ == "__main__":
    main()
