## Task 1

def decoder():
  def uppercase(number):
    remainder = int(number)%27
    if remainder:
      return chr(remainder+64)
    else:
      return 0

  def lowercase(number):
    remainder = int(number)%27
    if remainder:
      return chr(remainder+96)
    else:
      return 0

  def punctuation(number):
    return [0,'!','?',',','.',' ',';','"',"'"][int(number)%9]
  with open('textstream.txt', 'r') as textstream:
    message = textstream.readline().strip().split(',')

    # Gets the 3 decoders and set the current decoder to uppercase
    mode = [uppercase, lowercase, punctuation]; m = 0;

    # Init finalresult string
    finalresult = ''
    for number in message:
      # mode[m] is a function
      newchr = mode[m](number)
      if newchr == 0:
        # switch modes if the function returns 0
        m = m+1 if m < 2 else 0
      else:
        finalresult = finalresult + newchr

  # Output
  return finalresult

print(decoder())


## Task 2

def encoder(message):
  def uppercase(char):
    return ord(char)-64

  def lowercase(char):
    return ord(char)-96

  def punctuation(char):
    return [0,'!','?',',','.',' ',';','"',"'"].index(char)

  mode = [uppercase, lowercase, punctuation]; m = 0;
  charset = ([chr(z) for z in range(65,91)],[chr(z) for z in range(97,123)],['!','?',',','.',' ',';','"',"'"])
  finalresult = []
  for char in message:
    if char in charset[m]:
      finalresult.append(mode[m](char))
    else:
      finalresult.append(0)
      m = m+1 if m < 2 else 0
      finalresult.append(mode[m](char))

  return finalresult

print(encoder('What a wonderful day!'))


## Task 3

from random import randint
def random_encoder(message):
  def uppercase(char):
    return ord(char)-64

  def lowercase(char):
    return ord(char)-96

  def punctuation(char):
    return [0,'!','?',',','.',' ',';','"',"'"].index(char)

  mode = [uppercase, lowercase, punctuation]; m = 0;
  charset = ([chr(z) for z in range(65,91)],[chr(z) for z in range(97,123)],['!','?',',','.',' ',';','"',"'"])
  finalresult = []
  for char in message:
    if char in charset[m]:
      finalresult.append(randint(1,17)*mode[m](char))
    else:
      finalresult.append(0)
      m = m+1 if m < 2 else 0
      finalresult.append(randint(1,17)*mode[m](char))

  return finalresult
