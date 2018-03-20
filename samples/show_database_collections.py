from pymongo import MongoClient

client = MongoClient()
print(client.list_database_names())

for database in client.list_database_names():
    print(database, ":", client[database].collection_names())

