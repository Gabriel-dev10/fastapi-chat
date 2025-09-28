from pymongo import MongoClient
from app.config import MONGO_URL, MONGO_DB

# Initialize MongoDB client
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_messages():
    return list(db.messages.find())

def save_message(message):
    return db.messages.insert_one(message)