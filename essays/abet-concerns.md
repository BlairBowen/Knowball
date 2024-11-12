# ABET Concerns

***We have four main concerns that may constrain our development of Knowball.*** They are given below.

**First, we are concerned about data availability.** As discussed elsewhere, the objective of playing Knowball is to name increasingly
obscure athletes. So, we as developers must assemble enough data about athletes – their teams, statistics, achievements, search
analytics, social media following, and more – to respond given obscure names. That’s inherently difficult; there will be less data
about lesser-known athletes, even in the most comprehensive datasets. In addition, such datasets often have access limitations
(see economics). This could require us to pursue alternate methods of sourcing data.

**Second, we have a legality concern.** Web scraping is the likely solution to sourcing difficult data. However, doing so would require
caution to ensure Knowball is legally permissible. We must only scrape from sites whose terms of service don’t prohibit it, whose data
is publicly accessible, whose data isn’t protected against bots, and more. This, in itself, is a constraint that could influence the
ultimate quality of our solution.

**Third, we are concerned about the economics of implementing and maintaining Knowball.** As previously suggested, the most comprehensive
sports datasets will keep some, if not all of their data behind a paywall. In other words, quality data is likely to cost us. Quality
infrastructure is likely to cost us, too. Hosting Knowball on a cloud platform like Azure or AWS will incur charges, even on the most
basic plan. Balancing quality and cost-effectiveness is an engineering decision we’ll have to consider time and time again.

**Fourth, and finally, we are concerned about data alignment.** Let me explain what that means. Knowball will compute obscurity for athletes
in different sports, leagues, and countries. Does a Super Bowl have the same impact on one’s public image as a gold medal in Olympic
fencing? It certainly doesn’t, even though those examples are similar achievements: a championship versus a championship. So, we must
build a standardization process into Knowball, where statistics are weighted to reflect their origin. The danger here is those weights,
potentially, being arbitrary. We can likely agree that fencing medalists are more obscure than Super Bowl champions, but by how much? Can
we determine those differences algorithmically, perhaps by viewership data?
