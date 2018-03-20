from pymongo import MongoClient

client = MongoClient()

db = client.test
collection = db.model_meta


# If the collection does not currently exist, insert operations will create the collection.

db.model_meta.insert([{
    "name": "umesh",
    "marks": 90
},
    {
        "name": "RAJ",
        "marks": 91
    },
    {
        "name": "Kumar",
        "marks": 92
    }])

print(client.database_names())

# Specify Conditions with Operators

document = collection.find({"marks": {"$gt": 90}})

for record in document:
    print(record)
