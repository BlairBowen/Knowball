# Task List

The date of writing is September 25, 2024. We are early in this project, so it doesn’t serve us to
forecast minutia. Rather than specific features, enhancements, and bug fixes, the following tasks
represent large areas of our design. They will be further subdivided into deliverables as we engage
with them, and have the knowledge to do so. Such deliverables will be tracked on our project board.

### Ben

1. Refine the desired system operations during gameplay (i.e., the I/O through system components).
2. Research database frameworks (MySQL, PostgreSQL, MongoDB, SQLite, etc.) to inform the most suitable choice.
3. Research platforms on which to host the database (Azure, AWS, etc.) to inform the most suitable choice.
4. Collect options for sport-statistics APIs and weigh them against the alternative of web scraping.
5. Design the "Athlete DB" with Entity Relationship Diagrams.
6. Create database tables with the chosen framework, on the chosen platform. Populate them with test data.

### Blair

1. Research front-end frameworks (Vue.js, React, Angular, etc.) to inform the most suitable choice.
2. Design the UI/UX with a sequence of mockups representing state transitions.
3. Develop the front end, per the mockups approved in the previous task, and vet it with test data.
4. Connect the front end to backend processes like the Query Manager, Guess Validator, Obscurity Engine, etc.
5. Collect parameters for the Obscurity Engine (i.e., relevant metrics the engine should compute over).
6. Decompose natural language questions into manageable logic for the Question Validator.
7. Research uses for ML in the Obscurity Engine to inform the most suitable choice for its potential inclusion.

### Stetson

1. Guide discussion of weights on Obscurity Engine parameters (e.g., social following versus on-field statistics).
2. Tune the Obscurity Engine based on its response to predetermined test cases.
3. Tune standardization factors for our metrics across different countries, sports, leagues, etc.
4. Tune the Score Converter to produce digestible outputs for players of our game.
5. Tune the threshold of the Question Validator so that only questions of reasonable difficulty are pushed to the database.
6. Research data-analysis libraries in Python to inform the most suitable choice for our Obscurity Engine.

> ## Note
> This project was designed on mutual interests. Each member of Knowball cares to be involved in all
> parts of the system, however minimally. So, think of the above delegations not as a contract of
> sole responsibility, but as a commitment to lead each high-level task.
