import sys
import os
from flask import Flask
import pymongo
import logging
from logging.handlers import RotatingFileHandler

from api.views import mount_blueprints
from api.database.mongo.mongo_connection import MongoConnection
import time
log = logging.getLogger()

def create_app():
    app = Flask(__name__)
    app.config.update(
        {
            "FLASK_DEBUG": True
        }
    )

    with app.app_context():
        MongoConnection.initialize()
    #time.sleep(20)
    # if MongoConnection.DATABASE is None:
    #     log.error("MONGO DATABASE IS NONE")
    # else:
    #     log.warn("MONGO DATABASE IS ALIVE")
    mount_blueprints(app)
    setup_logging('development')
    return app


def setup_logging(flask_env):
    logFormatter = logging.Formatter("%(asctime)s")
    log = logging.getLogger('werkzeug')
    if flask_env == 'development':
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.WARN)
    log.propagate = False
    if len(log.handlers) < 1:
        streamHandler = logging.StreamHandler(sys.stdout)
        streamHandler.setFormatter(logFormatter)
        log.addHandler(streamHandler)
    else:
        streamHandler = log.handlers[0]
        streamHandler.setFormatter(logFormatter)
    if not os.path.isdir('logs'):
        os.mkdir('logs')

    fileHandler = RotatingFileHandler("logs/app.log", maxBytes=500000)
    fileHandler.setFormatter(logFormatter)
    log.addHandler(fileHandler)
