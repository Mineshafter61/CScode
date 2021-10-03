import pymongo
from TASK3_1 import second_dose_date

conn = pymongo.MongoClient('127.0.0.1', 27017)  # connect to db
db = conn.get_database('community_centre')
coll = db.get_collection('management_committee')  # get collection

# user input
while True:
  id = input('Member ID: ')
  if id.isdigit():
    break
  else:
    print('ID must be a number!')

na = True  # invalid ID flag (set to True if id is not found)
for member in coll.find({'_id': id}):
  na = False
  if 'date_second_dose' in member.keys():
    # fully vaccinated
    file = open('TASK3_3.txt', 'w')  # write the CERTIFICATE to file
    file.write('VACCINATION CERTIFICATE\n\nName: {0}\nVaccine type: CoviDie\nDate of first dose: {1}\nDate of second dose: {2}'.format(member['name'], member['date_first_dose'], member['date_second_dose']))
    file.close()
  elif 'date_first_dose' in member.keys():
    print('Date of second dose: {0}'.format(second_dose_date(member['date_first_dose'])))  # print second dose date
  else:
    print('Please take your first dose as soon as possible!')  # not vaccinated

if na:
  print('Member ID not found!')

conn.close()
