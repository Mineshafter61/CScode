class ToDo:

  
## Task 3.1
  def __init__(self, c: str, d: str): # Constructor
    self.__category = str(c)
    self.__description = str(d)

  def set_category(self, s: str):
    self.__category = str(s)

  def set_description(self, s: str):
    self.__description = str(s)

  def get_category(self):
    return self.__category

  def set_category(self):
    return self.__description

  def summary(self):
    return str(self.__category) + '|' + str(self.__description)

  def __str__(self):
    return self.summary()


## Task 3.2
  def compare_with(self, td: DatedToDo):
    # First few lines for greater than (we add this to the return statement)
    # Next few lines for less than (we subtract this from the return statement)
    return ( \
           (self.__category > td.get_category()) or \
           (self.__category == td.get_category() and self.__description > td.get_description()) \
           ) - ( \
           (self.__category < td.get_category()) or \
           (self.__category == td.get_category() and self.__description < td.get_description()) \
           )


## Task 3.3
    
class DatedToDo(ToDo):
  def __init__(self, dt: str, c: str, d: str):
    super().__init__(c, d)
    self.__due_date = str(dt)

  def set_due_date(self, d: str):
    self.__due_date = str(d)

  def get_due_date:
    return self.__due_date

  def summary(self):
    return super().summary() + str(self.__due_date)

  def __str__(self):
    return self.summary()

  def compare_with(self, td: DatedToDo):
    # First few lines for greater than (we add this to the return statement)
    # Next few lines for less than (we subtract this from the return statement)
    if type(self) != DatedToDo or type(td) != DatedToDo:
      if type(self) == DatedToDo: return 1
      elif type(td) == DatedToDo: return -1
      else:
        return super().compare_with(td)
    elif self.get_due_date() == td.get_due_date():
      

if __name__ == '__main__':

  TaskList = []
  
  tasks = [ToDo("reading", "Try some Shakespeare"), \
           ToDo("shopping","Consider items to recycle"), \
           ToDo("reading", "Search on the web"), \
           ToDo("reading", "Go to the library")\
           ]

  tasks_3 = [ToDo("reading", "Try some Shakespeare"), \
             DatedToDo("2019-12-15", "shopping", "buy bread"), \
             DatedToDo("2019-12-01", "reading", "read the newspapers"), \
           ToDo("shopping","Consider items to recycle"), \
           ToDo("reading", "Search on the web"), \
             DatedToDo("2019-11-21", "shopping", "buy lemons"), \
           ToDo("reading", "Go to the library")\
           ]

  def AddToList(tasks, TaskList):
    for eachtask in tasks:
      if len(TaskList) == 0:  # TaskList is empty
        TaskList.append(eachTask)  # add first task into TaskList
      else:
        current = 0
        while current < len(TaskList) and TaskList[current].compare_with(eachTask) == -1:
          current += 1
        if current == 0:  # insert as first object in TaskList
          TaskList.insert(0, eachTask)
        elif TaskList[current-1].compare_with(eachTask) == 1:
          TaskList.insert(current-1, eachTask)
        else:  # 0 or 1
          TaskList.insert(current, eachTask)
    return TaskList

  TaskList = AddToList(tasks, TaskList)
  for each in TaskList:
    print(each.summary())


  # Task 3.4

  CompletedTasks = [ToDo("reading", "try some Shakespeare"), \
                    ToDo("shopping", "buy bread"), \
                    DatedToDo("2019-11-21", "shopping", "buy lemons"), \
                    ToDo("watching", "go to the cinema")]

  for first in CompletedTasks:
    removed = False
    for second in TaskList:
      if type(first) == type(second):
        if first.compare_with(second) == 0:
          TaskList.remove(second)
          removed = True
    if removed == False:
      print("Completed task not found!")

  for each in TaskList:
    print(each.summary())
  
  
