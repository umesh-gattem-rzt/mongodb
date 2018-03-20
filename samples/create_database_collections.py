import os

from pymongo import MongoClient

client = MongoClient()

db = client.test_mongo
collection = db.mongo_collection

print(client.database_names())

file_path = '/'.join(str(__file__).split('/')[:-1]) + "/primer-dataset.json"

# neither the database nor the collection are created until you attempt to write a document.
os.system("mongoimport --db test_mongo --collection mongo_collection --file " + file_path)


# If you want to drop the currect collection and insert file then use this command
# os.system("mongoimport --db test_mongo --collection mongo_collection --drop --file " + file_path)

print(client.database_names())
