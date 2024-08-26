import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
from sqlalchemy import create_engine
from app.models import Base, Subreddit, Post, Proxy
from config import DATABASE_URL
from datetime import datetime, timedelta

def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")

    session = engine.connect()

    subreddits = [
        "AskReddit", "funny", "todayilearned", "pics", "gaming", "aww", "science", "worldnews",
        "movies", "music", "food", "books", "art", "photography", "DIY", "sports"
    ]
    session.execute(Subreddit.__table__.insert().values([{"name": name} for name in subreddits]))

    titles = [
        "What's your favorite book?",
        "TIL about the world's smallest mammal",
        "My dog's reaction when I come home",
        "Incredible sunset I captured last night",
        "New study reveals surprising facts about sleep",
        "What's the best advice you've ever received?",
        "Check out this DIY project I just finished",
        "Breaking: Major scientific discovery announced",
        "Movie recommendation thread: What should I watch tonight?",
        "I tried a new recipe and it turned out amazing!",
    ]

    contents = [
        "Share your favorite book and why you love it!",
        "https://en.wikipedia.org/wiki/Etruscan_shrew",
        "https://i.imgur.com/rGmVB7F.jpg",
        "https://i.imgur.com/KZbNwMJ.jpg",
        "A new study published in Nature reveals that...",
        "Let's share the best pieces of advice we've received. I'll start...",
        "https://i.imgur.com/DIY_Project.jpg",
        "Scientists at CERN have announced a breakthrough in...",
        "I'm looking for a good movie to watch tonight. Any suggestions?",
        "https://i.imgur.com/delicious_meal.jpg",
    ]

    now = datetime.utcnow()
    sample_posts = []
    for i in range(30):
        title = random.choice(titles)
        content = random.choice(contents)
        is_self = not content.startswith("http")
        subreddit_id = random.randint(1, len(subreddits))
        scheduled_time = now + timedelta(hours=random.randint(1, 72))
        
        sample_posts.append({
            "title": title,
            "content": content,
            "is_self": is_self,
            "scheduled_time": scheduled_time,
            "subreddit_id": subreddit_id
        })

    session.execute(Post.__table__.insert().values(sample_posts))

    proxies = [
        {"address": "proxy1.example.com", "port": 8080, "protocol": "http"},
        {"address": "proxy2.example.com", "port": 8080, "protocol": "https"},
        {"address": "proxy3.example.com", "port": 3128, "protocol": "http"},
        {"address": "proxy4.example.com", "port": 3128, "protocol": "https"},
        {"address": "proxy5.example.com", "port": 80, "protocol": "http"},
    ]
    session.execute(Proxy.__table__.insert().values(proxies))

    session.close()
    print("Sample data added successfully.")

if __name__ == "__main__":
    create_database()