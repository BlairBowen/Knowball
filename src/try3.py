import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Step 1: Define All NBA Team Wikipedia Pages
nba_teams = {
    "Atlanta Hawks": "Atlanta_Hawks",
    "Boston Celtics": "Boston_Celtics",
    "Brooklyn Nets": "Brooklyn_Nets",
    "Charlotte Hornets": "Charlotte_Hornets",
    "Chicago Bulls": "Chicago_Bulls",
    "Cleveland Cavaliers": "Cleveland_Cavaliers",
    "Dallas Mavericks": "Dallas_Mavericks",
    "Denver Nuggets": "Denver_Nuggets",
    "Detroit Pistons": "Detroit_Pistons",
    "Golden State Warriors": "Golden_State_Warriors",
    "Houston Rockets": "Houston_Rockets",
    "Indiana Pacers": "Indiana_Pacers",
    "Los Angeles Clippers": "Los_Angeles_Clippers",
    "Los Angeles Lakers": "Los_Angeles_Lakers",
    "Memphis Grizzlies": "Memphis_Grizzlies",
    "Miami Heat": "Miami_Heat",
    "Milwaukee Bucks": "Milwaukee_Bucks",
    "Minnesota Timberwolves": "Minnesota_Timberwolves",
    "New Orleans Pelicans": "New_Orleans_Pelicans",
    "New York Knicks": "New_York_Knicks",
    "Oklahoma City Thunder": "Oklahoma_City_Thunder",
    "Orlando Magic": "Orlando_Magic",
    "Philadelphia 76ers": "Philadelphia_76ers",
    "Phoenix Suns": "Phoenix_Suns",
    "Portland Trail Blazers": "Portland_Trail_Blazers",
    "Sacramento Kings": "Sacramento_Kings",
    "San Antonio Spurs": "San_Antonio_Spurs",
    "Toronto Raptors": "Toronto_Raptors",
    "Utah Jazz": "Utah_Jazz",
    "Washington Wizards": "Washington_Wizards"
}

nfl_teams = {
    "Arizona Cardinals": "Arizona_Cardinals",
    "Atlanta Falcons": "Atlanta_Falcons",
    "Baltimore Ravens": "Baltimore_Ravens",
    "Buffalo Bills": "Buffalo_Bills",
    "Carolina Panthers": "Carolina_Panthers",
    "Chicago Bears": "Chicago_Bears",
    "Cincinnati Bengals": "Cincinnati_Bengals",
    "Cleveland Browns": "Cleveland_Browns",
    "Dallas Cowboys": "Dallas_Cowboys",
    "Denver Broncos": "Denver_Broncos",
    "Detroit Lions": "Detroit_Lions",
    "Green Bay Packers": "Green_Bay_Packers",
    "Houston Texans": "Houston_Texans",
    "Indianapolis Colts": "Indianapolis_Colts",
    "Jacksonville Jaguars": "Jacksonville_Jaguars",
    "Kansas City Chiefs": "Kansas_City_Chiefs",
    "Las Vegas Raiders": "Las_Vegas_Raiders",
    "Los Angeles Chargers": "Los_Angeles_Chargers",
    "Los Angeles Rams": "Los_Angeles_Rams",
    "Miami Dolphins": "Miami_Dolphins",
    "Minnesota Vikings": "Minnesota_Vikings",
    "New England Patriots": "New_England_Patriots",
    "New Orleans Saints": "New_Orleans_Saints",
    "New York Giants": "New_York_Giants",
    "New York Jets": "New_York_Jets",
    "Philadelphia Eagles": "Philadelphia_Eagles",
    "Pittsburgh Steelers": "Pittsburgh_Steelers",
    "San Francisco 49ers": "San_Francisco_49ers",
    "Seattle Seahawks": "Seattle_Seahawks",
    "Tampa Bay Buccaneers": "Tampa_Bay_Buccaneers",
    "Tennessee Titans": "Tennessee_Titans",
    "Washington Commanders": "Washington_Commanders"
}

epl_teams = {
    "Arsenal": "Arsenal_F.C.",
    "Aston Villa": "Aston_Villa_F.C.",
    "Bournemouth": "A.F.C._Bournemouth",
    "Brentford": "Brentford_F.C.",
    "Brighton & Hove Albion": "Brighton_%26_Hove_Albion_F.C.",
    "Burnley": "Burnley_F.C.",
    "Chelsea": "Chelsea_F.C.",
    "Crystal Palace": "Crystal_Palace_F.C.",
    "Everton": "Everton_F.C.",
    "Fulham": "Fulham_F.C.",
    "Liverpool": "Liverpool_F.C.",
    "Luton Town": "Luton_Town_F.C.",
    "Manchester City": "Manchester_City_F.C.",
    "Manchester United": "Manchester_United_F.C.",
    "Newcastle United": "Newcastle_United_F.C.",
    "Nottingham Forest": "Nottingham_Forest_F.C.",
    "Sheffield United": "Sheffield_United_F.C.",
    "Tottenham Hotspur": "Tottenham_Hotspur_F.C.",
    "West Ham United": "West_Ham_United_F.C.",
    "Wolverhampton Wanderers": "Wolverhampton_Wanderers_F.C."
}



