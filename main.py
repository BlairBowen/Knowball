from src.pageview_scrape import scrape_pageviews
from src.unsupervised_learning import fetch_data_from_db, fuzzy_merge_best_available
from resources.config import nba_team_mapping, nfl_team_mapping, epl_team_mapping
import pandas as pd


if __name__ == "__main__":
    pass

    # sport = "nba"

    # # scrape_pageviews(sport)

    # query = f"SELECT * FROM {sport}_player"
    # database_df = fetch_data_from_db(query)

    # database_df = database_df[database_df.columns[:-2]]

    # database_df.to_csv(f"database_{sport}.csv")

    # local_df = pd.read_csv(f"complete_{sport}_roster.csv")

    # database_df = database_df.rename(columns={
    #     "Player": "Player_df1", 
    #     "Team": "Team_df1"
    #     })
    # local_df = local_df.rename(columns={
    #     "Player": "Player_df2", 
    #     "Team": "Team_df2"
    #     })

    # if sport == "nba":
    #     team_mapping = nba_team_mapping
    # if sport == "nfl":
    #     team_mapping = nfl_team_mapping
    # if sport == "epl":
    #     team_mapping = epl_team_mapping

    # merged_df = fuzzy_merge_best_available(database_df, local_df, "Player_df1", "Player_df2", "Team_df1", "Team_df2", team_mapping)

    # merged_df.to_csv(f"merged_{sport}.csv")
    
    # # duplicate_players = merged_df["Player_df1_x"].value_counts()
    # # duplicate_players = duplicate_players[duplicate_players > 1].index  # Get the names of duplicates

    # # # Filter the DataFrame to show only rows where "Player" is a duplicate
    # # duplicate_rows = merged_df[merged_df["Player_df1_x"].isin(duplicate_players)]

    # # print(duplicate_rows.columns)

    # # # Display the duplicated rows
    # # print(duplicate_rows[["Player_df2_x", "Team_df2_x"]])

    # team_df = pd.read_csv(f"{sport}_team_pageviews.csv").rename(columns={"Pageviews": "Team_Pageviews"})
    # df = pd.read_csv(f"merged_{sport}.csv")

    # merged_df = pd.merge(df, team_df, left_on="Team_df2_x", right_on="Team", how="inner").drop(columns=["Team"])
    # # merged_df = merged_df.drop(columns=["Team"])
    # merged_df.to_csv(f"merged_{sport}.csv")

