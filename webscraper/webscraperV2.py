import hashlib
import pandas as pd
from bs4 import BeautifulSoup
import requests
import uuid
import os

player_links = {}

def fetch_roster_from_html(html_content, sport):
    """
    Extract player names from the HTML content of a roster page.

    Args:
        html_content (str): HTML content of the roster page.

    Returns:
        list: A list of player names.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table', {'id': 'roster'})  # Update with the actual table ID or class if different
    roster = pd.read_html(str(table))[0]
    if sport == 'NBA':
        roster["Birth Date"] = pd.to_datetime(roster["Birth Date"], format="%B %d, %Y").dt.strftime("%m-%d-%Y")
    elif sport == 'NFL':
        roster = roster.loc[roster["No."] != "No."]
        roster = roster.loc[roster["Player"] != "Team Total"]
        roster["BirthDate"] = pd.to_datetime(roster["BirthDate"], format="%m/%d/%Y").dt.strftime("%m-%d-%Y")
    roster["Player"] = roster["Player"].str.replace(r"\(TW\)", "", regex=True).str.strip()
    roster["No."] = roster["No."].fillna(-1).astype(int)
    if table:
        for row in table.find_all('tr'):
            player_cell = row.find('td', {'data-stat': 'player'})  # Adjust 'data-stat' to match the HTML
            if player_cell:
                player_name = player_cell.text.strip()
                cleaned_name = player_name.replace("\xa0", "").replace("(TW)", "").strip()
                link_tag = player_cell.find('a')
                player_link = link_tag['href'] if link_tag else None
                roster.loc[roster["Player"] == cleaned_name, "Link"] = player_link
    roster["Player"] = roster["Player"].str.replace(r"\(SUS\)", "", regex=True).str.strip()
    roster["Player"] = roster["Player"].str.replace(r"\(FRES\)", "", regex=True).str.strip()
    roster["Player"] = roster["Player"].str.replace(r"\(IR\)", "", regex=True).str.strip()
    return roster

def generate_numeric_hashes(names, birthdates, sport, hash_length=7):
    """
    Generate numeric-only hashes for a list of names and corresponding birthdates.

    Args:
        names (list of str): List of player names.
        birthdates (list of str): List of birthdates in MM/DD/YYYY format.
        hash_length (int): Length of the numeric hash to return (default is 7).

    Returns:
        dict: A dictionary mapping player names to their numeric hashes.
    """
    numeric_hashes = {}
    for i, name in enumerate(names):
        # Loop over birthdates, matching name index
        birthdate = birthdates[i % len(birthdates)]
        combined = f"{name}{birthdate}"

        # Generate SHA-1 hash and extract numeric characters
        hash_key = hashlib.sha1(combined.encode()).hexdigest()
        if sport == 'NBA':
            sport_id = '0'
        elif sport == 'NFL':
            sport_id = '1'
        
        numeric_key = sport_id.join(filter(str.isdigit, hash_key))
        # numeric_key = sport_id.join(filter(str.isdigit, hash_key))[:hash_length]

        # Store the result in the dictionary
        numeric_hashes[name] = numeric_key

    return numeric_hashes


def extract_player_bio_and_stats(html_file):
    """
    Extract player bio information and career stats from an HTML file.

    Args:
        html_file (str): Path to the HTML file.

    Returns:
        dict: Player bio information.
        dict: DataFrames for career per game and career totals tables.
    """
    # Load and parse the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')

    # Extract bio information
    bio_info = {}
    bio_section = soup.find('div', id='meta')
    if bio_section:
        name_tag = bio_section.find('h1')
        if name_tag:
            bio_info['Name'] = name_tag.text.strip()

        for p_tag in bio_section.find_all('p'):
            text = p_tag.text.strip()
            if text.startswith('Position:'):
                bio_info['Position'] = text.replace('Position:', '').strip()
            elif 'Born:' in text:
                bio_info['Born'] = text.replace('Born:', '').strip()
            elif 'College:' in text:
                bio_info['College'] = text.replace('College:', '').strip()
            elif 'Height:' in text or 'Weight:' in text:
                bio_info.update({
                    key: value.strip() for key, value in \
                    (item.split(':') for item in text.split('\n') if ':' in item)
                })

    # Extract career stats tables
    tables = soup.find_all('table')
    stats_tables = {}
    for table in tables:
        if 'Per Game' in table.text:
            stats_tables['Career Per Game'] = pd.read_html(str(table))[0]
        elif 'Career Totals' in table.text:
            stats_tables['Career Totals'] = pd.read_html(str(table))[0]

    return bio_info, stats_tables

# Example Usage
# if __name__ == "__main__":
#     # Option to read from a local HTML file
#     local_file_path = "Knowball\\data\\preprocessing\\teams\\NFL\\sfo\\2024.html"  # Replace with your file path
    
#     try:
#         file_path = "Knowball\\data\\postprocessing\\teams\\NFL\\sfo\\2024_roster.csv"
#         with open(local_file_path, 'r', encoding='utf-8') as file:
#             html_content = file.read()

#         # Extract player names from the local HTML
#         roster = fetch_roster_from_html(html_content, sport='NFL')
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         roster.to_csv(file_path, index=False)

#     except FileNotFoundError:
#         print(f"File not found: {local_file_path}")

## above

    # # Option to fetch from a URL
    # url = "https://www.basketball-reference.com/teams/ATL/2025.html"  # Example URL
    # response = requests.get(url)

    # if response.status_code == 200:
    #     html_content = response.text

    #     # Extract player names from the HTML
    #     player_names = fetch_roster_from_html(html_content)

    #     # Example birthdates (simulated, replace with actual if available)
    #     sample_birthdates = [
    #         "01/01/1995", "02/15/1996", "03/20/1997", "04/10/1998",
    #         "05/25/1999", "06/30/2000", "07/15/2001", "08/05/2002",
    #         "09/25/1993", "10/10/1992", "11/11/1991", "12/12/1990",
    #         "01/22/1995", "02/14/1996", "03/16/1997", "07/12/1998",
    #     ]

    #     # Generate numeric-only hashes
    #     hashes = generate_numeric_hashes(player_names, sample_birthdates)

    #     # Convert to a DataFrame for display or saving
    #     df = pd.DataFrame(hashes.items(), columns=['Player Name', 'Numeric SHA Key'])
    #     print(df)

    #     # Optionally save to a CSV file
    #     df.to_csv("player_numeric_hashes.csv", index=False)
    # else:
    #     print(f"Failed to fetch the roster page. HTTP Status Code: {response.status_code}")

    # Example usage
if __name__ == "__main__":
    html_file_path = "Knowball\data\preprocessing\players\\NBA\ATL\Trae Young.html"  # Replace with the actual path to your file

    # Extract bio and stats
    player_bio, player_stats = extract_player_bio_and_stats(html_file_path)

    # Display bio information
    print("Player Bio Information:")
    for key, value in player_bio.items():
        print(f"{key}: {value}")

    # Display stats tables
    for table_name, df in player_stats.items():
        print(f"\n{table_name}:")
        print(df)

        # Optionally save to CSV
        # df.to_csv(f"{table_name.replace(' ', '_').lower()}.csv", index=False)