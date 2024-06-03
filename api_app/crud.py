from sqlalchemy.orm import Session
from . import models, schemas


def get_blog(db:Session, id:int):
    return db.query(models.Blog).filter(models.Blog.blog_id == id).first()


def get_blogs(db:Session, skip:int=0, limit:int=10):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def create_blog(db:Session, blog:schemas.BlogCreate):
    db_blog = models.Blog(title=blog.title, body=blog.body, created_by=blog.created_by)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def update_blog(db:Session, id:int, blog:schemas.BlogCreate):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id==id).first()
    db_blog.title = blog.title
    db_blog.body = blog.body
    db_blog.created_by = blog.created_by
    db.commit()
    db.refresh(db_blog)
    return db_blog


def delete_blog(db:Session, id:int):
    db_blog = db.query(models.Blog).filter(models.Blog.blog_id == id).first()
    if not db_blog:
        return None
    db.delete(db_blog)
    db.commit()
    return db_blog