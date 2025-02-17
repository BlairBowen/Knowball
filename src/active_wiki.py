# # # # # import requests
# # # # import pandas as pd
# # # # import time

# # # # # SPARQL endpoint URL
# # # # SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# # # # # Wikipedia Pageviews API
# # # # WIKIPEDIA_PAGEVIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"

# # # # # SPARQL query with LIMIT and OFFSET for pagination
# # # # SPARQL_QUERY_PAGINATED = """
# # # # SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?leagueLabel ?positionLabel WHERE {
# # # #   ?player wdt:P106 wd:Q937857;  # Instance of association football player
# # # #           wdt:P54 ?team;        # Member of sports team
# # # #           wdt:P413 ?position.   # Playing position

# # # #   ?team wdt:P118 ?league.       # Team is in league

# # # #   ?wikiPage schema:about ?player;
# # # #             schema:isPartOf <https://en.wikipedia.org/>;
# # # #             schema:name ?wikiPageTitle.

# # # #   VALUES ?league {wd:Q8170 wd:Q155223 wd:Q9448}  # NFL, NBA, EPL

# # # #   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
# # # # } LIMIT {limit} OFFSET {offset}
# # # # """

# # # # def fetch_active_players_paginated(limit=100):
# # # #     """
# # # #     Fetch all active players from Wikidata using paginated SPARQL queries.
# # # #     """
# # # #     print("🔎 Fetching active players from Wikidata (Paginated)...")

# # # #     all_players = []
# # # #     offset = 0

# # # #     while True:
# # # #         print(f"📥 Fetching players {offset} - {offset + limit}...")

# # # #         # Insert limit and offset values into the query
# # # #         query = SPARQL_QUERY_PAGINATED.format(limit=limit, offset=offset)
# # # #         headers = {"Accept": "application/sparql-results+json"}
# # # #         response = requests.get(SPARQL_ENDPOINT, params={"query": query}, headers=headers)

# # # #         if response.status_code != 200:
# # # #             print(f"❌ HTTP Error {response.status_code} - {response.text[:500]}")
# # # #             break

# # # #         try:
# # # #             data = response.json()
# # # #         except requests.exceptions.JSONDecodeError:
# # # #             print("❌ ERROR: Failed to parse JSON. Skipping batch...")
# # # #             break

# # # #         players = data.get("results", {}).get("bindings", [])
# # # #         if not players:
# # # #             print("✅ No more players found. Pagination complete.")
# # # #             break  # Stop loop if no more players

# # # #         # Convert data to pandas DataFrame
# # # #         df = pd.DataFrame([{
# # # #             "Player": player.get("playerLabel", {}).get("value", "N/A"),
# # # #             "WikipediaTitle": player.get("wikiPage", {}).get("value", "").replace("https://en.wikipedia.org/wiki/", ""),
# # # #             "Team": player.get("teamLabel", {}).get("value", "N/A"),
# # # #             "League": player.get("leagueLabel", {}).get("value", "N/A"),
# # # #             "Position": player.get("positionLabel", {}).get("value", "N/A")
# # # #         } for player in players])

# # # #         all_players.append(df)
# # # #         offset += limit  # Move to the next batch

# # # #         # Respect rate limits (avoid excessive calls)
# # # #         time.sleep(2)

# # # #     final_df = pd.concat(all_players, ignore_index=True) if all_players else None
# # # #     print(f"✅ Successfully retrieved {len(final_df)} players.")
# # # #     return final_df

# # # # def fetch_pageviews_bulk(df, start_date="20240101", end_date="20240201"):
# # # #     """
# # # #     Fetch Wikipedia page views for players using bulk API calls.
# # # #     """
# # # #     print("📊 Fetching Wikipedia pageviews for players...")

# # # #     pageview_data = []
# # # #     total_players = len(df)

