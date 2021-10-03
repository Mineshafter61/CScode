import pymongo

conn = pymongo.MongoClient('127.0.0.1', 27017)  # connect to db
db = conn.get_database('community_centre')
db.drop_collection('management_committee')  # clear collection
coll = db.get_collection('management_committee')  # get collection

# user input
while True:
  id = input('Member ID: ')
  if id.isdigit():
    break
  else:
    print('ID must be a number!')

cursor = coll.find({'_id': id})
try:
  for member in cursor:
    print(member)
except:
  print('There is no member with that ID!')

cursor.close()
conn.close()