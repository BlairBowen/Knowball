# Diagram Description

This is your guide to understanding the diagrams in this folder. It includes a key and some discussion of essential components.

## Key

- Dotted line = Frontend/Backend divider
- Arrow = Data flow
- Stick figure = Player
- Rectangle = Process
- Ellipse = Entity
- Rounded rectangle = Cluster of processes and entities
- Cylinder = Data

## Frontend (Game)

This layer defines how players will interact with the Knowball game.

#### Input

Players will enter athletes who fit a prompt in an interface similar to Wordle.

#### Output

The user will see...

- A prompt to which their inputs should respond.
- The score earned by their most recently entered athlete.
- Their total score for the prompt.

## Backend

This layer defines how the system processes user input, interacts with data sources, and generates scores. It spans several key
components that work together to validate user guesses, retrieve data, and compute obscurity.

#### Query Manager

The Query Manager is responsible for handling all queries. It interacts with data sources via APIs and/or web scraping, as well as our
Database to gather relevant data for the system. Such data includes...

- Athletes
- Cached obscurity engine outputs
- In-game leaderboards
- Athletes' on-field statistics
- Athletes' sporting achievements
- Athletes' social media analytics
- Search engine trends
- More

#### Obscurity Engine

The Obscurity Engine quantifies athletes' public presence deterministically. To do so, it considers the data given above. The algorithm
it will run is a work in progress and, later, will be tuned to align with our human interpretation of obscurity.

#### Standardize Data

This process standardizes data from our various sources. This is important because, when computing obscurity, different achievements hold
different weight. For example, a Super Bowl will likely do more for an athlete's public presence than an MLS Cup. So, this process ensures
contrasting data are transformed to a comparable scale.

#### Validate Inputs

This process checks that players' inputs are correct in response to the prompt they were given. It does so by comparison with our
Database.

#### Validate Trivia

This process checks that our trivia questions (prompts) are of appropriate difficulty for players. It does so by comparison with our
Database (for number of correct responses) and with the Obscurity Engine (for obscurity of correct responses).

#### Convert Output to Score

The Obscurity Engine will spit out a coefficient that, while meaningful, might not be easy for the average player to decipher. So,
such outputs will be run through a conversion process so that they may be returned to players as nice, whole numbers.

#### Data Sources

The system gathers data from the following external sources through API calls and web scraping.

- Google Trends for real-time search interest
- Sports references for athletic accolades and statistics
- Social media platforms for follower counts, mentions, engagement, etc

Each of these components contributes to generating a score for the player's inputs, which is displayed through the frontend.
