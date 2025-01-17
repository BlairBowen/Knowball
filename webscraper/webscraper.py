import os
import random
import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

domain = {
    'NBA': "https://www.basketball-reference.com",
    'NFL': "https://www.pro-football-reference.com",
}

NBA_TEAMS = [
    # "BOS",
    # "NYK",
    # "PHI",
    # "BRK",
    # "TOR",
    # "CLE",
    # "MIL",
    # "IND",
    # "DET",
    # "CHI",
    # "ORL",
    # "MIA",
    "ATL",
    # "CHO",
    # "WAS",
    # "OKC",
    # "DEN",
    # "MIN",
    # "POR",
    # "UTA",
    # "LAL",
    # "LAC",
    # "GSW",
    # "SAC",
    # "PHO",
    # "HOU",
    # "MEM",
    # "DAL",
    # "SAS",
    # "NOP",
]

NFL_TEAMS = [
    "buf",
    "mia",
    "nyj",
    "nwe",
    "rav",
    "pit",
    "cin",
    "cle",
    "htx",
    "clt",
    "jax",
    "oti",
    "kan",
    "sdg",
    "den",
    "rai",
    "phi",
    "was",
    "dal",
    "nyg",
    "det",
    "min",
    "gnb",
    "chi",
    "tam",
    "atl",
    "car",
    "nor",
    "ram",
    "sea",
    "crd",
    "sfo"
]

# Set up the WebDriver (use the appropriate driver for your browser)
service = Service(
    "Knowball\\webscraper\\chromedriver-win64\\chromedriver.exe"
)
options = webdriver.ChromeOptions()

# Uncomment the next line to run the browser in headless mode
# options.add_argument('--headless')

# Add User-Agent to mimic a real browser
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
)

# Enable browser automation flags
options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize the driver
driver = webdriver.Chrome(service=service, options=options)

# Disable detection of WebDriver
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });
    """
    },
)


def get_html_and_interact(url, interaction=None):
    """
    Fetches the HTML of the page and allows interactions like clicking or navigating.

    :param url: URL of the webpage to open
    :param interaction: Function for interactions to perform (optional)
    """
    try:
        # Open the webpage
        driver.get(url)
        random_delay(2, 7)  # Wait for the page to load

        # Perform human-like interactions
        human_like_interaction(driver)

        # Get the HTML of the page
        page_html = driver.page_source
        print("Page HTML fetched successfully!")

        # Perform interactions if specified
        if interaction:
            interaction(driver)

        return page_html

    except Exception as e:
        print(f"An error occurred: {e}")


def random_delay(min_seconds=2, max_seconds=5):
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)


# Function to perform human-like actions
def human_like_interaction(driver):
    try:
        # Scroll randomly
        for _ in range(random.randint(1, 3)):
            scroll_distance = random.randint(200, 1000)
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            random_delay(1, 3)

        # Move the mouse
        action = ActionChains(driver)
        body = driver.find_element(By.TAG_NAME, "body")
        action.move_to_element_with_offset(
            body, random.randint(1, 500), random.randint(1, 500)
        ).perform()
        random_delay(1, 3)

        # Perform a slight page interaction (hover over a random element if possible)
        links = driver.find_elements(By.TAG_NAME, "a")
        if links:
            random_link = random.choice(links)
            action.move_to_element(random_link).perform()
            random_delay(1, 3)
    except Exception as e:
        print(f"Human-like interaction failed: {e}")


# Rate-limiting function
def rate_limited_request(interval, func, *args, **kwargs):
    """
    Ensures that requests to a website are made at a controlled rate.

    :param interval: Time in seconds between requests.
    :param func: Function to execute.
    :param args: Positional arguments for the function.
    :param kwargs: Keyword arguments for the function.
    """
    rate_limited_request.last_called = getattr(
        rate_limited_request, "last_called", time.time() - interval
    )
    elapsed = time.time() - rate_limited_request.last_called
    if elapsed < interval:
        time.sleep(interval - elapsed)
    result = func(*args, **kwargs)
    rate_limited_request.last_called = time.time()
    return result


def get_team_pages(sport, teams, year):
    if sport == 'NBA':
        year_link = year
    elif sport == 'NFL':
        year_link = f"{year}_roster"

    for team in teams:
        url = f"{domain[sport]}/teams/{team}/{year_link}.htm"  # Replace with the target URL
        html = rate_limited_request(3, get_html_and_interact, url)
        file_path = f"Knowball/data/preprocessing/teams/{sport}/{team}/{year}.html"

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)
        except Exception as e:
            print(f"Page Failed for {team}'s Page: {e}")


def get_player_pages(sport, teams, year):
    if sport == 'NBA':
        pass
    elif sport == 'NFL':
        pass

    for team in teams:
        roster = pd.read_csv(f"Knowball/data/postprocessing/teams/{sport}/{team}/{year}_roster.csv")
        for _, player in roster.iterrows():
            player_link = player["Link"]
            player_name = player["Player"]
            url = f"{domain[sport]}{player_link}"  # Replace with the target URL
            html = rate_limited_request(3, get_html_and_interact, url)
            file_path = f"Knowball/data/preprocessing/players/{sport}/{team}/{player_name}.html"

            # Ensure the directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(html)
            except Exception as e:
                print(f"Page Failed for {team}'s Page: {e}")



get_player_pages('NFL', ['sfo'], 2024)
