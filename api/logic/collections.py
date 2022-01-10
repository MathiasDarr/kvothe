import logging

from api.database.mongo.collections.document import Documents
from api.database.mongo.collections.collections import Collections
from api.database.mongo.mongo_connection import MongoConnection
import time
import sys
import os
from flask import Flask
import pymongo
import logging
from logging.handlers import RotatingFileHandler
log = logging.getLogger()

# def create_app():
#     app = Flask(__name__)
#     app.config.update(
#         {
#             "FLASK_DEBUG": True
#         }
#     )
#
#     with app.app_context():
#         MongoConnection.initialize()
#     time.sleep(20)
#     # if MongoConnection.DATABASE is None:
#     #     log.error("MONGO DATABASE IS NONE")
#     # else:
#     #     log.warn("MONGO DATABASE IS ALIVE")
#     return app

log = logging.getLogger()

class CollectionsManager:
    def __init__(self):
        MongoConnection.initialize()
        self.BardCollections = Collections(MongoConnection.DATABASE)

    def create_collection(self, collection_name):
        collection = {'name': collection_name}
        result = self.BardCollections.insert(collection)
        #log.warn("THE RESULT LOOKS LIKE: {}".format(result))

    # def query_collections(self):
    #     self.BardCollections.


# class CollectionsManager:
#     def __init__(self):
#         log.warn("THE DATABASE LOOKS LIKE {}".format(MongoConnection.DATABASE))
#         if MongoConnection is None:
#             MongoConnection.initialize()
#
#         # if MongoConnection.DATABASE is None:
#         #     log.error("FROM COLLECTIONS MANAGER MONGO DATABASE IS NONE")
#         # else:
#         #     log.warn("FROM COLLECTIONS MANAGER MONGO DATABASE IS ALIVE")
#         # log.warn("FROM COLLECTIONS MANAGER MONGO DATABASE IS ALIVE")
#         self.BardCollections = Collections(MongoConnection.DATABASE)
#         self.BardDocuments = Documents(MongoConnection.DATABASE)
#         result = self.BardCollections.insertOne({"name":"c1"})
#         #log.warn("THE RESULT LOOKS LIKE: {}".format(result))

#
#     def create_document(self, document_name):
#         document = {'name': document_name}
#         self.BardDocuments.insertOne(document)

