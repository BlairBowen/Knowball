# Diagram Description

This is your guide to understanding the diagrams in this folder. It includes a key and some discussion of essential components.

## Key

- Stick figure: The player
- Vertical, rounded rectangle - This represents a process layer
- Horizontal, sharp rectange - A single step of the process
- Solid arrow - Indicates flow of data
- Cylinder - Database

## Frontend Layer
This layer defines how the user will interact with the Knowball game.
### Input
The user will be presented with a Vue UI with input fields to allow them to input their answer to the prompt.
### Output
The user will be presented with the following:
* The score they just received
* Total Score
* A Prompt to guide obscure athlete guesses

## Backend Processes Layer

This layer describes how the system processes user input, interacts with external data sources, and calculates scores. It encompasses several key components that work together to validate user guesses, retrieve athlete data, and calculate an obscurity score.

### Query Manager
The Query Manager is responsible for managing the flow of queries. It interacts with external APIs, web scrapers, and the Athlete Database to gather relevant data for the system. This data includes:
* Athletes
* Athlete performance statistics
* Accolades
* Social media activity
* Trends in public awareness

### Data Standardization
This component standardizes the data received from various sources, ensuring that data from different sports and leagues hold the same value before entering the Obscurity Engine

### Question Validator
The Question Validator checks the validity of a Prompt the user sees. It does this by making sure a standard obscurity distribution and valid athlete count for a question is met

### Obscurity Engine
The Obscurity Engine works with the WIP (Work in Progress) Algorithm to calculate an obscurity score. This score is derived by analyzing how "well-known" an athlete is based on several factors, including:
* Social media mentions
* Google Trends data
* Athletic accolades
* Social media followers

### Score Converter
Once the obscurity score is calculated, the Score Converter translates the obscurity score into a user-friendly score. This score reflects how well the user guessed in relation to the obscurity of the athlete in question.

### External Data Sources
The system gathers data from the following external sources through API calls and web scraping:
* Google Trends for real-time search interest
* Sports references for athletic accolades and statistics
* Social media platforms for follower counts and mentions

Each of these components contributes to generating a final score for the user's guess, which is then displayed through the frontend.
