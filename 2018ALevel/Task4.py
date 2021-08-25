with open('MAZE.TXT','r') as mazef:
  maze = [[c for c in l if c!='\n'] for l in mazef]
#[print(i) for i in maze]


# Generate prize location
from random import randint
x = randint(0,9)
y = randint(0, 10)
while maze[y][x] == 'X':
  x = randint(0,9)
  y = randint(0, 10)
maze[y][x] = 'P'  # prize location
#[print(i) for i in maze]


p_pos = [4, 5]  # initialise player pos
maze[p_pos[1]][p_pos[0]] = 'O'  # set player pos to O
[print(''.join(i)) for i in maze]  # (display)
prev = ''  # var for previous move
while p_pos != [x, y]:  # check if player is at prize location
  
   # player input
  action = input('Direction: ').upper() 
  while not (action in 'UDLR' or action == ''):
    print('Invalid direction!')
    action = input('Direction: ').upper()
  # check if first move
  if action == '' and prev != '':
    action = prev
  elif prev == '':
    while not (action in 'UDLR'):
      print('Invalid direction!')
      action = input('Direction: ')

  # update player pos
  maze[p_pos[1]][p_pos[0]] = '.'  # reset current pos
  if action == 'U':
    if maze[p_pos[1]-1][p_pos[0]] != 'X':  # check if wall
      p_pos[1] -= 1
  elif action == 'D':
    if maze[p_pos[1]+1][p_pos[0]] != 'X':  # check if wall
      p_pos[1] += 1
  elif action == 'L':
    if maze[p_pos[1]][p_pos[0]-1] != 'X':  # check if wall
      p_pos[0] -= 1
  elif action == 'R':
    if maze[p_pos[1]][p_pos[0]+1] != 'X':  # check if wall
      p_pos[0] += 1
  prev = action  # store previous action
  maze[p_pos[1]][p_pos[0]] = 'O'  # set new player pos to O

  [print(''.join(i)) for i in maze]

# got prize
print('Player has reached the prize')
