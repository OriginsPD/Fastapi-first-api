'''
    Fast Api Framework lesson
    Innovation REST Api Version 0.0.2
    # import uvicorn
    '''
from typing import Optional
from fastapi import (FastAPI, Depends, HTTPException,
                     status, Response,)
from sqlalchemy.orm import Session
from schemas import Blog as schema
from database import engine, SessionLocal
from models import Base, Blog

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create(request: schema, db: Session = Depends(get_db)):
    new_blog = Blog(title=request.title,
                    body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session = Depends(get_db)):
    db.query(Blog).filter(Blog.id == id).delete(
        synchronize_session=False)
    db.commit()
    return {"done"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schema, db: Session = Depends(get_db)):
    selected_blog = db.query(Blog).filter(Blog.id == id)
    if not selected_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")
    selected_blog.update(request.dict())
    db.commit()
    return {"blog updated successful"}


@app.get('/blog')
async def all(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200)
async def show(id, response: Response, db: Session = Depends(get_db)):
    selected_blog = db.query(Blog).filter(Blog.id == id).first()
    if not selected_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the {id} is not available")
    return selected_blog
