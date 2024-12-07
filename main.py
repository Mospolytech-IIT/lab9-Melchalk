import uvicorn
from starlette.responses import FileResponse
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import sessionmaker
from models import engine

import users_funcs as user
import posts_funcs as post

SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/user/all")
def get_all_user():
    return user.get_all_users(db)

@app.get("/users")
def show_users():
    return FileResponse("pages/user_table.html")

@app.post("/user/add")
def add_user(username = Form(), email = Form(), password=Form()):
    user.add_user(username, email, password, db)
    return FileResponse("pages/user_table.html")

@app.get("/users/add")
def show_add_user():
    return FileResponse("pages/user_add.html")

@app.delete("/users/{id}")
def delete_user(id):
    user.delete_user(id, db)

@app.get("/post/all")
def get_all_post():
    return post.get_all_posts(db)

@app.get("/posts")
def show_posts():
    return FileResponse("pages/post_table.html")

@app.post("/post/add")
def add_post(title = Form(), content = Form(), user_id=Form()):
    post.add_post(title, content, user_id, db)
    return FileResponse("pages/post_table.html")

@app.get("/posts/add")
def show_add_posts():
    return FileResponse("pages/post_add.html")

@app.delete("/posts/{id}")
def delete_post(id):
    post.delete_post(id, db)

uvicorn.run(app, host="127.0.0.1", port=8000)