import pymongo
from pymongo import MongoClient
from bson.dbref import DBRef

config = {
    "username": "bard",
    "password": "bard",
    "server": "mongo",
}

connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = MongoClient(connector)

db = client['bard-db']
collections = db.collections
documents = db.documents

collections.insert_one({'name':'collection_1'})
documents.insert_one({'name': 'document_1'})

collection1 = collections.find_one({'name':'collection_1'})

documents.insert_one({'name':'first_document', 'collection': collection1['_id']})

first_document = documents.find_one({'name':'first_document'})