# # # #     for index, row in df.iterrows():
# # # #         title = row["WikipediaTitle"]
# # # #         url = WIKIPEDIA_PAGEVIEWS_URL.format(title, start_date, end_date)

# # # #         print(f"🔄 [{index+1}/{total_players}] Fetching views for {row['Player']} ({title})...")

# # # #         response = requests.get(url)
# # # #         if response.status_code == 200:
# # # #             try:
# # # #                 pageviews = response.json()
# # # #                 total_views = sum(item["views"] for item in pageviews.get("items", []))
# # # #                 print(f"   ✅ Retrieved {total_views} views.")
# # # #             except requests.exceptions.JSONDecodeError:
# # # #                 print(f"   ❌ Failed to parse JSON for {title}. Setting views to 0.")
# # # #                 total_views = 0
# # # #         else:
# # # #             total_views = 0
# # # #             print(f"   ❌ Failed to fetch pageviews (HTTP {response.status_code})")

# # # #         pageview_data.append(total_views)

# # # #         # Respect rate limits (avoid excessive calls)
# # # #         time.sleep(0.5)

# # # #     df["TotalPageViews"] = pageview_data
# # # #     print("✅ Wikipedia pageviews fetching completed.")
# # # #     return df

# # # # def save_to_csv(df, filename="active_players_pageviews.csv"):
# # # #     """
# # # #     Save the DataFrame to a CSV file.
# # # #     """
# # # #     print(f"💾 Saving data to {filename}...")
# # # #     df.to_csv(filename, index=False)
# # # #     print("✅ Data successfully saved!")
# # # #     return filename

# # # # # Run the script
# # # # print("🚀 Starting script (Paginated Mode)...")

# # # # players_df = fetch_active_players_paginated(limit=100)  # Fetch players in batches of 100
# # # # if players_df is not None:
# # # #     players_df = fetch_pageviews_bulk(players_df)
# # # #     csv_file = save_to_csv(players_df)

# # # # print("🏁 Script execution completed!")

# # # import requests
# # # import pandas as pd
# # # import time

# # # # SPARQL endpoint URL
# # # SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# # # # Wikipedia Pageviews API
# # # WIKIPEDIA_PAGEVIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"

# # # # SPARQL query template (use f-strings instead of .format())
# # # SPARQL_QUERY_PAGINATED = """
# # # SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?leagueLabel ?positionLabel WHERE {{
# # #   ?player wdt:P106 wd:Q937857;  # Instance of association football player
# # #           wdt:P54 ?team;        # Member of sports team
# # #           wdt:P413 ?position.   # Playing position

# # #   ?team wdt:P118 ?league.       # Team is in league

# # #   ?wikiPage schema:about ?player;
# # #             schema:isPartOf <https://en.wikipedia.org/>;
# # #             schema:name ?wikiPageTitle.

# # #   VALUES ?league {{wd:Q8170 wd:Q155223 wd:Q9448}}  # NFL, NBA, EPL

# # #   SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
# # # }} LIMIT {limit} OFFSET {offset}
# # # """

# # # def fetch_active_players_paginated(limit=100):
# # #     """
# # #     Fetch all active players from Wikidata using paginated SPARQL queries.
# # #     """
# # #     print("🔎 Fetching active players from Wikidata (Paginated)...")

# # #     all_players = []
# # #     offset = 0

# # #     while True:
# # #         print(f"📥 Fetching players {offset} - {offset + limit}...")

# # #         # Use f-string instead of .format() to avoid KeyError
# # #         query = SPARQL_QUERY_PAGINATED.format(limit=limit, offset=offset)
# # #         headers = {"Accept": "application/sparql-results+json"}
# # #         response = requests.get(SPARQL_ENDPOINT, params={"query": query}, headers=headers)

# # #         if response.status_code != 200:
# # #             print(f"❌ HTTP Error {response.status_code} - {response.text[:500]}")
# # #             break

