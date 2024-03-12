html_url = "https://stathead.com/football/team-game-finder.cgi?request=1&order_by_asc=1&order_by=date&timeframe=seasons&year_min=2014&year_max=2023&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_yds&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_td&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rush_yds&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rush_td&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=turnovers&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=pass_yds_opp&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=rush_yds_opp&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=time_of_poss&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=turnovers_opp&team_id=cin"

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Read team IDs and names from CSV
team_data = pd.read_csv('stathead_team_ids.csv', header=None, names=['ID', 'Team Name'])

# Iterate over each row in the DataFrame
for index, row in team_data.iterrows():
    team_id = row['ID']
    team_name = row['Team Name']
    
    # Construct the URL for each team ID
    url = f"https://stathead.com/football/team-game-finder.cgi?request=1&order_by_asc=1&order_by=date&timeframe=seasons&year_min=2014&year_max=2023&ccomp%5B1%5D=gt&cval%5B1%5D=0&cstat%5B1%5D=pass_yds&ccomp%5B2%5D=gt&cval%5B2%5D=0&cstat%5B2%5D=pass_td&ccomp%5B3%5D=gt&cval%5B3%5D=0&cstat%5B3%5D=rush_yds&ccomp%5B4%5D=gt&cval%5B4%5D=0&cstat%5B4%5D=rush_td&ccomp%5B5%5D=gt&cval%5B5%5D=0&cstat%5B5%5D=turnovers&ccomp%5B6%5D=gt&cval%5B6%5D=0&cstat%5B6%5D=pass_yds_opp&ccomp%5B7%5D=gt&cval%5B7%5D=0&cstat%5B7%5D=rush_yds_opp&ccomp%5B8%5D=gt&cval%5B8%5D=0&cstat%5B8%5D=time_of_poss&ccomp%5B9%5D=gt&cval%5B9%5D=0&cstat%5B9%5D=turnovers_opp&team_id={team_id}"
    
    # Fetch HTML content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
       
        table = soup.find('table')
        if table:
            data = []
            for row in table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                if len(row_data) >= 14:  # Check if row has enough columns
                    data.append(row_data)
                    print("Row data:", row_data)
                else:
                    print("Skipping row:", row_data)
            
            if len(data) > 0:  # Check if there's valid data
                header_row = data[1]  # Remove empty strings from header row
                print("Header row:", header_row)
                print("Number of columns in header row:", len(header_row))
                print("Number of rows in data:", len(data))

                # Create DataFrame
                df = pd.DataFrame(data[1:], columns=header_row)
                
                # Write to CSV with appropriate team name
                filename = f"{team_name}_{team_id}_data.csv"
                df.to_csv(filename, index=False)
                print(f"Data for {team_name} written to {filename}")
            else:
                print(f"No valid data found for {team_name}")
        else:
            print(f"No table found for {team_name}")

    else:
        print(f"Failed to fetch data for {team_name}")
