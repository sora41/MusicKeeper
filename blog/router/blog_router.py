from typing import List
from fastapi import APIRouter, Depends, status as http_status ,Response, HTTPException
from blog.schemas.blog import Blog as Blog_schemas, ShowBlog
from blog.schemas.user_schemas import User
from blog.database import  get_db
from sqlalchemy.orm import Session
from blog.repository import blog_repository
from string import Template
from blog.oauth2 import get_current_user  

BLOG_ID_NOT_FOUND = "blog $id not found"

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

@router.post('',status_code = http_status.HTTP_201_CREATED)
def create_blog(request: Blog_schemas ,db:Session = Depends(get_db)):
    return blog_repository.create_blog(request=request,db=db)


@router.get('', response_model = List[ShowBlog] )
def get_all_blog(db:Session = Depends(get_db),current_user:User= Depends(get_current_user)):
    return blog_repository.get_all_blog(db)

@router.get('/test/dev')
def test():
    test = 'test $a and test'
    t= Template(test)
    res = t.substitute(a= 'LOL')
    return res

@router.get('/{id}',status_code = http_status.HTTP_200_OK, response_model = ShowBlog )
def show_on_blog(id: int,response: Response, db:Session = Depends(get_db)):
    blog = blog_repository.get_blog_by_id(id=id,db=db)
    if not blog:
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND, detail= Template(BLOG_ID_NOT_FOUND).substitute(id= id))
    return blog

@router.delete('/{id}',status_code = http_status.HTTP_204_NO_CONTENT)
def destroy_blog(id:int, db:Session = Depends(get_db)):
    blog = blog_repository.delete_blog_by_id(id=id,db=db)
    if not blog:
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND,detail= Template(BLOG_ID_NOT_FOUND).substitute(id= id))
    return  Response(status_code=http_status.HTTP_204_NO_CONTENT)

@router.put('/{id}',status_code = http_status.HTTP_202_ACCEPTED)
def update_blog(id:int,request:Blog_schemas, db:Session = Depends(get_db)):
    blog_to_update= blog_repository.update_blog_by_id(id=id,request=request,db = db)
    if not blog_to_update:
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND, detail= Template(BLOG_ID_NOT_FOUND).substitute(id= id))
    return  Response(status_code=http_status.HTTP_204_NO_CONTENT) 

