import logging
from pymongo import MongoClient
from flask import current_app

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
            database = current_app.config['BARD_DB']
            connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
            client = MongoClient(connector)
            MongoConnection.DATABASE = client[database]

        except Exception as e:
            log.error("Unable to connect to the mongo server {}".format(e))
            raise e