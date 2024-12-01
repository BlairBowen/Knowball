# Data Sources

This document collects ***options we could leverage to pull sports data into Knowball***.

## Paid Services

#### [Sportradar](https://sportradar.com/media-tech/data-content/sports-data-api/)

Sportradar seems to have everything we might need and, as a bonus, they partner with major
sporting franchises - so we can be confident that their data is good. I even saw mention
that they have player data down to XY coordinates. However, it seems like this could be an
expensive option. Their prices aren't listed anywhere apparent, but it seems like they
could top out around $500 for a year.

#### [Stats Perform](https://developer.stats.com/)

While Stats Perform seems to have everything we would need, it's likely more than we need.
Getting any concrete information seems to involve contacting them, suggesting that we'd be
clients rather than just users. My judgement is that our project isn't of sufficient
scale for a solution this involved.

#### [SportsDataIO](https://sportsdata.io/scores-and-stats)

SportsDataIO is another robust option. However, this one offers a free trial that, unless
I'm reading incorrectly, has no usage limit. It is, instead, restricted in other ways.
For example, the data is scrambled. This option is more intriguing than the two above, but
I still feel like something more straightforward is best for our needs.

#### [Sports Reference API](https://pypi.org/project/sportsreference/)

Sports Reference API is free, well-documented, and easy to use with Python. However, its
data is mostly about teams, meaning getting historical player data could be complicated.
The data we need is displayed on the Sports Reference website, though
([example](https://www.pro-football-reference.com/players/L/LewiRa00.htm)). Player
achievements are specifically well-recorded there, meaning we could scrape them.

#### [Stathead](https://stathead.com/?__hstc=213859787.012bb7eef9abbe6357f8e0203f8c4a6a.1733094779937.1733094779937.1733094779937.1&__hssc=213859787.18.1733094779938&__hsfp=3011104808&_gl=1*1klwwwq*_ga*NzM4NjcyNTc5LjE3MzMwOTQ3ODA.*_ga_80FRT7VJ60*MTczMzA5NDc3OS4xLjEuMTczMzA5NTM5OC4wLjAuMA..)

Stathead is the Sports Reference database, from what I understand. It has plans starting
at just $9 per month, which is a great price point for our budget. New users begin with
a 1 month free trial. Stathead provide access to ANY AND ALL information on the Sports
Reference websites. However, it's unclear if it does so through an API. Rather, it seems
like the data is given from GUI-based searches and filtering. However, knowing what we
need, we could export a bunch of searches to CSVs and move them into our database with a
pipeline. This solution wouldn't be scalable, but would work.
