
from fastapi import FastAPI 
from blog.models import models
from blog.database import  engine
from blog.router import blog_router as blog,user_router as user
from blog.router import authentification_router as auth
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)
