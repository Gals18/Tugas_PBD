import pymongo

db = pymongo.MongoClient("mongodb://localhost:27017/")

dbku = db["dbTugas"]
collectionku = dbku['dbcolom']

for dbcolom in collectionku.find():
  print(dbcolom)