# # #         try:
# # #             data = response.json()
# # #         except requests.exceptions.JSONDecodeError:
# # #             print("❌ ERROR: Failed to parse JSON. Skipping batch...")
# # #             break

# # #         players = data.get("results", {}).get("bindings", [])
# # #         if not players:
# # #             print("✅ No more players found. Pagination complete.")
# # #             break  # Stop loop if no more players

# # #         # Convert data to pandas DataFrame
# # #         df = pd.DataFrame([{
# # #             "Player": player.get("playerLabel", {}).get("value", "N/A"),
# # #             "WikipediaTitle": player.get("wikiPage", {}).get("value", "").replace("https://en.wikipedia.org/wiki/", ""),
# # #             "Team": player.get("teamLabel", {}).get("value", "N/A"),
# # #             "League": player.get("leagueLabel", {}).get("value", "N/A"),
# # #             "Position": player.get("positionLabel", {}).get("value", "N/A")
# # #         } for player in players])

# # #         all_players.append(df)
# # #         offset += limit  # Move to the next batch

# # #         # Respect rate limits (avoid excessive calls)
# # #         time.sleep(2)

# # #     final_df = pd.concat(all_players, ignore_index=True) if all_players else None
# # #     print(f"✅ Successfully retrieved {len(final_df)} players.")
# # #     return final_df

# # # # Run the script
# # # print("🚀 Starting script (Paginated Mode)...")
# # # players_df = fetch_active_players_paginated(limit=100)

# # import requests
# # import pandas as pd
# # import time

# # # SPARQL endpoint URL
# # SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# # # Wikipedia Pageviews API
# # WIKIPEDIA_PAGEVIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"

# # # SPARQL query template with "Played in Competition" filter
# # SPARQL_QUERY_PAGINATED = """
# # SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?leagueLabel ?positionLabel WHERE {{

# #   ?player wdt:P106 wd:Q937857;  # Instance of association football player
# #           wdt:P54 ?team;        # Member of sports team
# #           wdt:P413 ?position.   # Playing position
# #           wdt:P1344 ?competition.  # Player has participated in competition

# #   ?team wdt:P118 ?league.       # Team is in league

# #   ?wikiPage schema:about ?player;
# #             schema:isPartOf <https://en.wikipedia.org/>;
# #             schema:name ?wikiPageTitle.

# #   # Only include major competitions to filter active players
# #   VALUES ?competition {{wd:Q219546 wd:Q842793 wd:Q1326489 wd:Q5369 wd:Q220015 wd:Q83474}}

# #   # Only include teams from NFL, NBA, and EPL
# #   VALUES ?league {{wd:Q8170 wd:Q155223 wd:Q9448}}  

# #   SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
# # }} LIMIT {limit} OFFSET {offset}
# # """

# # def fetch_active_players_paginated(limit=100):
# #     """
# #     Fetch all active players from Wikidata using paginated SPARQL queries.
# #     """
# #     print("🔎 Fetching active players from Wikidata (Paginated)...")

# #     all_players = []
# #     offset = 0

# #     while True:
# #         print(f"📥 Fetching players {offset} - {offset + limit}...")

# #         # Use f-string instead of .format() to avoid KeyError
# #         query = SPARQL_QUERY_PAGINATED.format(limit=limit, offset=offset)
# #         headers = {"Accept": "application/sparql-results+json"}
# #         response = requests.get(SPARQL_ENDPOINT, params={"query": query}, headers=headers)

# #         if response.status_code != 200:
# #             print(f"❌ HTTP Error {response.status_code} - {response.text[:500]}")
# #             break

# #         try:
# #             data = response.json()
# #         except requests.exceptions.JSONDecodeError:
# #             print("❌ ERROR: Failed to parse JSON. Skipping batch...")
# #             break

# #         players = data.get("results", {}).get("bindings", [])
# #         if not players:
# #             print("✅ No more players found. Pagination complete.")
# #             break  # Stop loop if no more players

