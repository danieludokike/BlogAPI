from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from sqlalchemy.exc import UnmappedInstanceError
from .database import SessionLocal, db_engine, Base
from . import models, schemas, crud


Base.metadata.create_all(bind=db_engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

# End point for creating a blog
@app.post("/api/blogs/", response_model=schemas.Blog)
def create_blog(blog:schemas.BlogCreate, db:Session=Depends(get_db)):
    return crud.create_blog(db=db, blog=blog)


# End pint for getting a single blog
@app.get("/api/blogs/{id}", response_model=schemas.Blog)
def read_blog(id:int, db:Session=Depends(get_db)):
    db_blog = crud.get_blog(db, id=id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog


# End point for getting multiple blogs
@app.get("/api/blogs/", response_model=list[schemas.Blog])
def read_blogs(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs


# End pint for blog update
@app.put("/api/blogs/{id}", response_model=schemas.Blog)
def update_blog(id:int, blog:schemas.BlogCreate, db:Session=Depends(get_db)):
    return crud.update_blog(db, id, blog)


# End point for blog deletion
@app.delete("/api/blogs/{id}", response_model=schemas.Blog)
def delete_blog(id:int, db:Session=Depends(get_db)):
    try:
        deleted_blog = crud.delete_blog(db, id)
        if not deleted_blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        return delete_blog(db, id)
    # except UnmappedInstanceError:
    except:
        raise HTTPException(status_code=404, detail="Blog has already been deleted")
        
        