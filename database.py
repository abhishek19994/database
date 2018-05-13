import pymongo
class Database(object):
    URI="mongodb://127.0.0.1:27017"
    database=None
    @staticmethod
    def initialise():
        client=pymongo.MongoClient(Database.URI)
        Database.database=client['fullstack']
    @staticmethod
    def insert(collection,data):
        Database.database[collection].insert(data)
    @staticmethod
    def find(collection,data):
        return Database.database[collection].find(data)
    @staticmethod
    def find_one(collection,data):
        return Database.database[collection].find_one(data)
        