# Step 2: Scrape Roster from Wikipedia (with player links)
def fetch_roster_from_wikipedia(team_wiki_title, sport):
    """Scrape the roster from an NBA team's Wikipedia page, including player Wikipedia links."""
    url = f"https://en.wikipedia.org/wiki/{team_wiki_title}"
    headers = {"User-Agent": "MyNBAStatsApp/1.0 (myemail@example.com)"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching {team_wiki_title}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the correct roster table
    if sport != "epl":
        # tables = soup.find_all("table", {"class": "toccolours"})
        roster_table = soup.find("table", {"class": "toccolours"})
    elif sport == "epl":
        # tables = soup.find_all("table", {"class": "toccolours"})
        roster_table = soup.find("table", {"role": "presentation"})
    else:
        roster_table = None

    # roster_table = tables[0]

    # for table in tables:
    #     if table.find("th") and "No." in table.text and "Pos." in table.text:  # Check if table contains headers
    #         roster_table = table
    #         break

    if not roster_table:
        print(f"Could not find roster table for {team_wiki_title}")
        return None

    # Extract player names and Wikipedia links
    if sport == "nba":
        players = []
        for row in roster_table.find_all("tr")[2:]:  # Skip header row
            cols = row.find_all("td")
            if len(cols) > 3:
                player_name = cols[2].text.strip()
                player_link = cols[2].find("a")["href"] if cols[2].find("a") else None

                if player_link:
                    player_link = "https://en.wikipedia.org" + player_link  # Make full URL

                player_name = player_name.replace("(TW)", "")
                last_name, first_name = player_name.split(", ")
                player_name = f"{first_name} {last_name}"

                players.append({"Player": player_name, "Wikipedia_Link": player_link})

        return players
    elif sport == "nfl":
        players = []
        for row in roster_table.find_all("tr"):  # Skip header row
            for cols in row.find_all("td"):
                for player in cols.find_all("li")[:-3]:
                    try:
                        player_name = player.find("a").text.strip()
                        player_link = player.find("a")["href"] if player.find("a") else None

                        if player_link:
                            player_link = "https://en.wikipedia.org" + player_link  # Make full URL

                        # player_name = player_name.replace("(TW)", "")
                        # last_name, first_name = player_name.split(", ")
                        # player_name = f"{first_name} {last_name}"

                        players.append({"Player": player_name, "Wikipedia_Link": player_link})
                    except Exception:
                        pass
    elif sport == "epl":
        players = []
        for row in roster_table.find_all("tr")[2:]:  # Skip header row
            cols = row.find_all("td")
            # print([col for col in cols])
            try:
                player_name = cols[3].text.strip()
                player_link = cols[3].find("a")["href"] if cols[3].find("a") else None

                if player_link:
                    player_link = "https://en.wikipedia.org" + player_link  # Make full URL

                player_name = player_name.split("(")[0]
                print(player_name)
                players.append({"Player": player_name, "Wikipedia_Link": player_link})
            except IndexError:
                pass

    return players

# Step 3: Get Wikipedia Pageviews for Each Player
def fetch_pageviews(wikipedia_url):
    """Fetch monthly Wikipedia pageviews for an NBA player."""
    if not wikipedia_url:
        return None  # Skip if no Wikipedia page

    # Extract the Wikipedia title from URL
    wikipedia_title = wikipedia_url.split("/")[-1]

    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{wikipedia_title}/monthly/20240101/20241231"
    headers = {"User-Agent": "MyNBAStatsApp/1.0 (myemail@example.com)"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["items"]
        total_views = sum(item["views"] for item in data)  # Sum up monthly views
        return total_views
    else:
        print(f"Error fetching pageviews for {wikipedia_title}: {response.status_code}")
        return None

# Step 4: Scrape Rosters & Get Player Pageviews
all_team_df = {"Team": [], "Player": [], "Pageviews": []}
all_team_rosters = {}

sport = "nfl"

if sport == "nba":
    teams = nba_teams
elif sport == "nfl":
    teams = nfl_teams
elif sport == "epl":
    teams = epl_teams

for team, wiki_title in teams.items():
    roster = fetch_roster_from_wikipedia(wiki_title, sport)
    if not roster:
        continue  # Skip if no roster found

    team_roster = []
    print(f"\n{team} Roster:")

    for player in roster:
        pageviews = fetch_pageviews(player["Wikipedia_Link"])
        print(f"{player['Player']} - {player['Wikipedia_Link']}: {pageviews if pageviews else 'No data'}")

        team_roster.append({"Player": player["Player"], "Wikipedia_Link": player["Wikipedia_Link"], "Pageviews": pageviews})
        all_team_df["Team"].append(team)
        all_team_df["Player"].append(player["Player"])
        all_team_df["Pageviews"].append(pageviews)
        # print(all_team_df)
        time.sleep(1)  # Sleep to avoid API rate limits

    all_team_rosters[team] = team_roster
    df = pd.DataFrame(all_team_df)
    df.to_csv(f"{sport}.csv")
