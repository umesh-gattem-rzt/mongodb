from pymongo import MongoClient

client = MongoClient()

print(client.list_database_names())

client.drop_database("sample_mongo")

print(client.list_database_names())

# Drop Collection in database

for database in client.list_database_names():
    collections = client[database].collection_names()
    for collection in collections:
        if database == "primer" and collection == "dataset":
            client[database].drop_collection(collection)
