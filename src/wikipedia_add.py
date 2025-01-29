import requests
import pandas as pd

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

    data = {
        "Name": ["Matt Ryan", "Michael Jordan", "LeBron James"],
        "Wikipedia Title": [None, None, None]  
    }
    df = pd.DataFrame(data)

    df["Wikipedia Title"] = df["Name"].apply(lambda x: get_correct_wikipedia_page(x, sport="basketball"))
    df["Page Views"] = df["Wikipedia Title"].apply(lambda x: get_wikimedia_pageviews(x) if x else None)

    print(df)

    # print(get_wikimedia_pageviews(get_correct_wikipedia_page('Matt Ryan')))
