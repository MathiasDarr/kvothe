import logging

from api.database.mongo.collections.collections import Collections
from api.database.mongo.mongo_connection import MongoConnection


log = logging.getLogger(__name__)

class CollectionsManager:
    def __init__(self):
        MongoConnection.initialize()
        self.BardCollections = Collections(MongoConnection.DATABASE)

    def create_collection(self, name):
        return self.BardCollections.create_collection(name)

    def get_collections(self):
        fetched_collections = self.BardCollections.find()
        log.warn("FETCHED C {}".format(fetched_collections))
        return fetched_collections


