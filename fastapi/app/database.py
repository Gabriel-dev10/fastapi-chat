"""
Module for MongoDB connection and database operations.
"""

from pymongo import MongoClient
from app.config import MONGO_URL, MONGO_DB

# Initialize MongoDB client
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]

def get_messages():
    """Retrieve all messages from the database."""
    return list(db.messages.find())

def save_message(message):
    """Save a new message to the database."""
    return db.messages.insert_one(message)