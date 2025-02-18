# Knowball User Guide

## Introduction
**Knowball** is a sports trivia game where players must name an athlete that fits a given prompt while aiming for the most obscure choice possible. The game challenges your deep knowledge of sports rosters and statistics.

## How to Play
1. The game presents you with a prompt (e.g., **"NBA player with more than 3 PPG in a season"**).
2. You must enter the name of a **current** player who meets the criteria.
3. Your score is based on the **obscurity** of your choice—less popular picks earn more points.
4. The game provides feedback on your selection, including:
   - Whether the player is **valid** (fits the criteria).
   - The **obscurity score** (based on player recognition and usage rate).
5. Play multiple rounds and compete for the lowest total score!

## Scoring System
- **Obscurity Score**: The rarer the pick, the better your score.
- **Invalid Answers**: If a player doesn’t fit the prompt, you receive a penalty.
- **Leaderboard**: Compete against others for the most obscure selections!

## Installation & Setup
### Prerequisites
- Python 3.x
- Required dependencies (install via `pip install -r requirements.txt`)

### Running the Game
```sh
python knowball.py
```
Follow the on-screen instructions to start playing!

## Rules & Restrictions
- Only current athletes are allowed.
- Players must match the prompt’s statistical criteria.
- No duplicate answers within the same session.

## FAQ
### What happens if I enter an invalid player?
You'll receive an error message and a chance to try again.

### How is obscurity determined?
The system calculates obscurity based on player usage, media mentions, and recent performance.

For more details, visit the [User Manual](USER_MANUAL.md). (Coming Soon)