# #         # Convert data to pandas DataFrame
# #         df = pd.DataFrame([{
# #             "Player": player.get("playerLabel", {}).get("value", "N/A"),
# #             "WikipediaTitle": player.get("wikiPage", {}).get("value", "").replace("https://en.wikipedia.org/wiki/", ""),
# #             "Team": player.get("teamLabel", {}).get("value", "N/A"),
# #             "League": player.get("leagueLabel", {}).get("value", "N/A"),
# #             "Position": player.get("positionLabel", {}).get("value", "N/A")
# #         } for player in players])

# #         all_players.append(df)
# #         offset += limit  # Move to the next batch

# #         # Respect rate limits (avoid excessive calls)
# #         time.sleep(2)

# #     final_df = pd.concat(all_players, ignore_index=True) if all_players else None
# #     print(f"✅ Successfully retrieved {len(final_df)} players.")
# #     return final_df

# # def fetch_pageviews_bulk(df, start_date="20240101", end_date="20240201"):
# #     """
# #     Fetch Wikipedia page views for players using bulk API calls.
# #     """
# #     print("📊 Fetching Wikipedia pageviews for players...")

# #     pageview_data = []
# #     total_players = len(df)

# #     for index, row in df.iterrows():
# #         title = row["WikipediaTitle"]
# #         url = WIKIPEDIA_PAGEVIEWS_URL.format(title, start_date, end_date)

# #         print(f"🔄 [{index+1}/{total_players}] Fetching views for {row['Player']} ({title})...")

# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             try:
# #                 pageviews = response.json()
# #                 total_views = sum(item["views"] for item in pageviews.get("items", []))
# #                 print(f"   ✅ Retrieved {total_views} views.")
# #             except requests.exceptions.JSONDecodeError:
# #                 print(f"   ❌ Failed to parse JSON for {title}. Setting views to 0.")
# #                 total_views = 0
# #         else:
# #             total_views = 0
# #             print(f"   ❌ Failed to fetch pageviews (HTTP {response.status_code})")

# #         pageview_data.append(total_views)

# #         # Respect rate limits (avoid excessive calls)
# #         time.sleep(0.5)

# #     df["TotalPageViews"] = pageview_data
# #     print("✅ Wikipedia pageviews fetching completed.")
# #     return df

# # def save_to_csv(df, filename="active_players_pageviews.csv"):
# #     """
# #     Save the DataFrame to a CSV file.
# #     """
# #     print(f"💾 Saving data to {filename}...")
# #     df.to_csv(filename, index=False)
# #     print("✅ Data successfully saved!")
# #     return filename

# # # Run the script
# # print("🚀 Starting script (Paginated Mode)...")

# # players_df = fetch_active_players_paginated(limit=100)  # Fetch players in batches of 100
# # if players_df is not None:
# #     players_df = fetch_pageviews_bulk(players_df)
# #     csv_file = save_to_csv(players_df)

# # print("🏁 Script execution completed!")

# import requests
# import pandas as pd
# import time

# # SPARQL endpoint URL
# SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# # Wikipedia Pageviews API
# WIKIPEDIA_PAGEVIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"

# # SPARQL query template (fixed with OPTIONAL filters)
# SPARQL_QUERY_PAGINATED = """
# SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?leagueLabel ?positionLabel WHERE {{

#   ?player wdt:P106 wd:Q937857;  # Instance of association football player
#           wdt:P54 ?team;        # Member of sports team
#           wdt:P413 ?position.   # Playing position

#   OPTIONAL {{
#     ?player wdt:P1344 ?competition.  # Player has participated in competition (if available)
#   }}

#   ?team wdt:P118 ?league.  # Team is in a league

#   OPTIONAL {{
#     ?wikiPage schema:about ?player;
#               schema:isPartOf <https://en.wikipedia.org/>;
#               schema:name ?wikiPageTitle.
#   }}

