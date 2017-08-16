from pymongo import MongoClient

client = MongoClient('localhost', 27017)
print(client)
db = client.test_database
print(db)
