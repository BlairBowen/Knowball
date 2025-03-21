import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
import unicodedata

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


def fetch_roster_from_wikipedia(team_wiki_title, sport):
    """Scrape the roster from a team's Wikipedia page, including player Wikipedia links."""
    
    url = f"https://en.wikipedia.org/wiki/{team_wiki_title}"
    headers = {"User-Agent": "MySportsStatsApp/1.0 (myemail@example.com)"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching {team_wiki_title}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Determine the correct roster table based on the sport
    roster_table = None
    if sport == "epl":
        roster_table = soup.find("table", {"role": "presentation"})
    else:
        for table in soup.find_all("table", {"class": "toccolours"}):
            caption = table.find("caption")
            if caption and "roster" in caption.text.lower():
                roster_table = table
                break

    if not roster_table:
        print(f"Could not find roster table for {team_wiki_title}")
        return None
    


    # Extract players based on sport
    if sport == "nba":
        return extract_nba_players(roster_table)
    elif sport == "nfl":
        return extract_nfl_players(roster_table)
    elif sport == "epl":
        return extract_epl_players(roster_table)
    else:
        print(f"Sport '{sport}' not supported.")
        return None


def extract_nba_players(roster_table):
    """Extract NBA player names and Wikipedia links from the roster table."""
    players = []
    for row in roster_table.find_all("tr")[2:]:  # Skip header row
        cols = row.find_all("td")
        if len(cols) > 3:
            player_name = cols[2].text.strip()
            print(player_name)
            player_link = cols[2].find("a")["href"] if cols[2].find("a") else None

            if player_link:
                player_link = "https://en.wikipedia.org" + player_link  # Make full URL

            # Format player name (convert "Last, First" to "First Last")
            player_name = player_name.replace(". ", ".")
            player_name = " ".join(unicodedata.normalize("NFKC", player_name).split())
            player_name = re.sub(r"\(.*?\)", "", player_name).strip()
            
            if ", " in player_name:
                last_name, first_name = player_name.split(", ")
                try:
                    first_name, suffix = first_name.split(" ")
                    suffix = " " + suffix
                except Exception:
                    suffix = ""
                player_name = f"{first_name} {last_name}{suffix}"

            players.append({"Player": player_name, "Wikipedia_Link": player_link})

    return players


def extract_nfl_players(roster_table):
    """Extract NFL player names and Wikipedia links from the roster table."""
    players = []
    for row in roster_table.find_all("tr"):
        for cols in row.find_all("td"):
            for player in cols.find_all("li"):
                if not player.find_parent("div", class_="hlist"):  # Exclude hlist divs
                    try:
                        player_name = player.find("a").text.strip()
                        player_link = player.find("a")["href"] if player.find("a") else None

                        if player_link:
                            player_link = "https://en.wikipedia.org" + player_link  # Make full URL

                        players.append({"Player": player_name, "Wikipedia_Link": player_link})
                    except AttributeError:
                        pass  # Skip if <a> tag is missing

    return players


def extract_epl_players(roster_table):
    """Extract EPL player names and Wikipedia links from the roster table."""
    players = []
    for row in roster_table.find_all("tr")[2:]:  # Skip header row
        cols = row.find_all("td")
        try:
            player_name = cols[3].text.strip().split(" (")[0]  # Remove extra text
            player_link = cols[3].find("a")["href"] if cols[3].find("a") else None

            if player_link:
                player_link = "https://en.wikipedia.org" + player_link  # Make full URL

            players.append({"Player": player_name, "Wikipedia_Link": player_link})
        except IndexError:
            pass  # Skip rows with missing data

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


def scrape_pageviews(sport):
    # Mapping sports to team lists
    sport_teams = {
        "nba": nba_teams,
        "nfl": nfl_teams,
        "epl": epl_teams
    }

    teams = sport_teams.get(sport, {})

    all_team_data = []
    team_pageviews_data = []

    for team, wiki_title in teams.items():
        roster = fetch_roster_from_wikipedia(wiki_title, sport)
        if not roster:
            continue  # Skip teams without a roster

        print(f"\n{team} Roster:")
        
        team_roster = [
            {
                "Player": player["Player"],
                "Wikipedia_Link": player["Wikipedia_Link"],
                # "Pageviews": None
                "Pageviews": fetch_pageviews(player["Wikipedia_Link"])
            }
            for player in roster
        ]

        for player_data in team_roster:
            print(f"{player_data['Player']} - {player_data['Wikipedia_Link']}: {player_data['Pageviews'] or 'No data'}")

        all_team_data.extend([{"Team": team, **player_data} for player_data in team_roster])
        team_pageviews = fetch_pageviews(f"https://en.wikipedia.org/wiki/{wiki_title}")
        team_pageviews_data.append({"Team": team, "Pageviews": team_pageviews})
        print(f"Team: {team} - Pageviews: {team_pageviews}")

        time.sleep(1)  # Sleep to avoid API rate limits

    # Convert to DataFrame and save
    df = pd.DataFrame(all_team_data)
    df.to_csv(f"complete_{sport}_roster.csv", index=False)
    team_df = pd.DataFrame(team_pageviews_data)
    team_df.to_csv(f"{sport}_team_pageviews.csv", index=False)

    

    #     # Database connection parameters
    # server = "knowball.database.windows.net"
    # database = "knowball-sql"
    # username = "kbserver"
    # password = "ciminibb$bowenbv$king3ss$"

    # # URL Encode Password (if it has special characters)
    # encoded_password = urllib.parse.quote_plus(password)

    # # ✅ Correct ODBC Connection String
    # conn_str = (
    #     "DRIVER={ODBC Driver 18 for SQL Server};"
    #     f"SERVER={rc.sql_server};"
    #     f"DATABASE={rc.sql_database};"
    #     f"UID={rc.sql_username};"
    #     f"PWD={rc.sql_password};"
    #     "Encrypt=yes;"
    #     "TrustServerCertificate=no;"
    #     "Connection Timeout=30;"
    # )

    # # Create SQLAlchemy engine
    # engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

    # # ✅ Use `connect()` before executing queries
    # try:
    #     with engine.connect() as conn:
    #         result = conn.execute(text("SELECT * FROM nba_player"))
    #         df = pd.DataFrame(result.fetchall(), columns=result.keys())
    #     print(df.head())
    # except Exception as e:
    #     print(f"Connection failed: {e}")
