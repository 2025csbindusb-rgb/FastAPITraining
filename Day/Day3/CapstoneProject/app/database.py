#This file creates a single, shared connnection to ManogoDB using pymongo
from pymongo import MongoClient
from pymongo.database import Database
from app.config import settings

#MangoClient manages a pool connections to the MangoDB server.
client : MongoClient=MongoClient(settings.MONGO_URI)
database : Database=client[settings.MONGO_DB_NAME]

#Sends the ping command to MangoDB to confirm the connection is alive
def ping_database()->bool:
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False
    