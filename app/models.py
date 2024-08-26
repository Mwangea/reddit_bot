from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Subreddit(Base):
    __tablename__ = 'subreddits'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    posts = relationship("Post", back_populates="subreddit")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(300), nullable=False)
    content = Column(String(40000), nullable=False)
    is_self = Column(Boolean, default=True)
    scheduled_time = Column(DateTime, nullable=False)
    posted = Column(Boolean, default=False)
    reddit_post_id = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)
    subreddit_id = Column(Integer, ForeignKey('subreddits.id'), nullable=False)
    subreddit = relationship("Subreddit", back_populates="posts")

class Proxy(Base):
    __tablename__ = 'proxies'
    id = Column(Integer, primary_key=True)
    address = Column(String(100), unique=True, nullable=False)
    port = Column(Integer, nullable=False)
    protocol = Column(String(10), nullable=False)
    last_used = Column(DateTime)
    is_active = Column(Boolean, default=True)