#   # Only include major competitions to filter active players
#   VALUES ?competition {{wd:Q219546 wd:Q842793 wd:Q1326489 wd:Q5369 wd:Q220015 wd:Q83474}}

#   # Only include teams from NFL, NBA, and EPL
#   VALUES ?league {{wd:Q8170 wd:Q155223 wd:Q9448}}  

#   SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
# }} LIMIT {limit} OFFSET {offset}
# """

# def fetch_active_players_paginated(limit=100, debug=False):
#     """
#     Fetch all active players from Wikidata using paginated SPARQL queries.
#     """
#     print("🔎 Fetching active players from Wikidata (Paginated)...")

#     all_players = []
#     offset = 0

#     while True:
#         print(f"📥 Fetching players {offset} - {offset + limit}...")

#         # Use f-string instead of .format() to avoid KeyError
#         query = SPARQL_QUERY_PAGINATED.format(limit=limit, offset=offset)

#         if debug:
#             print("🔍 SPARQL Query Sent:\n", query)  # Debugging line

#         headers = {"Accept": "application/sparql-results+json"}
#         response = requests.get(SPARQL_ENDPOINT, params={"query": query}, headers=headers)

#         if response.status_code != 200:
#             print(f"❌ HTTP Error {response.status_code} - {response.text[:500]}")
#             break

#         try:
#             data = response.json()
#         except requests.exceptions.JSONDecodeError:
#             print("❌ ERROR: Failed to parse JSON. Skipping batch...")
#             break

#         players = data.get("results", {}).get("bindings", [])
#         print(players)
#         if not players:
#             print("✅ No more players found. Pagination complete.")
#             break  # Stop loop if no more players

#         # Convert data to pandas DataFrame
#         df = pd.DataFrame([{
#             "Player": player.get("playerLabel", {}).get("value", "N/A"),
#             "WikipediaTitle": player.get("wikiPage", {}).get("value", "").replace("https://en.wikipedia.org/wiki/", ""),
#             "Team": player.get("teamLabel", {}).get("value", "N/A"),
#             "League": player.get("leagueLabel", {}).get("value", "N/A"),
#             "Position": player.get("positionLabel", {}).get("value", "N/A")
#         } for player in players])

#         all_players.append(df)
#         offset += limit  # Move to the next batch

#         # Respect rate limits (avoid excessive calls)
#         df.head()
#         time.sleep(2)

#     if all_players:
#         final_df = pd.concat(all_players, ignore_index=True)
#         print(f"✅ Successfully retrieved {len(final_df)} players.")
#     else:
#         final_df = pd.DataFrame()  # Return empty DataFrame to avoid NoneType error
#         print("❌ No players found. Returning empty DataFrame.")

#     return final_df

# def fetch_pageviews_bulk(df, start_date="20240101", end_date="20240201"):
#     """
#     Fetch Wikipedia page views for players using bulk API calls.
#     """
#     print("📊 Fetching Wikipedia pageviews for players...")

#     pageview_data = []
#     total_players = len(df)

#     for index, row in df.iterrows():
#         title = row["WikipediaTitle"]
#         url = WIKIPEDIA_PAGEVIEWS_URL.format(title, start_date, end_date)

#         print(f"🔄 [{index+1}/{total_players}] Fetching views for {row['Player']} ({title})...")

#         response = requests.get(url)
#         if response.status_code == 200:
#             try:
#                 pageviews = response.json()
#                 total_views = sum(item["views"] for item in pageviews.get("items", []))
#                 print(f"   ✅ Retrieved {total_views} views.")
#             except requests.exceptions.JSONDecodeError:
#                 print(f"   ❌ Failed to parse JSON for {title}. Setting views to 0.")
#                 total_views = 0
#         else:
#             total_views = 0
#             print(f"   ❌ Failed to fetch pageviews (HTTP {response.status_code})")

#         pageview_data.append(total_views)

