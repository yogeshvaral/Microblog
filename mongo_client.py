import os
from pymongo import MongoClient

MONGO_URL = "mongodb://image-gallary_mongo_1"
# MONGO_URL = "mongodb://root:mypassword@mongo:27017/"
MONGO_USERNAME = "root"
MONGO_PASSWORD = "mypassword"
MONGO_PORT = "27017"

mongo_client = MongoClient(
    host=MONGO_URL,
    username=MONGO_USERNAME,
    password=MONGO_PASSWORD,
    port=int(MONGO_PORT),
)


def insert_test_document():
    """insert sample document to test connection to DB"""
    db = mongo_client.test
    test_collection = db.test_collection
    res = test_collection.insert_one({"name": "Yogesh", "instructor": True})
    print(res)
