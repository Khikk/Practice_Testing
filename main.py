from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker
import logging
import sys

app = FastAPI()

# Модели данных
class Post(BaseModel):
    id: int
    title: str
    author: str

class Comment(BaseModel):
    id: int
    body: str
    post_id: int

class Profile(BaseModel):
    name: str


db = {
    "posts": [
        {"id": 1, "title": "json-server", "author": "typicode"}
    ],
    "comments": [
        {"id": 1, "body": "some comment", "post_id": 1}
    ],
    "profile": {"name": "typicode"}
}

# Логгирование
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# CRUD-запросы для сущности Post
@app.get("/posts")
async def get_posts():
    logging.info("GET /posts")
    return db["posts"]

@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    logging.info(f"GET /posts/{post_id}")
    for post in db["posts"]:
        if post["id"] == post_id:
            return post
    return {"error": "Post not found"}

@app.post("/posts")
async def create_post(post: Post):
    logging.info(f"POST /posts {post}")
    db["posts"].append(post.dict())
    return {"message": "Post created successfully"}

@app.put("/posts/{post_id}")
async def update_post(post_id: int, post: Post):
    logging.info(f"PUT /posts/{post_id} {post}")
    for i, p in enumerate(db["posts"]):
        if p["id"] == post_id:
            db["posts"][i] = post.dict()
            return {"message": "Post updated successfully"}
    return {"error": "Post not found"}

@app.delete("/posts/{post_id}")
async def delete_post(post_id: int):
    logging.info(f"DELETE /posts/{post_id}")
    for i, post in enumerate(db["posts"]):
        if post["id"] == post_id:
            db["posts"].pop(i)
            return {"message": "Post deleted successfully"}
    return {"error": "Post not found"}

# CRUD-запросы для сущности Comment
@app.get("/comments")
async def get_comments():
    logging.info("GET /comments")
    return db["comments"]

@app.get("/comments/{comment_id}")
async def get_comment(comment_id: int):
    logging.info(f"GET /comments/{comment_id}")
    for comment in db["comments"]:
        if comment["id"] == comment_id:
            return comment
    return {"error": "Comment not found"}

@app.post("/comments")
async def create_comment(comment: Comment):
    logging.info(f"POST /comments {comment}")
    db["comments"].append(comment.dict())
    return {"message": "Comment created successfully"}

@app.put("/comments/{comment_id}")
async def update_comment(comment_id: int, comment: Comment):
    logging.info(f"PUT /comments/{comment_id} {comment}")
    for i, c in enumerate(db["comments"]):
        if c["id"] == comment_id:
            db["comments"][i] = comment.dict()
            return {"message": "Comment updated successfully"}
    return {"error": "Comment not found"}

@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int):
    logging.info(f"DELETE /comments/{comment_id}")
    for i, comment in enumerate(db["comments"]):
        if comment["id"] == comment_id:
            db["comments"].pop(i)
            return {"message": "Comment deleted successfully"}
    return {"error": "Comment not found"}

# CRUD-запросы для сущности Profile
@app.get("/profile")
async def get_profile():
    logging.info("GET /profile")
    return db["profile"]

@app.put("/profile")
async def update_profile(profile: Profile):
    logging.info(f"PUT /profile {profile}")
    db["profile"] = profile.dict()
    return {"message": "Profile updated successfully"}

# Генерация случайных данных
fake = Faker()
