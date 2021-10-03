import pymongo

conn = pymongo.MongoClient('127.0.0.1', 27017)  # connect to db
db = conn.get_database('community_centre')
db.drop_collection('management_committee')  # clear collection
coll = db.get_collection('management_committee')  # get collection

file = open('VACCINATION.txt', 'r')

for line in file:
    data = line.strip().split(',')  # get the data
    # fit the data into one of the formats
    _id = data[0]
    name = data[1]
    coll.insert_one({'_id': _id, 'name': name})
    if len(data) > 2 and data[2].isdigit():
        date_first_dose = data[2]
        coll.update_one({'_id': _id, 'name': name}, {'$set':{'fdate_irst_dose': date_first_dose}})
    elif len(data) > 2:
        remarks = data[2]
        coll.update_one({'_id': _id, 'name': name}, {'$set':{'remarks': remarks}})
        continue
    if len(data) > 3 and data[3].isdigit():
        date_second_dose = data[3]
        coll.update_one({'_id': _id, 'name': name}, {'$set':{'date_second_dose': date_second_dose}})
    elif len(data) > 3:
        remarks = data[3]
        coll.update_one({'_id': _id, 'name': name}, {'$set':{'remarks': remarks}})
        continue
    if len(data) > 4:
        remarks = data[4]
        coll.update_one({'_id': _id, 'name': name}, {'$set':{'remarks': remarks}})

file.close()
conn.close()