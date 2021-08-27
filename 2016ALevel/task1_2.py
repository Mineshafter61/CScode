# Task 1.2
from random import randint

number_list = []
frequency_dict = {}
to_generate = 1000
upper_limit = 20
for i in range(to_generate):
  n = randint(1,upper_limit)
  number_list.append(n)
  if n not in frequency_dict:
    frequency_dict[n] = 1
  else:
    frequency_dict[n] += 1

print("Integer | Frequency | Difference")
for i in range(1, 21):
  print('{0:<7} | {1:<9} | {2:<10}'.format(i, frequency_dict[i], int(abs(frequency_dict[i] - to_generate/upper_limit)) ))
