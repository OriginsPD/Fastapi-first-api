from pydantic import BaseModel
from typing import List, Optional


class BlogBase(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode: bool = True


class BlogSchema(BlogBase):
    class Config():
        orm_mode: bool = True


class UserSchema(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogSchema]

    class Config():
        orm_mode: bool = True


class ShowBlog(BlogSchema):
    creator: ShowUser

    class Config():
        orm_mode: bool = True
