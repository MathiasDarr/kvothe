import logging
import uuid
import datetime

log = logging.getLogger()

class BardDB():
    def __init__(self, database):
        self.db = database
        self.log = logging.getLogger('werkzeug')
        #log.warn("FFROM BARD DB")
        #self.log.warn("from bard da")
    def generateJobId(self):
        return str(uuid.uuid4())

    def insertMany(self, docs, collection=None):
        collection = self.collection if not collection else collection
        if len(docs) > 0:
            try:
                log.warn("YESSSS")
                r = self.db[collection].insert_many(docs)
                log.warn("AND THE RESULT LOOKS LIKE : {}".format(r))
                log.warn("{}: Insertubg {} documents into {}".format(datetime.datetime.now(), len(docs), collection))
            except Exception as e:
                log.error("Failure on inserting {} documents into {} {}".format(len(docs), collection, e))
                return None


    def insertOne(self, doc, collection=None):
        collection = self.collection if not collection else collection
        #log.warn("THE COLLECSTIN LOOKS LIKE: {}".format(collection))
        try:
            #log.warn("THE DATABASE LOOKS LIKE: {}".format(self.db))
            # r = self.db[collection].insert_one(doc)
            #log.warn("THE RESULT OF INSERT_ONE IS {}".format(r))
            return True
        except Exception as e:
            log.warn('Failure insering document into {}: {}'.format(collection, e))
            return None


    def insert(self, results, jobName, overwrite=False):
        jobId = self.generateJobId()
        log.warn("WHAT")
        results = [ {'jobName': 'Job1'}]
        # for result in results:
        #     if result:
        #         result['jobId'] = jobId
        #         result['jobName'] = jobName
        if self.insertMany(results):
            log.info("Documents inserted into {}".format(len(results), self.collection))
        else:
             return None
    def find(self, collection):
        collection = self.collection if not collection else collection
        try:
            return self.db[collection].find({})
        except Exception as e:
            log.warn('Find did not work')