#         # Respect rate limits (avoid excessive calls)
#         time.sleep(0.5)

#     df["TotalPageViews"] = pageview_data
#     print("✅ Wikipedia pageviews fetching completed.")
#     return df

# def save_to_csv(df, filename="active_players_pageviews.csv"):
#     """
#     Save the DataFrame to a CSV file.
#     """
#     print(f"💾 Saving data to {filename}...")
#     df.to_csv(filename, index=False)
#     print("✅ Data successfully saved!")
#     return filename

# # Run the script
# print("🚀 Starting script (Paginated Mode)...")

# players_df = fetch_active_players_paginated(limit=100, debug=False)  # Fetch players in batches of 100
# if not players_df.empty:
#     players_df = fetch_pageviews_bulk(players_df)
#     csv_file = save_to_csv(players_df)

# print("🏁 Script execution completed!")

import requests
import pandas as pd
import time

# SPARQL endpoint URL
SPARQL_ENDPOINT = "https://query.wikidata.org/sparql"

# Wikipedia Pageviews API
WIKIPEDIA_PAGEVIEWS_URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{}/daily/{}/{}"

# Wikidata Q-IDs for Leagues
LEAGUE_QIDS = {
    "NBA": "Q155223",
    "NFL": "Q8170",
    "EPL": "Q9448"
}

# SPARQL query template with parameterized league selection
SPARQL_QUERY_PAGINATED = """
SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?leagueLabel ?positionLabel WHERE {{

  ?player wdt:P106 wd:Q937857;  # Instance of association football player
          wdt:P54 ?team;        # Member of sports team
          wdt:P413 ?position.   # Playing position

  OPTIONAL {{
    ?player wdt:P1344 ?competition.  # Player has participated in competition (if available)
  }}

  ?team wdt:P118 ?league.  # Team is in a league

  OPTIONAL {{
    ?wikiPage schema:about ?player;
              schema:isPartOf <https://en.wikipedia.org/>;
              schema:name ?wikiPageTitle.
  }}

  # Filter only the selected league
  VALUES ?league {{wd:{league_qid}}}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
}} LIMIT {limit} OFFSET {offset}
"""

SPARQL_QUERY_NBA_ACTIVE = """
SELECT ?player ?playerLabel ?wikiPage ?teamLabel ?positionLabel WHERE {{

  # Must be an instance of a basketball player
  ?player wdt:P106 wd:Q3665646;  # Basketball player profession

  # Must currently be on an NBA team
  ?player wdt:P54 ?team.
  ?team wdt:P118 wd:Q155223.  # Team is part of NBA

  # Ensure player is part of the current NBA season
  ?player wdt:P1344 ?competition.
  ?competition wdt:P31 wd:Q27020041.  # Competition is a basketball season

  # Position information
  OPTIONAL {{ ?player wdt:P413 ?position. }}

  # Wikipedia page information
  OPTIONAL {{ 
    ?wikiPage schema:about ?player;
              schema:isPartOf <https://en.wikipedia.org/>;
              schema:name ?wikiPageTitle.
  }}

  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
}} LIMIT {limit} OFFSET {offset}
"""


