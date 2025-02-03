# Database Glossary

***This document defines all column names Knowball's database***, as some are rather vague in their abbreviation.

## epl_player

- **ID**: An integer number that uniquely identifies each player, assigned in alphabetical order.
- **Player**: Each player's name.
- **Until**: The most recent season that each player participated in.
- **MP**: Matches Played by the player or squad.
- **Min**: Minutes
- **Start**: Game or games started by player.
- **Sub**: Game or games player did not start, so as a substitute.
- **Gls**: Goals scored.
- **Ast**: Assists
- **NPG**: Non-Penalty Goals
- **PK**: Penalty Kicks made.
- **Sh**: Shots total.
- **SoT**: Shots on Target
- **SoT%**: Percentage of shots that are on target.
- **ShDist**: Average distance, in yards, from goal of all shots taken.
- **FK**: Shots from Free Kicks.
- **PaCmp**: Passes Completed including live ball passes (including crosses) as well as corner kicks, throw-ins, free kicks and goal kicks.
- **PaCmp%**: Pass Completion Percentage.
- **KP**: Key Passes, those that directly lead to a shot (assisted shots).
- **Crs**: Completed crosses into the 18-yard box.
- **PrgP**: Progressive Passes, which are completed passes that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch.
- **Car**: Carries, the number of times the player controlled the ball with their feet.
- **TotDist**: Total Distance, in yards, a player moved the ball while controlling it with their feet, in any direction.
- **PrgC**: Carries that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any carry into the penalty area. Excludes carries which end in the defending 50% of the pitch.
- **Mis**: Number of times a player failed when attempting to gain control of a ball.
- **Dis**: Number of times a player loses control of the ball after being tackled by an opposing player. Does not include attempted take-ons.
- **TOnAtt**: Number of attempts to Take On defenders while dribbling.
- **TOnSucc**: Number of defenders taken on successfully, by dribbling past them. Unsuccessful take-ons include attempts where the dribbler retained possession but was unable to get past the defender.
- **TOnSucc%**: Percentage of Take-Ons completed successfully.
- **Tkl**: Tackles, the number of players tackled.
- **TklW**: Tackles in which the tackler's team won possession of the ball.
- **Def_3rd**: Tackles in defensive 1/3 of the pitch.
- **Mid_3rd**: Tackles in middle 1/3 of the pitch.
- **Att_3rd**: Tackles in attacking 1/3 of the pitch.
- **Blck**: Number of times blocking a shot by standing in its path.
- **Int**: Interceptions
- **Clr**: Clearances
- **Err**: Errors leading to an opponent's shot.
- **DuelW**: Aerials Duels Won
- **DuelW%**: Percentage of Aerials Duels Won.
- **CrdY**: Yellow Cards
- **CrdR**: Red Cards
- **Fls**: Fouls committed.
- **Fld**: The number of times a player was Fouled.
- **Off**: Offsides against a player. 
- **OG**: Own Goals
- **Recov**: Number of loose balls recovered.
- **GA**: Goals Against
- **Sv**: Saves
- **Sv%**: Save Percentage
- **CS**: Clean Sheets, full matches by goalkeeper where no goals are allowed.
- **CS%**: Percentage of matches that result in clean sheets.
- **Pos**: The player's Position(s) on the pitch.
- **Team**: The Team(s) a player competed for.
- **BdOr**: Balon d'Ors won, the award for the best player in the world for a given year.
- **GBoot**: Premier League Golden Boots won, the top scorer award.
- **GGlove**: Premier League Golden Gloves won, the top goalkeeper award.
- **POTY**: Premier League Player of the Year awards won.
- **TOTY**: Premier League Team of the Year inclusions.
- **WC**: World Cups won.
- **Euro**: European Championships won.
- **UCL**: Champions League titles won.
- **Prem**: Premier League titles won.
- **IG**: Instagram followers.
- **Wiki**: Last month's Wikipedia page views.

## nba_player

- **ID**: An integer number that uniquely identifies each player, assigned in alphabetical order.
- **Player**: Each player's name.
- **Until**: The most recent season that each player participated in.
- **G**: Games
- **GS**: Games Started
- **All_Star**: All-Star team selections.
- **MP**: Minutes Played
- **FG**: Field Goals
- **FGA**: Field Goal Attempts
- **2P**: 2-Point Field Goals
- **2PA**: 2-Point Field Goal Attempts
- **3P**: 3-Point Field Goals
- **3PA**: 3-Point Field Goal Attempts
- **FT**: Free Throws
- **FTA**: Free Throw Attempts
- **ORB**: Offensive Rebounds
- **DRB**: Defensive Rebounds
- **TRB**: Total Rebounds
- **AST**: Assists
- **STL**: Steals
- **BLK**: Blocks
- **TOV**: Turnovers
- **PF**: Personal Fouls
- **PTS**: Points
- **FG%**: Field Goal Percentage
- **2P%**: 2-Point Field Goal Percentage
- **3P%**: 3-Point Field Goal Percentage
- **FT%**: Free Throw Percentage
- **TS%**: True Shooting Percentage, a measure of shooting efficiency that takes into account 2-point field goals, 3-point field goals, and free throws.
- **eFG%**: Effective Field Goal Percentage, this statistic adjusts for the fact that a 3-point field goal is worth one more point than a 2-point field goal.
- **Pos**: Position
- **Team**: The Team(s) a player competed for.
- **MVP**: NBA Most Valuable Player awards won.
- **ROY**: NBA Rookie of the Year awards won.
- **DPOY**: NBA Defensive Player of the Year awards won.
- **All_NBA**: All-NBA team inclusions across first, second, and third teams.
- **Champ**: NBA Championships won.
- **IG**: Instagram followers.
- **Wiki**: Last month's Wikipedia page views.

