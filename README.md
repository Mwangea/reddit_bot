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

   3. Update your `.env` file with this URL

### Continuous Deployment
To set up continuous deployment:

1. Connect your GitHub repository to the Heroku app:
- Go to the Heroku Dashboard > Your App > Deploy
- Choose GitHub as the deployment method
- Connect to your GitHub repository
2. Enable automatic deploys from your main branch
3. Optionally, set up review apps for pull requests

### Monitoring and Maintenance
- Use `heroku logs --tail` to monitor your app in real-time
- Set up Heroku Scheduler for periodic tasks if needed
- Regularly check your app's resource usage in the Heroku Dashboard

## Features

- Proxy rotation to avoid IP bans
- Scheduled posting to multiple subreddits
- Database storage for posts, subreddits, and proxies
- Easy management of content through command-line scripts

## Configuration

The bot's behavior can be configured through the `.env` file. Available options include:

- `POSTING_INTERVAL`: Time between posts (in minutes)
- `MAX_POSTS_PER_DAY`: Limit on daily posts
- `SUBREDDIT_COOLDOWN`: Time to wait before posting to the same subreddit (in hours)

## Logging

Logs are stored in the `logs` directory. The log level can be adjusted in the `config.py` file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes and commit them
4. Push to your fork and submit a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This bot is for educational purposes only. Make sure to comply with Reddit's terms of service and API usage guidelines when using this bot.
