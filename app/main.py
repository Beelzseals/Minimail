from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os


load_dotenv()
app = FastAPI(title="Minimail API")


@app.get("/")
async def root():
    return {"message": "Welcome to the Minimail API!"}
