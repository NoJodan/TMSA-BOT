class MongoManager:
    def __init__(self, uri):
        self.uri = uri
        self.client = None
        self.database = None

    def connect(self):
        from pymongo import MongoClient
        self.client = MongoClient(self.uri)
        self.database = self.client.get_default_database()

    def insert_document(self, collection_name, document):
        collection = self.database[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_document(self, collection_name, query):
        collection = self.database[collection_name]
        document = collection.find_one(query)
        return document

    def close(self):
        if self.client:
            self.client.close()