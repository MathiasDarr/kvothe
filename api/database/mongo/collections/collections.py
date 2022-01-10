from api.database.mongo.bard_db import BardDB


class Collections(BardDB):
    def __init__(self, database):
        self.collection = 'collections'
        super().__init__(database)

    def insert(self, results):
        #return "a"
        return super().insert(results,"job1")