def fetch_active_players_paginated(league="NBA", limit=100, debug=False):
    """
    Fetch all active players from Wikidata for a specific league using paginated SPARQL queries.
    """
    if league not in LEAGUE_QIDS:
        raise ValueError(f"Invalid league: {league}. Choose from {list(LEAGUE_QIDS.keys())}")

    print(f"🔎 Fetching active players from Wikidata (League: {league})...")

    all_players = []
    offset = 0
    league_qid = LEAGUE_QIDS[league]  # Get the Wikidata Q-ID for the league

    while True:
        print(f"📥 Fetching players {offset} - {offset + limit}...")

        # Format the SPARQL query with the selected league
        # query = SPARQL_QUERY_PAGINATED.format(league_qid=league_qid, limit=limit, offset=offset)
        query = SPARQL_QUERY_NBA_ACTIVE.format(limit=limit, offset=offset)

        if debug:
            print("🔍 SPARQL Query Sent:\n", query)

        headers = {"Accept": "application/sparql-results+json"}
        response = requests.get(SPARQL_ENDPOINT, params={"query": query}, headers=headers)

        if response.status_code != 200:
            print(f"❌ HTTP Error {response.status_code} - {response.text[:500]}")
            break

        try:
            data = response.json()
        except requests.exceptions.JSONDecodeError:
            print("❌ ERROR: Failed to parse JSON. Skipping batch...")
            break

        players = data.get("results", {}).get("bindings", [])
        if not players:
            print("✅ No more players found. Pagination complete.")
            break  # Stop loop if no more players

        # Convert data to pandas DataFrame
        df = pd.DataFrame([{
            "Player": player.get("playerLabel", {}).get("value", "N/A"),
            "WikipediaTitle": player.get("wikiPage", {}).get("value", "").replace("https://en.wikipedia.org/wiki/", ""),
            "Team": player.get("teamLabel", {}).get("value", "N/A"),
            "League": player.get("leagueLabel", {}).get("value", "N/A"),
            "Position": player.get("positionLabel", {}).get("value", "N/A")
        } for player in players])

        all_players.append(df)
        print(df.head())
        offset += limit  # Move to the next batch

        # Respect rate limits (avoid excessive calls)
        time.sleep(2)

    if all_players:
        final_df = pd.concat(all_players, ignore_index=True)
        print(f"✅ Successfully retrieved {len(final_df)} players.")
    else:
        final_df = pd.DataFrame()  # Return empty DataFrame to avoid NoneType error
        print("❌ No players found. Returning empty DataFrame.")

    # Print first and last player for verification
    if not final_df.empty:
        print(f"🔝 First Player: {final_df.iloc[0]['Player']}")
        print(f"🔚 Last Player: {final_df.iloc[-1]['Player']}")

    return final_df

def fetch_pageviews_bulk(df, start_date="20240101", end_date="20240201"):
    """
    Fetch Wikipedia page views for players using bulk API calls.
    """
    print("📊 Fetching Wikipedia pageviews for players...")

    pageview_data = []
    total_players = len(df)

    for index, row in df.iterrows():
        title = row["WikipediaTitle"]
        url = WIKIPEDIA_PAGEVIEWS_URL.format(title, start_date, end_date)

        print(f"🔄 [{index+1}/{total_players}] Fetching views for {row['Player']} ({title})...")

        response = requests.get(url)
        if response.status_code == 200:
            try:
                pageviews = response.json()
                total_views = sum(item["views"] for item in pageviews.get("items", []))
                print(f"   ✅ Retrieved {total_views} views.")
            except requests.exceptions.JSONDecodeError:
                print(f"   ❌ Failed to parse JSON for {title}. Setting views to 0.")
                total_views = 0
        else:
            total_views = 0
            print(f"   ❌ Failed to fetch pageviews (HTTP {response.status_code})")

        pageview_data.append(total_views)

        # Respect rate limits (avoid excessive calls)
        time.sleep(0.5)

    df["TotalPageViews"] = pageview_data
    print("✅ Wikipedia pageviews fetching completed.")
    return df

def save_to_csv(df, filename="active_players_pageviews.csv"):
    """
    Save the DataFrame to a CSV file.
    """
    print(f"💾 Saving data to {filename}...")
    df.to_csv(filename, index=False)
    print("✅ Data successfully saved!")
    return filename

# Run the script for NBA only
print("🚀 Starting script (NBA Mode)...")

players_df = fetch_active_players_paginated(league="NBA", limit=100, debug=False)  # Fetch only NBA players
if not players_df.empty:
    players_df = fetch_pageviews_bulk(players_df)
    csv_file = save_to_csv(players_df)

print("🏁 Script execution completed!")
