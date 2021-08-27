# Task 2.2
keysf = open('KEYS2.TXT', 'r')
Max = 20
HashTable = [None for i in range(Max)]
numbers = [int(i) for i in keysf]
for n in numbers:
  Address = n % Max
  while HashTable[Address] is not None:
    if Address < 19:
      Address += 1
    else:
      Address = 0
  HashTable[Address] = n

print(HashTable)
for data in HashTable:
  if data is not None:
    print(data)
keysf.close()
