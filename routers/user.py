from fastapi import (APIRouter, Depends, HTTPException,
                     status,)
from sqlalchemy.orm import Session
from hashing import Bcrypt
from schemas import (UserSchema, ShowUser,)
from database import get_db
from models import (User,)


router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post('/', response_model=ShowUser)
async def create_user(request: UserSchema, db: Session = Depends(get_db)):
    hashedPassword = Bcrypt.hash(request.password)
    new_user = User(name=request.name, email=request.email,
                    password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}', response_model=ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the {id} is not available")
    return user
