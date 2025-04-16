# Final Assessment

> Ben Cimini (ciminibb@mail.uc.edu), CS

I was in charge of our backend and UI, among other things. This paragraph will focus on the former. Work on the backend began with sourcing
data—our biggest challenge. Single APIs do exist that would’ve provided access to all the sports, social media, and web data we needed.
However, such solutions were far beyond our budget. Using a collection of free (or least-cost) APIs wasn’t preferable, either. That would’ve
introduced many potential points of failure into our project. Instead, I started a free trial of Stathead, which allowed me to query the
Sports Reference database with a GUI. In doing so, I was able to export all of our sports data as CSV files. Afterward, I built an automated
pipeline to copy the data to an Azure SQL database. Any modifications to the CSVs would trigger the pipeline to run again, thereby refreshing
our dataset. Through the above, I got quite comfortable working with Azure, as well as cleaning datasets.

The UI, on the other hand, began with design. Such creative aspects of software development are strengths of mine, so I was able to arrive at
an engaging yet user-friendly mockup. However, the implementation of it was a new experience for me. After some research, I decided on React
and Tailwind CSS as our front-end tech stack. I picked them up relatively quickly, but there were challenges. Mainly, my ad-hoc development
methods meant I had to overhaul the architecture a few times. At first, I built each on-screen element as a separate component with all
database interactions contained within them. As a consequence, the exchange of data between components was sloppy at best, impractical at worst.
To remedy the problem, I built screens as parents to the components. That way, all database interactions could be handled by the parents, who
could pass the results to their corresponding child components. I learned a great deal about front-end development from this project. Proper
architecture was an important lesson, obviously, but so was programming the middleware between backend and UI.

My group accomplished our key objectives! Of course, the scope of our project did shrink as we went along, but such diversions were made for the
greater good. From the start, our main priority was to produce a polished, finished game. It’s easy to have good ideas but hard to execute
them—which we did. Specifically, both major systems in our design were completed: the Obscurity Engine and Knowball, the game that uses it. By the
Expo, the Obscurity Engine was able to quantify athletes’ relative obscurity in compliance with the perception of all who tested our project;
nobody seemed to disagree with its outputs, which shows our machine-learning model was accurate. Knowball was very popular among people who played
it. We had several groups that stuck around our booth for 15 minutes or more, playing it over and over. The mark of any good game is being fun, and
it seems we delivered on that expectation.

***TEAM EVALUATION OMITTED***
