# import urllib.parse
# from resources import config as rc
# from sqlalchemy import create_engine, text
# import pandas as pd
# import time


# # Database connection parameters
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

# # Retry logic
# MAX_RETRIES = 3  # Number of times to retry connection
# WAIT_TIME = 3  # Seconds to wait between retries

# for attempt in range(1, MAX_RETRIES + 1):
#     try:
#         print(f"Attempt {attempt} of {MAX_RETRIES} to connect to the database...")
#         with engine.connect() as conn:
#             result = conn.execute(text("SELECT * FROM nba_player"))
#             df = pd.DataFrame(result.fetchall(), columns=result.keys())
#         print("Connection successful!")
#         print(df.head())  # Print first few rows
#         break  # Exit loop on success
#     except Exception as e:
#         print(f"Connection attempt {attempt} failed: {e}")
#         if attempt < MAX_RETRIES:
#             print(f"Retrying in {WAIT_TIME} seconds...")
#             time.sleep(WAIT_TIME)
#         else:
#             print("All connection attempts failed. Please check your database settings.")


# print(df)

import sys
import os
import urllib.parse
import time
import pandas as pd
from sqlalchemy import create_engine, text
from rapidfuzz import process, fuzz

# Ensure the root directory is in sys.path for absolute imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import resources.config as rc  # Import config with credentials

def fetch_data_from_db(query, max_retries=3, wait_time=3):
    """
    Connects to the database and fetches data using the provided SQL query.
    
    Args:
        query (str): SQL query to execute.
        max_retries (int): Number of retries if the connection fails.
        wait_time (int): Seconds to wait before retrying.
    
    Returns:
        pd.DataFrame: A DataFrame containing the query results, or None if the connection fails.
    """
    # Correct ODBC Connection String
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={rc.sql_server};"
        f"DATABASE={rc.sql_database};"
        f"UID={rc.sql_username};"
        f"PWD={rc.sql_password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    # Create SQLAlchemy engine
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

    for attempt in range(1, max_retries + 1):
        try:
            print(f"Attempt {attempt} of {max_retries} to connect to the database...")
            with engine.connect() as conn:
                result = conn.execute(text(query))
                df = pd.DataFrame(result.fetchall(), columns=result.keys())
            print("✅ Connection successful!")
            return df  # Return the DataFrame
        except Exception as e:
            print(f"❌ Connection attempt {attempt} failed: {e}")
            if attempt < max_retries:
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("⛔ All connection attempts failed.")
                return None  # Return None if all attempts fail


def fuzzy_merge(df1, df2, key1, key2, threshold=80):
    """
    Perform a fuzzy merge on two DataFrames based on string similarity.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame.
        key1 (str): Column name in df1 to match.
        key2 (str): Column name in df2 to match.
        threshold (int): Minimum similarity score (0-100).

    Returns:
        pd.DataFrame: Merged DataFrame with best matches.
    """
    matches = []
    
    for name in df1[key1]:
        best_match = process.extractOne(name, df2[key2], scorer=fuzz.ratio)
        
        if best_match and best_match[1] >= threshold:
            matches.append((name, best_match[0], best_match[1]))
    
    matched_df = pd.DataFrame(matches, columns=[key1, key2, "Match Score"])

    # Merge and drop duplicate Player columns
    merged_df = df1.merge(matched_df, on=key1).merge(df2, on=key2)

    # Drop duplicate "Player" columns if they exist
    merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]

    return merged_df

