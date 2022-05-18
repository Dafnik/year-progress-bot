# year progress bot
[Deployed live version](https://voi.social/@year_progress)

## Setup
Create a `token.secret` file where you save your mastodon api key

## Run
Add a cron job which executes `bot.py`
```bash
@daily cd /path/to/year_progress/ && python3 bot.py
```
