from pydantic import BaseModel
from datetime import datetime


class BlogBase(BaseModel):
    title: str
    body: str


class BlogCreate(BlogBase):
    created_by: str


class Blog(BlogBase):
    blog_id: int
    date: datetime
    created_by: str
    
    class Config:
        orm_mode = True