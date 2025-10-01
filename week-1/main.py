from fastapi import FastAPI
from db import search_posts


app = FastAPI()

@app.get("/")
async def root():
    posts = search_posts()
    return posts
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}