from api.database.mongo.bard_db import BardDB


class Collections(BardDB):
    def __init__(self, database):
        self.collection = 'collections'
        super().__init__(database)

    def insert(self, results):
        return super().insert(results,"job1")

    def create_collection(self, name):
        doc = {
            'name': name
        }
        return self.insert_one(doc, self.collection)