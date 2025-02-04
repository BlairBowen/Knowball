import requests
import pandas as pd
import pyodbc
from resources import config as rc

headers = {
    "User-Agent": "Knowball/1.0 (ciminibb@mail.uc.edu)"
}

def get_wikimedia_pageviews(title, start_date="20240101", end_date="20240128"):
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{title}/daily/{start_date}/{end_date}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_views = sum(item['views'] for item in data.get('items', []))
        return total_views
    else:
        print(f"Error fetching data for {title}: {response.status_code}")
        return None
    

def get_correct_wikipedia_page(athlete_name, sport="basketball"):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={athlete_name}&format=json"
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        search_results = response.json().get("query", {}).get("search", [])
        
        for result in search_results:
            title = result["title"]
            snippet = result["snippet"].lower()
            
            if sport.lower() in snippet or sport.lower() in title.lower():
                return title 
    
    print(f"Could not find a Wikipedia page for {athlete_name} in {sport}.")
    return None

if __name__ == "__main__":

    import urllib.parse
    import pyodbc
    import pandas as pd
    from sqlalchemy import create_engine, text

    # Database connection parameters
    server = "knowball.database.windows.net"
    database = "knowball-sql"
    username = "kbserver"
    password = "ciminibb$bowenbv$king3ss$"

    # URL Encode Password (if it has special characters)
    encoded_password = urllib.parse.quote_plus(password)

    # ✅ Correct ODBC Connection String
    conn_str = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    # Create SQLAlchemy engine
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

    # ✅ Use `connect()` before executing queries
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT TOP 10 * FROM nba_player"))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df.head())
    except Exception as e:
        print(f"Connection failed: {e}")


    # data = {
    #     "Name": ["Matt Ryan", "Michael Jordan", "LeBron James", "Luka Doncic"],
    #     "Wikipedia Title": [None, None, None, None]  
    # }
    print(df.columns)

    df["Wikipedia Title"] = df["Player"].apply(lambda x: get_correct_wikipedia_page(x, sport="basketball"))
    df["Page Views"] = df["Wikipedia Title"].apply(lambda x: get_wikimedia_pageviews(x) if x else None)

    print(df)