from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint

#create a Post class containing the features we want

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#inherit the PostBase class by using "pass" keyword
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
        
#create a response class
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    #de pydantic read data even its not a dict
    class Config:
        orm_mode = True

class PostOut(PostBase):
    post: Post
    votes: int

    class Config:
        orm_mode = True

        
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    post_id:int
    dir: conint(le=1) #le=1 means less than or equal 1