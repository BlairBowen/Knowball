import requests
import pandas as pd
import pyodbc
from resources import config as rc
from fuzzywuzzy import fuzz

pat = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI4NGU4MjIxYzgwZDMyZDEzOGRmYWZiNDczOTAyY2IyNiIsImp0aSI6ImRlZTBlY2FjNjcxNTJhNjNlZjlhMmEyYjI4M2ZhN2VkNzRhYjcwYjcxNWYwN2Q4MGIyYzBhZGI2NTYyZTg1MWY4NjMxMWEyOGFlZGI3MzlkIiwiaWF0IjoxNzM4NzgxMjY4LjE3ODc1OCwibmJmIjoxNzM4NzgxMjY4LjE3ODc2MiwiZXhwIjozMzI5NTY5MDA2OC4xNzYzMDgsInN1YiI6Ijc3NTcxMTgyIiwiaXNzIjoiaHR0cHM6Ly9tZXRhLndpa2ltZWRpYS5vcmciLCJyYXRlbGltaXQiOnsicmVxdWVzdHNfcGVyX3VuaXQiOjUwMDAsInVuaXQiOiJIT1VSIn0sInNjb3BlcyI6WyJiYXNpYyJdfQ.qGzdRuRaBw2KPnw0jKjkR8TP7vjgEODTjnX0jVmzVJ03dO12FbBvX0K3zpI5QyxsT3ro7Lp2gPgHyWVTygLybjBKfhzkncI5qagWIxpSr9JTuuF7kE95ZURLel_JVnABOkn98ylm_iD7ZDis4IpFxSI79x0F-0icdfm3eZBeLqOrWb4YW3qsAroD2ljitn42R49AXypf9VVf8PDs36lw6bmS4JUCO6_mf-fbyMefqdfDO-FsmRRUNjX5bUTuxSzbSRR9vgJs0txN0xJiPHPmg8MHmORWfqYJtFYJPpGnMDf8nx08HmLwvr0LmqwnsW6YRE6BolfoG9fP2zNQU3XKjhIhJpNxissoGF20ITDhrQbykzInRzyACFX3A6-GyYjQZuxTw51JQfVB163d94pnBD4q0oCU2ayFhApVVpl-HrNsjL3LGHt9FSD-Kc8Hr233xVNywTe4-MBliS6i92ZOSoKXMPVFOqmAi_llmMbiQ_7lO8BYFx5RGcaolK3LAkphkbcS0WPhQ_2b3x7qsg2UHo182ODrJ_NIT6PZnX6neTbOsCWqAHS7TnSaYFpEwXVF1wWeEN5LLoO1oSuLtxjR_nw5ebZf0Wc2ByIVYPcrghfkH9kMlwc5GfSSthfEGLtzKlBrWXt6dcXlZTleXeaHWXDAVRRWQ0ZlTtHknK2a0AMw'

# headers = {
#     "User-Agent": "Knowball/1.0 (ciminibb@mail.uc.edu)",
#     'Authorization': f'Bearer {pat}'
# }

# def get_wikimedia_pageviews(title, start_date="20240101", end_date="20240128"):
#     url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{title}/daily/{start_date}/{end_date}"
    
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         total_views = sum(item['views'] for item in data.get('items', []))
#         return total_views
#     else:
#         print(f"Error fetching data for {title}: {response.status_code}")
#         return None
    

# def get_correct_wikipedia_page(athlete_name, sport="basketball"):
#     search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={athlete_name}&format=json"
    
#     response = requests.get(search_url, headers=headers)
#     print(response)
#     if response.status_code == 200:
#         search_results = response.json().get("query", {}).get("search", [])
        
#         for result in search_results:
#             title = result["title"]
#             snippet = result["snippet"].lower()
            
#             if sport.lower() in snippet or sport.lower() in title.lower():
#                 return title 
    
#     print(f"Could not find a Wikipedia page for {athlete_name} in {sport}.")
#     return None

# if __name__ == "__main__":

#     import urllib.parse
#     import pyodbc
#     import pandas as pd
#     from sqlalchemy import create_engine, text

#     # Database connection parameters
#     server = "knowball.database.windows.net"
#     database = "knowball-sql"
#     username = "kbserver"
#     password = "ciminibb$bowenbv$king3ss$"

#     # URL Encode Password (if it has special characters)
#     encoded_password = urllib.parse.quote_plus(password)

