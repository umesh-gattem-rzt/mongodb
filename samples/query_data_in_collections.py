from pymongo import MongoClient

client = MongoClient()

db = client.test

# Finds the whole document in primer dataset and student collection
document = db.model_meta.find()
for record in document:
    print(record)

# To find particular key
find_network_name = db.model_meta.find({"0.network_name": "titanic_data"})

for network_name in find_network_name:
    print(network_name)


