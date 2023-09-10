import pymongo


class Mongo:
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27028
    MONGO_DB = 'local'

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://" + self.MONGO_HOST + ":" + str(self.MONGO_PORT))
        self.db = self.client[self.MONGO_DB]
