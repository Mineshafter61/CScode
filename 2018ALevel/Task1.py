if __name__ == '__main__':
  step_list = []
  for i in range(10):
    print('(If there are no more entries left, press ENTER without typing anything)')
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
    savedlines = [line for line in starf]
    starName = savedlines[-2].strip()
    starStep = savedlines[-1].strip()[1:]
    print("Last week, {0} was 'Star of the Week' with {1} steps taken.".format(starName, starStep))
    print("This week, {0} is 'Star of the Week' with {1} steps taken.".format(step_list[-1][1], step_list[-1][0]))
    starf.write(str(step_list[-1][1])+'\n,'+str(step_list[-1][0])+'\n')
