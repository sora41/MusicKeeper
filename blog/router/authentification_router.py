from blog.models.models import User
from fastapi import APIRouter,Depends,status as http_status,HTTPException
from blog.database import get_db
from sqlalchemy.orm import Session
from blog.schemas.login import Login
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from blog.repository import user_repository
from blog.hashing import Hash
from blog.router.jwt_token import create_access_token
from blog.schemas.user_schemas import  User as User_schemas
router =router = APIRouter(
    tags=['auth']
)


#def login(request:OAuth2PasswordRequestForm = Depends() , db:Session =Depends(get_db)):
@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends() , db:Session =Depends(get_db)):
    user:User_schemas = user_repository.get_user_by_email(email=request.username,db=db)
    if not user :
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND,detail=f"ivalide creds")
   
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code= http_status.HTTP_404_NOT_FOUND,detail=f"ivalide pwd")
   
    #JWT TOKEN  3h28

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
   

