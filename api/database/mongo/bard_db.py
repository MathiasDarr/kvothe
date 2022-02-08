from logging import getLogger
import uuid
import datetime
import json
from bson import ObjectId

log = getLogger(__name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class BardDB:
    def __init__(self, database):
        self.db = database

    def jsonify(self, results):
        return json.loads(JSONEncoder().encode(results))

    def generateJobId(self):
        return str(uuid.uuid4())

    def insertMany(self, docs, collection=None):
        collection = self.collection if not collection else collection
        if len(docs) > 0:
            try:
                r = self.db[collection].insert_many(docs)
            except Exception as e:
                log.error("Failure on inserting {} documents into {} {}".format(len(docs), collection, e))
                return None

    def insert_one(self, doc, collection=None):
        collection = self.collection if not collection else collection
        try:
            r = self.db[collection].insert_one(doc)
            return str(r.inserted_id)
        except Exception as e:
            log.warn('Failure insering document into {}: {}'.format(collection, e))
            return None

    def insert(self, results, jobName, overwrite=False):
        jobId = self.generateJobId()
        results = [{'jobName': 'Job1'}]
        if self.insertMany(results):
            log.info("Documents inserted into {}".format(len(results), self.collection))
        else:
            return None

    def find(self, collection=None):
        collection = self.collection if not collection else collection
        try:
            cursor = self.db[collection].find({})
            return self.jsonify(list(cursor))
        except Exception as e:
            log.info('Find did not work')
