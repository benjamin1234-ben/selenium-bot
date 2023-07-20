from pymongo import MongoClient

import logging

def connect_db(uri : str):
    try:
        client = MongoClient(uri)
        db = client["oddz_dev"]
    except TimeoutError:
        logging.error("Cannot connect to database, may be due to poor network connectivity")
        connect_db(uri=uri)
    else:
        print(type(db))
        return db

def get_users(db):
    try:
        users = db.collection["users"].find()
    except TimeoutError:
        logging.error("Cannot retreive user data from database, may be due to poor network connectivity")
    else:
        print(type(users))
        return users