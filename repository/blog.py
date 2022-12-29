from fastapi import (HTTPException,
                     status, Response,)
from sqlalchemy.orm import Session
from models import (Blog,)


class BlogRequest():
    def get_all(db: Session):
        blogs = db.query(Blog).all()
        return blogs

    def create(db: Session, request):
        data = Blog(title=request.title,
                    body=request.body,
                    user_id=1)
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

    def destroy(db: Session, id):
        selected_blog = db.query(Blog).filter(Blog.id == id)
        if not selected_blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        selected_blog.delete(synchronize_session=False)
        db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    def update(db: Session, id: int, request):
        data = db.query(Blog).filter(Blog.id == id)
        if not data.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        data.update(request.dict())
        db.commit()
        return Response(status_code=status.HTTP_200_OK)

    def show(db: Session, id):
        data = db.query(Blog).filter(Blog.id == id).first()
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with the {id} is not available")
        return data
