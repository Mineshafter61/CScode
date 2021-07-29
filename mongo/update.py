import pymongo
client = pymongo.MongoClient("127.0.0.1",27017)
db = client.get_database('entertainment')
coll = db.get_collection('movies')

result = coll.find()
print('All documents in movies collection:')
for document in result:
  print(document)

search = {'year':{'$gt':2016}}
update = {'$set':{'year':2015}}
coll.update_one(search, update)

result = coll.find()
print('All documents in movies collection:')
for document in result:
  print(document)

coll.update_many(search, update)

result = coll.find()
print('All documents in movies collection:')
for document in result:
  print(document)

search = {'year':{'$eq':2018}}
update = {'$unset':{'year':0}}
coll.update_many(search, update)

result = coll.find()
print('All documents in movies collection:')
for document in result:
  print(document)

client.close()
