import logging
from pymongo import MongoClient


log = logging.getLogger()

class MongoConnection:
    DATABASE = None
    CONNECTION_TIMEOUT = 5000

    @staticmethod
    def initialize():
        try:
            config = {
                "username": "bard",
                "password": "bard",
                "server": "mongo",
            }
            database = 'bard-db'
            connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
            client = MongoClient(connector)
            db = client[database]
            doc1 = db.collections.insert_one({'doc1':'a'})
            #log.warn("DOC1: {}".format(doc1))
            # log.warn(client.server_info())
            MongoConnection.DATABASE = client[database]
            collections = db.collections.find({})
            log.warn("COLLECTIONS LOOK LIKE: {}".format(collections))
            log.warn("THE DATABASE LOOKS LIKE {}".format(MongoConnection.DATABASE))

        except Exception as e:
            log.error("Unable to connect to the mongo server {}".format(e))
            raise e