class MongoManager:
    def __init__(self, uri, database_name=None):
        self.uri = uri
        self.database_name = database_name
        self.client = None
        self.database = None

    def connect(self):
        from pymongo import MongoClient
        self.client = MongoClient(self.uri)
        if self.database_name:
            self.database = self.client[self.database_name]
        else:
            raise ValueError("No se especificó un nombre de base de datos.")

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