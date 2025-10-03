from fastapi import FastAPI
import db


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def get_posts():
    posts = db.search_posts()
    return posts

@app.get("/items/{item_id}")
async def read_item(item_id):
    #retornar dados do item_id do banco de dadaos
    return {"item_id": item_id}

