import praw
import schedule
import time
import logging
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Post, Subreddit
from app.proxy_manager import get_next_proxy, update_proxy_usage, get_proxy_dict
from config import (
    DATABASE_URL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
    REDDIT_USER_AGENT, REDDIT_USERNAME, REDDIT_PASSWORD
)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD
)

def get_pending_post():
    session = Session()
    try:
        now = datetime.utcnow()
        post = session.query(Post).filter(Post.posted == False, Post.scheduled_time <= now).order_by(Post.scheduled_time).first()
        return post
    except Exception as e:
        logging.error(f"Error retrieving pending post: {e}")
    finally:
        session.close()
    return None

def make_post(post):
    session = Session()
    try:
        proxy = get_next_proxy(session)
        if not proxy:
            logging.error("No active proxies available")
            return False

        proxy_dict = get_proxy_dict(proxy)
        subreddit = reddit.subreddit(post.subreddit.name)
        
        if post.is_self:
            submission = subreddit.submit(post.title, selftext=post.content, proxies=proxy_dict)
        else:
            submission = subreddit.submit(post.title, url=post.content, proxies=proxy_dict)
        
        logging.info(f"Posted successfully: {post.title} in r/{post.subreddit.name} using proxy {proxy.address}")
        
        post.posted = True
        post.reddit_post_id = submission.id
        session.commit()
        
        update_proxy_usage(session, proxy)
        return True
    except Exception as e:
        logging.error(f"Error posting: {e}")
        return False
    finally:
        session.close()

def scheduled_task():
    post = get_pending_post()
    if post:
        success = make_post(post)
        if not success:
            logging.warning(f"Failed to post: {post.title}")
    else:
        logging.info("No posts scheduled at this time.")

def run_bot():
    schedule.every(1).minutes.do(scheduled_task)
    while True:
        try:
            schedule.run_pending()
            time.sleep(10)
        except Exception as e:
            logging.error(f"Unexpected error in main loop: {e}")
            time.sleep(60)

if __name__ == "__main__":
    logging.info("Reddit Bot started")
    run_bot()