## nfl_player

- **ID**: An integer number that uniquely identifies each player, assigned in alphabetical order.
- **Player**: Each player's name.
- **Until**: The most recent season that each player participated in.
- **G**: Games played.
- **GS**: Games Started as an offensive or defensive player.
- **Cmp**: Passes completed.
- **PaAtt**: Passes Attempted
- **Cmp%**: Percentage of passes completed.
- **PaYds**: Yards gained by passing.
- **PaTD**: Passing Touchdowns
- **IntO**: Interceptions thrown (offensive player).
- **Rate**: Passer rating.
- **SkO**: Times sacked (first recorded in 1969, player per game since 1981).
- **QBWin**: Team wins in games started by this QB (regular season).
- **GWD**: Game-winning drives led by quarterback.

Rushing
Att -- Rushing Attempts (sacks not included in NFL)
Yds -- Rushing Yards Gained (sack yardage is not included by NFL)
Y/A -- Rushing Yards per Attempt
Minimum 6.25 rushes per game scheduled to qualify as leader.
Minimum 750 rushes to qualify as career leader.
TD -- Rushing Touchdowns
Y/G -- Rushing Yards per Game
(minimum half a game per game scheduled to qualify as leader)
(Rushing Yards)/(Games Played)
1D -- First downs rushing
Succ% -- Rushing Success Rate
A successful rush gains least 40% of yards required on 1st down, 60% of yards required on 2nd down, and 100% on 3rd or 4th down. Denominator is rushing attempts.
Receiving
Tgt -- Pass Targets (since 1992, derived from NFL play-by-play data)
Rec -- Receptions
Yds -- Receiving Yards
Y/R -- Receiving Yards per Reception
Minimum 1.875 catches per game scheduled to qualify as leader.
Minimum 200 receptions to qualify as career leader.
TD -- Receiving Touchdowns
Y/G -- Receiving Yards per Game
(minimum half a game played per game scheduled to qualify as leader, 32 games for career leaders)
(Receiving Yards)/(Games Played)
Ctch% -- Catch%, receptions divided by targets (since 1992)
Y/Tgt -- Receiving Yards per Target (target numbers since 1992)
1D -- First downs receiving
Succ% -- Receiving Success Rate
A successful reception gains at least 40% of yards required on 1st down, 60% of yards required on 2nd down, and 100% on 3rd or 4th down. Denominator is targets.
TD -- Touchdowns of every type
PAT
XPM -- Extra Points Made
XPA -- Extra Points Attempted
Kicking
XP% -- Extra Point Percentage
(Extra Points Made)/(Extra Points Attempted)
Minimum 1.5 attempts per game scheduled to be a leader.
FG
FGM -- Field Goals Made
FGA -- Field Goals Attempted
Kicking
FG% -- Percentage of field goals made, 100*(FGM/FGA)
Minimum 0.75 attempts per game scheduled to qualify as a leader.
Minimum 100 FGA to qualify as career leader.
Other Scoring
2PM -- Two-Point Conversions Made
Sfty -- Safeties scored by player/team
Scoring
Pts -- Total points scored by all means
Fantasy
FantPt -- Fantasy points:
1 point per 25 yards passing
4 points per passing touchdown
-2 points per interception thrown
1 point per 10 yards rushing/receiving
6 points per TD
2 points per two-point conversion
-2 points per fumble lost (est. prior to 1994)
PPR -- Fantasy points (PPR scoring):
1 point per 25 yards passing
4 points per passing touchdown
-2 points per interception thrown
1 point per reception
1 point per 10 yards rushing/receiving
6 points per TD
2 points per two-point conversion
-2 points per fumble lost (est. prior to 1994)
Fantasy per Game
FantPt -- Fantasy points per game played
PPR/G -- PPR Fantasy points per game played, see glossary for scoring details
Sacks
Sk -- Sacks (official since 1982,
based on play-by-play, game film
and other research since 1960)
Tackles
Solo -- Tackles
Before 1994: unofficial and inconsistently recorded from team to team. For amusement only.
1994-now: unofficial but consistently recorded.
Ast -- Assists on tackles
Before 1994: combined with solo tackles
1994-now: unofficial, but consistently recorded
Comb -- Tackles
Combined solo + assisted tackles
Prior to 1994, all tackles are put into 'combined', though
they are unofficial and inconsistently recorded from team to team. For amusement only.
TFL -- Tackles For Loss, recorded for 95% of games from 1999-2007 and 100% since 2008
QBHits -- Quarterback hits, recorded since 2006
Def Interceptions
Int -- Passes intercepted on defense
Yds -- Yards interceptions were returned
IntTD -- Interceptions returned for touchdowns
PD -- Passes defended by a defensive player, since 1999
Fumbles
Fmb -- Number of times fumbled both lost and recovered by own team
These represent ALL fumbles by the player on offense, defense, and special teams.
Available for player games since 1989.
FR -- Fumbles recovered by a Player or Team
Original fumble by either team
Yds -- Yards recovered fumbles were returned
FRTD -- Fumbles recovered resulting in a touchdown for the recoverer
FF -- Number of times forced a fumble by the opposition recovered by either team
Touch -- Touches: Rushing Attempts and Receptions
TotOff -- Total Offense
Rush Yards + Passing Yards - Yards Lost to Sacks
YScm -- Yards from Scrimmage: Receiving and Rushing Yards
APYd -- All-purpose yards: Rushing, Receiving and Kick, Punt, Interception, and Fumble Return Yardage
Returns
RtY -- Combined Kick and Punt Return Yardage
Pos -- Position
