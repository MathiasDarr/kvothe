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
            MongoConnection.DATABASE = client[database]

        except Exception as e:
            log.error("Unable to connect to the mongo server {}".format(e))
            raise e