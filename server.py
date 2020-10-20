import os
from fastapi import FastAPI

app = FastAPI()

APP_NAME = os.getenv('APP_NAME', 'MY API')

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "APP_NAME" : APP_NAME,
    }
