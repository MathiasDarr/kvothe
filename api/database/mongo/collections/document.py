from api.database.mongo.bard_db import BardDB


class Documents(BardDB):
    def __init__(self, database):
        self.collection = 'document'
        super().__init__(database)

    def insert(self, results):
        return super().insert(results,"job1")