```mermaid

---
title: Knowball's simple database
---
erDiagram
  NBA-PLAYERS {
    int ID
    string Player
    types StatsAndInfo
  }
  NFL-PLAYERS {
    int ID
    string Player
    types StatsAndInfo
  }
  EPL-PLAYERS {
    int ID
    string Player
    types StatsAndInfo
  }
  LEADERBOARD {
    int ID
    string Name
    int Score
    string League
  }

```
