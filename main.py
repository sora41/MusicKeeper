from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body:str
    publish: Optional[bool]


@app.get('/blog')
def index():
    return {'data':'blog list'}

@app.get('/blog/unpublished')
def unpublished_blog():
    return {'unpublished'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def show_coments(id):
    return {'data': {'id':id ,'comments': { 1,2}}}

@app.get('/about')
def about():
    return {'data': 'about'}

@app.post('/blog')
def post_blog(request: Blog):
    return  request
