# Reddit Bot

This is a Reddit bot that schedules and posts content to various subreddits using proxy rotation.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with the necessary credentials
4. Create the database: `python scripts/create_database.py`
5. Run the bot: `python -m app.bot`

## Usage

- To add new posts, subreddits, or proxies, use: `python scripts/manage_posts.py`
- To modify the sample data, edit the `scripts/create_database.py` file

## Deployment

This bot is set up to be deployed on Heroku. Follow these steps:

1. Create a new Heroku
