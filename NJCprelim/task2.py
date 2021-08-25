# Task 2.1
import json
with open("RESTAURANTS.json", 'r') as restaurantsf:
  restaurantsdict = json.loads(restaurantsf.read())
restaurants = {}
for restaurant_name in restaurantsdict:
  if restaurant_name not in restaurants:
    if type(restaurantsdict[restaurant_name]) != float:
      restaurants[restaurant_name] = 0.0
    else:
      restaurants[restaurant_name] = restaurantsdict[restaurant_name]

print(restaurants)


# Task 2.2
def mergeSort(arr):
  if len(arr) == 1:
    return arr
  else:
    m = len(arr) // 2
    return merge(mergeSort(arr[:m]), mergeSort(arr[m:]))

def merge(l_arr, r_arr):
  m_arr = [None for i in range(len(l_arr) + len(r_arr))]
  i, j, k = 0, 0, 0
  while i < len(l_arr) and j < len(r_arr):
    if l_arr[i] > r_arr[j]:
      m_arr[k] = l_arr[i]
      i += 1
    else:
      m_arr[k] = r_arr[j]
      j += 1
    k += 1
  while i < len(l_arr):
    m_arr[k] = l_arr[i]
    i += 1
    k += 1
  while j < len(r_arr):
    m_arr[k] = r_arr[j]
    j += 1
    k += 1
  return m_arr

# Task 2.3
ratings_first_list = [(restaurants[restaurant], restaurant) for restaurant in restaurants]
ratings_first_list = mergeSort(ratings_first_list)
for restaurant in ratings_first_list[0:10]:
  print(restaurant[1])

# Task 2.4
import pymongo

client = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = client.get_database('Entertainment')
coll = db.get_collection('Restaurants')

for restaurant in ratings_first_list:
  coll.insert_one({restaurant[1]: restaurant[0]})

print(coll.count_documents())

client.close()
