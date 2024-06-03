from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Relationship
from datetime import datetime
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"
    blog_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now)
    created_by = Column(String, index=True)
