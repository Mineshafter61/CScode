# Task 2.1
keysf = open('KEYS1.TXT', 'r')
Max = 20
HashTable = [None for i in range(Max)]
numbers = [int(i) for i in keysf]
for n in numbers:
  Address = n % Max
  HashTable[Address] = n

for data in HashTable:
  if data is not None:
    print(data)
keysf.close()
