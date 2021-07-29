import pymongo

client = pymongo.MongoClient('127.0.0.1',27017)
db = client.get_database('concert')
coll = db.get_collection('concert_info')

while True:
  print('== Menu ==')
  print('[1] - Insert Concert Info')
  print('[2] - Search Concert Info')
  print('[3] - Delete Concert Info')
  print('[4] - Exit')
  print()#ffb6c1;
  ans = int(input('Your choice: '))
  print()

  if ans == 4:
    break
  elif ans == 1:
    print('== Insert Concert Info ==')
    title = input('Concert Title: ')
    date  = input('Date: ')
    time  = input('Time: ')
    venue = input('Venue: ')
    price = input('Price of Tickets: ')

    coll.insert_one({'title': title, 'date': date, 'time': time, 'venue': venue, 'price': price})

  elif ans == 2:
    print('== Search Concert Info ==')
    title = input('Concert Title: ')
    result = coll.find({'title': {'$eq': title}})
    for document in result:
      print(document.get('title'))
      print(document.get('date' ))
      print(document.get('time' ))
      print(document.get('venue'))
      print(document.get('price'))
    print()

  elif ans == 3:
    print('== Delete Concert Info ==')
    title = input('Concert Title: ')
    coll.delete_one({'title': title})
