## Task 2.1
'''
A: Low > High
B: IntDiv(High+Low,2)  // IntDiv(a,b) returns the integer division of a and b.
C: RETURN BinarySearch(ThisArray, FindValue, Middle, High)
'''


## Task 2.2
def InitialiseAnimals():
  with open('ANIMALS.TXT', 'r') as animalsf:
    return [animal for animal in animalsf]

def BinarySearch(ThisArray, FindValue, Low, High):
  Middle = 0  # 0 is an integer
  if Low > High:
    return -1 # not found
  else:
    # calculate new Middle value
    Middle = (Low+High) // 2
    if ThisArray[Middle] > FindValue:
      return BinarySearch(ThisArray, FindValue, Low, Middle-1)
    elif ThisArray[Middle] < FindValue:
      return BinarySearch(ThisArray, FindValue, Middle, High)
    else:
      return Middle

def main2_2():
  MyAnimal = InitialiseAnimals()
  animal = input('Animal name?')
  index = BinarySearch(MyAnimal, animal, 0, len(MyAnimal))
  if index == -1:
    # not found
    print('Animal not found')
  else:
    print('Animal found at index', index)


## Task 2.3
def InitialiseAnimals():
  with open('ANIMALS.TXT', 'r') as animalsf:
    return [animal for animal in animalsf]

def BinarySearch(ThisArray, FindValue, Low, High, Calls):
  Middle = 0  # 0 is an integer
  if Low > High:
    return -1 # not found
  else:
    # calculate new Middle value
    Middle = (Low+High) // 2
    if ThisArray[Middle] > FindValue:
      return BinarySearch(ThisArray, FindValue, Low, Middle-1, Calls+1)
    elif ThisArray[Middle] < FindValue:
      return BinarySearch(ThisArray, FindValue, Middle, High, Calls+1)
    else:
      return Middle, Calls

def main2_3():
  MyAnimal = InitialiseAnimals()
  animal = input('Animal name?')
  index, calls = BinarySearch(MyAnimal, animal, 0, len(MyAnimal), 1)  # No. of calls start from 1 because there will always be at least 1 call.
  if index == -1:
    # not found
    print('Animal not found')
  else:
    print('Animal found at index', index)
    print('Number of function calls:', calls)
