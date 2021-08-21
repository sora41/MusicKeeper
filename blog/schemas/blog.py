from typing import Optional
from pydantic import BaseModel
from blog.schemas.user_schemas import ShowUser 

class Blog(BaseModel):
    title:str
    body:str
    creator: Optional[ShowUser]
    user_id: Optional[int]

class ShowBlog(Blog):
    class Config():
        orm_mode=True



