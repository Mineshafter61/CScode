class Record:
  def __init__(self, PersonName, TelephoneNumber):
    self.__PersonName = PersonName
    self.__TelephoneNumber = TelephoneNumber

  def setPersonName(self, PersonName):
    self.__PersonName = PersonName

  def getPersonName(self):
    return self.__PersonName

  def setTelephoneNumber(self, TelephoneNumber):
    self.__TelephoneNumber = TelephoneNumber

  def getTelephoneNumber(self):
    return self.__TelephoneNumber


class HashTable:
  """docstring for HashTable."""

  def __init__(self, size=500):
    self.__size = size
    self.__table = [Record for i in range(self.__size)]

  def insert(self, index, record):
    self.__table[index] = record

  def get(self, index):
    return self.__table[index]

  def DisplayValues(self):
    print('Index | PersonName | TelephoneNumber')
    print('*'*36)
    for record in range(self.__size):
      print('{0:>3} | {1:^10} | {2:^15}')


def GenerateHash(SearchName):
  HashTotal = 0
  pos = 1
  for Character in SearchName:
    ascii = int(ord(Character))
    ascii *= pos
    HashTotal += ascii
    pos += 1
  Hash = HashTotal % 500
  return Hash


def search(SearchName, hash_table):
  # hash_table is a HashTable object
  hash = GenerateHash(SearchName)
  name = hash_table.get(hash).getPersonName()
  while name != SearchName and name != '':
    hash += 1
    name = hash_table.get(hash).getPersonName()
  # name either found or not found
  if name == '':
    return 'NOT FOUND'
  else:
    return hash, name, hash_table.get(hash).getTelephoneNumber()


if __name__ == '__main__':
  with open('HASHEDDATA.TXT', 'r') as f:
    index = 0
    h = HashTable(500)
    for line in f:
      i,name,tel = line.split(',')
      if name and tel:
        r = Record(name, tel)
        h.insert(int(i), r)
      else:
        continue
  h.DisplayValues()


  print(GenerateHash('Tait Davinder'))
  print(GenerateHash('Anandan Yeo'))


  print(search('Charlie Love', h))
  print(search('Chin Tan', h))
  print(search('John Barrowman', h))
