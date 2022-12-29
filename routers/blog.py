from typing import List
from fastapi import (APIRouter, Depends, status,)
from sqlalchemy.orm import Session
from schemas import (BlogSchema, ShowBlog,)
from database import get_db
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


@router.get('/', response_model=List[ShowBlog])
async def all(db: Session = Depends(get_db)):
    return blog.BlogRequest.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,
             response_model=List[ShowBlog])
async def create(request: BlogSchema, db: Session = Depends(get_db)):
    return blog.BlogRequest.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,
               )
async def destroy(id: int, db: Session = Depends(get_db)):
    return blog.BlogRequest.destroy(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id: int, request: BlogSchema, db: Session = Depends(get_db)):
    return blog.BlogRequest.update(db, id, request)


@router.get('/{id}', status_code=200, response_model=ShowBlog,
            )
async def show(id: int,  db: Session = Depends(get_db)):
    return blog.BlogRequest.show(db, id)