#     # ✅ Correct ODBC Connection String
#     conn_str = (
#         "DRIVER={ODBC Driver 18 for SQL Server};"
#         f"SERVER={rc.sql_server};"
#         f"DATABASE={rc.sql_database};"
#         f"UID={rc.sql_username};"
#         f"PWD={rc.sql_password};"
#         "Encrypt=yes;"
#         "TrustServerCertificate=no;"
#         "Connection Timeout=30;"
#     )

#     # Create SQLAlchemy engine
#     engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")

#     # ✅ Use `connect()` before executing queries
#     try:
#         with engine.connect() as conn:
#             result = conn.execute(text("SELECT TOP 10 * FROM nba_player"))
#             df = pd.DataFrame(result.fetchall(), columns=result.keys())
#         print(df.head())
#     except Exception as e:
#         print(f"Connection failed: {e}")


#     data = {
#         "Name": ["Matt Ryan", "Michael Jordan", "LeBron James", "Luka Doncic"],
#         "Wikipedia Title": [None, None, None, None]  
#     }

#     df = pd.DataFrame(data)
#     print(df.columns)

#     df["Wikipedia Title"] = df["Name"].apply(lambda x: get_correct_wikipedia_page(x, sport="basketball"))
#     df["Page Views"] = df["Wikipedia Title"].apply(lambda x: get_wikimedia_pageviews(x) if x else None)

#     df.to_csv('example.csv')
#     print(df)

# Function to get Wikimedia page views
def get_wikimedia_pageviews(title, start_date="20240101", end_date="20240128"):
    url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{title}/daily/{start_date}/{end_date}"
    
    headers = {
        "User-Agent": "Knowball/1.0 (ciminibb@mail.uc.edu)",
        'Authorization': f'Bearer {pat}'
    }

    print(title)

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        total_views = sum(item['views'] for item in data.get('items', []))
        return total_views
    elif response.status_code == 403:
        print(f"403 Forbidden: Wikimedia API blocked the request for {title}. Check User-Agent header.")
        return None
    else:
        print(f"Error fetching data for {title}: {response.status_code}")
        return None

# Function to find the correct Wikipedia title for an athlete
def get_correct_wikipedia_page(athlete_name, sport="basketball"):
    search_url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={athlete_name}&format=json"
    
    headers = {
        "User-Agent": "Knowball/1.0 (ciminibb@mail.uc.edu)",
        # 'Authorization': f'Bearer {pat}'
    }

    print(athlete_name)
    result_list = []

    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        search_results = response.json().get("query", {}).get("search", [])
        
        for result in search_results:
            title = result["title"]
            snippet = result["snippet"].lower()
            result_list.append([title, snippet])
            
        check = 0

        while len(result_list) > 1:
            print(len(result_list))
            result_list = []
            for result in result_list:
                print(result)
                if check == 0:
                    print(fuzz.ratio(result[0].split(' (')[0], athlete_name))
                    if fuzz.ratio(result[0].split(' (')[0], athlete_name) > 90:
                        result_list.append(result)
                elif check == 1:
                    if sport.lower() in snippet or sport.lower() in title.lower():
                        result_list.append(result)
                else:
                    break
            check += 1
                
        if len(result_list) > 0:
            print(result_list[0])
            return result_list[0]
        else:
            print("Couldn't Find")
            return None
                
    
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

    # ✅ Use `connect()` before executing queries
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT TOP 10 * FROM nba_player"))
            df = pd.DataFrame(result.fetchall(), columns=result.keys())
        print(df.head())
    except Exception as e:
        print(f"Connection failed: {e}")

    # # Example: Pre-existing DataFrame (assuming it has athlete names)
    # data = {
    #     "Name": ["Matt Ryan", "Michael Jordan", "LeBron James"],
    #     "Wikipedia Title": [None, None, None]  # Placeholder for Wikipedia page titles
    # }
    # df = pd.DataFrame(data)

    # Update Wikipedia Title and fetch Page Views
    df["Wikipedia Title"] = df["Player"].apply(lambda x: get_correct_wikipedia_page(x, sport="basketball"))
    # df["Wiki"] = df["Wikipedia Title"].apply(lambda x: get_wikimedia_pageviews(x) if x else None)

    df.to_csv('example.csv')
    # print(df.shape)
    print(df)

