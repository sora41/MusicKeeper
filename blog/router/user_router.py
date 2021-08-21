from typing import List
from fastapi import APIRouter, Depends, status as http_status ,Response, HTTPException
from blog.schemas.user_schemas import User as User_schemas,ShowUser
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.repository import user_repository


USER_ID_NOT_FOUND = "user $id not found"

router = APIRouter(
    prefix="/user",
    tags=['users']
)

@router.get('/', response_model = List[ShowUser] )
def get_all_user(db:Session =Depends(get_db)):
    return user_repository.get_all_users(db=db)

@router.post('',status_code = http_status.HTTP_201_CREATED,response_model=ShowUser)
def create_user(request: User_schemas ,db:Session = Depends(get_db)): 
    return user_repository.create_user(db=db,request=request)

@router.get('/{id}',status_code = http_status.HTTP_200_OK, response_model = ShowUser )
def show_on_user(id,response: Response, db:Session = Depends(get_db)):
    user = user_repository.get_user_by_id(id=id,db=db)
    if not user:
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND, detail=f"Item {id} not found")
       
    return user

@router.put('/{id}',status_code = http_status.HTTP_202_ACCEPTED)
def update_user(id,request:User_schemas, db:Session = Depends(get_db)):
    user_to_update= user_repository.update_user_by_id(id=id ,request=request,db=db)
    if not user_to_update:
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND, detail=f"Item {id} not found")
  
    
    return  Response(status_code=http_status.HTTP_204_NO_CONTENT) 


