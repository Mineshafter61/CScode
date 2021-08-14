def ROT_13(string: str):
  returnstr = ''
  for char in string:
    new_ord = ord(char)+13 if char.isalpha() else ord(char)
    if char.isupper() and new_ord > 90:
      new_ord -= 26
    elif char.islower() and new_ord > 122:
      new_ord -= 26
    returnstr = returnstr+chr(new_ord)
    
  return returnstr

def task2_1():
  print( ROT_13(input('String: ')) )

def task2_2():
  string = input('String: ')
  doubleR13 = ROT_13(ROT_13(string))
  print(doubleR13)
  print('Is the resulting string equal to the original string?', ('No','Yes')[doubleR13==string] )

if __name__ == '__main__':
  task2_1()
  task2_2()
