# database.py - functions for managing database

from pymongo import MongoClient

import json
config = {}
with open("./config.json") as f:
    config = json.load(f)

client = MongoClient(f"mongodb+srv://mongo:{config.get('password')}@adbms.ntgiqfs.mongodb.net/?retryWrites=true&w=majority")

from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection


def get_items(id=None):
    if id is None:
        items = list_collection.find({})
    else:
        items = list_collection.find({'_id': ObjectId(id)})
    items = [{'id': str(item['_id']), 'description': item['description'], 'quantity': item.get('quantity', 1)} for item in items]
    return items


def add_item(description):
    list_collection.insert_one({'description': description})


def add_item(description, quantity):
    list_collection.insert_one({'description': description, 'quantity': quantity})


def delete_item(id):
    list_collection.delete_one({'_id': ObjectId(id)})


def update_item(id, description):
    list_collection.update_one({'_id': ObjectId(id)}, {'$set': {'description': description}})
