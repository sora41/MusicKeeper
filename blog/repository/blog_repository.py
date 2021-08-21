from blog.database import  get_db
from sqlalchemy.orm import Session, session
from blog.models.models import Blog as Blog_model
from blog.schemas.blog import Blog as Blog_schemas

def get_all_blog(db:Session ):
    return  db.query(Blog_model).all()


def create_blog(request:Blog_schemas, db:Session ):
    new_blog= Blog_model(title= request.title , body = request.body)
    new_blog.user_id = request.user_id
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog_by_id(id:int, db:session):
    blog = db.query(Blog_model).filter(Blog_model.id == id).first()    
    return blog

def delete_blog_by_id(id:int,db:session):
   blog_to_delete= db.query(Blog_model).filter(Blog_model.id == id)
   if not blog_to_delete.first():
      return None
   blog_to_delete.delete(synchronize_session=False)
   db.commit()
 
def update_blog_by_id(id:int,request:Blog_schemas,db:session):
    
    blog_to_update= db.query(Blog_model).filter(Blog_model.id == id).first()
    if not blog_to_update:
        return None
  
    blog_to_update.title = request.title
    blog_to_update.body= request.body

    db.add(blog_to_update)
    db.commit()
    
    return blog_to_update 