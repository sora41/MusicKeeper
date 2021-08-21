from blog.database import  get_db
from sqlalchemy.orm import Session, session
from blog.models.models import User as User_model
from blog.schemas.user_schemas import User as User_schemas
from blog.hashing import Hash

def get_all_users(db:Session ):
    return  db.query(User_model).all()


def create_user(request:User_schemas, db:Session ):
    new_user= User_model(name= request.name , email= request.email ,password = Hash.bcryp(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

def get_user_by_id(id:int, db:session):
    user = db.query(User_model).filter(User_model.id == id).first()        
    return user

def get_user_by_email(email:str, db:session):
    user = db.query(User_model).filter(User_model.email == email).first()        
    return user

def update_user_by_id(id:int,request:User_schemas,db:session):
    user_to_update= db.query(User_model).filter(User_model.id == id).first()  
    if not user_to_update:
         return None

    user_to_update.name = request.name
    user_to_update.password= Hash.bcryp(request.password)
    user_to_update.email = request.email

    db.add(user_to_update)
    db.commit()

    return user_to_update

#def delete_user_by_id(id:int,db:session):