# Task 1.1
from random import randint

number_list = []
frequency_dict = {}
for i in range(1000):
  n = randint(1,20)
  number_list.append(n)
  if n not in frequency_dict:
    frequency_dict[n] = 1
  else:
    frequency_dict[n] += 1

print("Integer | Frequency")
for i in range(1, 21):
  print('{0:<7} | {1:<9}'.format(i, frequency_dict[i]))
