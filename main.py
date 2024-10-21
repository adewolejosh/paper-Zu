
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from pymongo.mongo_client import MongoClient
from redis import Redis

import google.generativeai as genai
import logging
import os


load_dotenv()

# Redis configuration
redis_host = os.environ.get('REDIS_HOST')
redis_port = os.environ.get('REDIS_PORT')
redis = Redis(host=redis_host, port=redis_port)

async def lifespan_events():
    await FastAPILimiter.init(redis)
    yield
    await FastAPILimiter.close()

lifespan_events()

app = FastAPI()
# app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

# Mongo configuration
MONGO_USER = os.environ.get('MONGODB_USER')
MONGO_PASSWORD = os.environ.get('MONGODB_PASSWORD')
MONGO_HOST = os.environ.get('MONGODB_HOST')
uri = f'mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/?retryWrites=true&w=majority&appName=learningCluster'
client = MongoClient(uri)

db = client.sample_paper

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
ai_model = genai.GenerativeModel("gemini-1.5-flash")

try:
    client.admin.command('ping')
    print('pinged')
except Exception as e:
    print(e)

