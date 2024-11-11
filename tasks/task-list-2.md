# Task List

The list below represents ***all of our currently forecasted deliverables***, with who is responsible for leading them.

> The date of revising this list is November 11th, 2024. At this point, the inevitable minutia of implementing our design
> still can't be forecasted perfectly. Each of the tasks below has the potential to be subdivided into further tasks. As
> we work through the list and gain insight, any subdivisions will be captured on our project board. Also, the delegation
> expressed below is not a contract of sole responsibility, but a commitment to lead the given high-level deliverables.

#### Ben

- Research database frameworks (MySQL, PostgreSQL, MongoDB, SQLite, etc.) to inform the most suitable choice.
- Research platforms on which to host the database (Azure, AWS, etc.) to inform the most suitable choice.
- Collect options for sport-statistics APIs and weigh them against the alternative of web scraping.
- Design the database with Entity Relationship Diagrams.
- Create database tables with the chosen framework, on the chosen platform. Populate them with test data.
- Develop a function by which Obscurity Engine outputs are cached for some finite amount of time.
- Develop a function by which high scores are saved to ephemeral, daily leaderboards.
- Refine the desired system operations during gameplay (i.e., the I/O through system components).
- Develop a function by which player inputs are validated for correctness before being passed to the Obscurity Engine.
- Work on our final presentation and project board.

#### Blair

- Research front-end frameworks (Vue.js, React, Angular, etc.) to inform the most suitable choice.
- Research uses for ML in the Obscurity Engine to inform the most suitable choice for its potential inclusion.
- Collect parameters for the Obscurity Engine (i.e., relevant metrics the engine should compute over).
- Begin to set up some web scrapers, should that option be pursued, to lay a foundation for our methods and needs.
- Begin processing some basic, essential data to lay a foundation for our methods and needs.
- Design the UI/UX with a sequence of mockups representing state transitions.
- Develop the front end, per the mockups approved in the previous task, and vet it with test data.
- Develop a function by which external data is fetched from APIs on non-cached user input.
- Create the Obscurity Engine by implementing its basic, untuned algorithm and functions.
- Decompose natural language questions into manageable logic for the Question Validator.
- Develop a function by which trivia questions are validated for appropriate difficulty before being committed.

#### Stetson

- Research data-analysis libraries in Python to inform the most suitable choice for our Obscurity Engine.
- Hold a discussion of weights on Obscurity Engine parameters (e.g., social following versus on-field statistics).
- Connect the front end to backend processes like the Query Manager, Guess Validator, Obscurity Engine, etc.
- Author our set of trivia questions and insert them into the database via the Question Validator.
- Develop the process by which data is standardized. This, of course, requires a choice of standardization factors.
- Tune the Obscurity Engine based on its response to predetermined test cases.
- Tune standardization factors for our metrics across different countries, sports, leagues, etc.
- Tune the Score Converter to produce digestible outputs for players of our game.
- Tune the threshold of the Question Validator so that only questions of reasonable difficulty are pushed to the database.
