## Task 4.1 ##

'''
Use a 2d array to define the pond, x and y coordinates represented in ROW and COL.
Water in the pond is represented by the character '.'
function declare_pond is used to define the 2d array.
function display_grid takes the 2d array and displays it.
'''

ROW = 8   # define constants for row and column
COL = 15

def declare_pond():
  return [['.' for x in range(COL)] for y in range(ROW)]

def display_grid(pond):
  for x in range(ROW):
    for y in range(COL):
      print(pond[x][y], end='')
    print()
    

## Task 4.2 ##

pond = declare_pond()
x = eval(input('X coordinate <1 to 8> ?  '))
y = eval(input('Y coordinate <1 to 15> ? '))
pond[x-1][y-1] = 'S'
display_grid(pond);print('========')


## Task 4.3 ##

from random import randint

pond = declare_pond()

fish_pos = []
for i in range(3):
  fish_p = (randint(1,8), randint(1,15))
  while fish_p in fish_pos:
    fish_p = (randint(1,8), randint(1,15))
  fish_pos.append(fish_p)

for p in fish_pos:
  pond[p[0]-1][p[1]-1] = 'F'
  
display_grid(pond);print('========')


## Task 4.4 ##

from random import randint

pond = declare_pond()

fish_pos = []
for i in range(3):
  fish_p = (randint(1,8), randint(1,15))
  while fish_p in fish_pos:
    fish_p = (randint(1,8), randint(1,15))
  fish_pos.append(fish_p)

for p in fish_pos:
  pond[p[0]-1][p[1]-1] = 'F'

x = eval(input('X coordinate <1 to 8> ?  '))
y = eval(input('Y coordinate <1 to 15> ? '))
pond[x-1][y-1] = 'PH'[int( pond[x-1][y-1]=='F' )]
display_grid(pond);print('========')
