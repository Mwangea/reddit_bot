import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Subreddit, Post, Proxy
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def add_subreddit(name):
    session = Session()
    try:
        subreddit = Subreddit(name=name)
        session.add(subreddit)
        session.commit()
        print(f"Subreddit '{name}' added successfully.")
    except Exception as e:
        print(f"Error adding subreddit: {e}")
        session.rollback()
    finally:
        session.close()

def add_post(title, content, subreddit_name, scheduled_time, is_self=True):
    session = Session()
    try:
        subreddit = session.query(Subreddit).filter_by(name=subreddit_name).first()
        if not subreddit:
            subreddit = Subreddit(name=subreddit_name)
            session.add(subreddit)
        
        post = Post(
            title=title,
            content=content,
            is_self=is_self,
            scheduled_time=scheduled_time,
            subreddit=subreddit
        )
        session.add(post)
        session.commit()
        print(f"Post '{title}' scheduled for r/{subreddit_name} at {scheduled_time}.")
    except Exception as e:
        print(f"Error adding post: {e}")
        session.rollback()
    finally:
        session.close()

def add_proxy(address, port, protocol):
    session = Session()
    try:
        proxy = Proxy(address=address, port=port, protocol=protocol)
        session.add(proxy)
        session.commit()
        print(f"Proxy '{address}:{port}' added successfully.")
    except Exception as e:
        print(f"Error adding proxy: {e}")
        session.rollback()
    finally:
        session.close()