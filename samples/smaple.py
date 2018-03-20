from pymongo import MongoClient
import os

client = MongoClient()

db = client.primer

# cursor = db.student.find({'address.building': '7316'})
# os.system("mongoimport --db primer --collection dataset --file /Users/umesh/Desktop/primer-dataset.json")
cursor = db.dataset.find({"0.network_name": "titanic_data"})
# print(cursor)
# cursor = db.student.find()
for document in cursor:
    print(document)
