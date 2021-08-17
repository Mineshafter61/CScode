if __name__ == '__main__':
  step_list = []
  for i in range(10):
    print('(If there are no more entries left, press ENTER without typing anything)')
    name = input('Enter Name {}: '.format(i+1))
    while not name.isalpha():
      print('Invalid input!')
      name = input('Enter Name {}: '.format(i+1))
    if name == '':
      break
    steps = input('Enter Steps: ')
    while not steps.isdigit() or int(steps)<0 or int(steps)>100000:
      print('Invalid input!')
      steps = input('Enter Steps: ')
    steps = int(steps)

    step_list.append((steps, name))

  step_list.sort()

  with open('STAR.TXT', 'r+') as starf:
    a = starf.readlines()
    try:
      star = a[-1].split(',')
    except:
      print("This week, {0} is 'Star of the Week' with {1} steps taken.".format(step_list[-1][1], step_list[-1][0]))
      for line in starf:
        starf.write(line)
      starf.write('\n'+str(step_list[-1][1])+','+str(step_list[-1][0]))
    else:
      print("Last week, {0} was 'Star of the Week' with {1} steps taken.".format(star[0], star[1]))
      print("This week, {0} is 'Star of the Week' with {1} steps taken.".format(step_list[-1][1], step_list[-1][0]))
      for line in starf:
        starf.write(line)
      starf.write('\n'+str(step_list[-1][1])+','+str(step_list[-1][0]))
