# Task 2.3
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

ID = int(input('ID: '))
ID_addr = ID % Max
stop_loop = Max + 1
while HashTable[ID_addr] != ID:
  stop_loop = ID % Max
  if ID_addr < 19:
    ID_addr += 1
  else:
    ID_addr = 0
  if ID_addr == stop_loop:
    break
if ID_addr == stop_loop:
  print('Not found')
else:
  print(ID_addr)

keysf.close()
