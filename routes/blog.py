from typing import Optional
from fastapi import APIRouter

from models.blog import Blog
from config.db import conn
from schemas.blog import blogEntity, blogsEntity, blogsEntityResume
from bson.objectid import ObjectId

blog = APIRouter()

@blog.get('/blog')
async def find_all_blogs(search: Optional[str]= ''):
    if search != '':
        return blogsEntityResume(conn.local.blog.find({"$or":[{"content":{"$regex" :search }},{"title":{"$regex" :search }},{"author":{"$regex" :search }}]}))
    else:
        return blogsEntityResume(conn.local.blog.find())

@blog.get('/blog/{id}')
async def find_blog(id):
    return blogEntity(conn.local.blog.find_one({"_id":ObjectId(id)}));

@blog.post('/blog')
async def create_blog(blog: Blog):
    conn.local.blog.insert_one(dict(blog))
    return blogsEntity(conn.local.blog.find())


@blog.put('/blog/{id}')
async def update_blog(id, blog:Blog):
    conn.local.blog.find_one_and_update({"_id":ObjectId(id)},{
        "$set": dict(blog)
    })
    return blogEntity(conn.local.blog.find_one({"_id":ObjectId(id)}))

@blog.delete('/blog/{id}')
async def delete_blog(id):
    return blogEntity(conn.local.blog.find_one_and_delete({"_id":ObjectId(id)}))