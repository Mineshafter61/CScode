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
class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day
    
class DatedToDo(ToDo):
  def __init__(self, dt: Date, c: str, d: str):
    super().__init__(c, d)
    self.__due_date = dt

  def set_due_date(self, d: Date):
    self.__due_date = d

  def get_due_date:
    return self.__due_date

  def summary(self):
    return str(self.__category) + '|' + str(self.__description) + '|' + str(self.__due_date)

  def __str__(self):
    return self.summary()

  def compare_with(self, td: DatedToDo):
    # First few lines for greater than (we add this to the return statement)
    # Next few lines for less than (we subtract this from the return statement)
    return ( \
           (self.__category > td.get_category()) or \
           (self.__category == td.get_category() and self.__description > td.get_description()) or \
           (self.__category == td.get_category() and self.__description == td.get_description() and self.__due_date > td.get_due_date()) \
           ) - ( \
           (self.__category < td.get_category()) or \
           (self.__category == td.get_category() and self.__description < td.get_description()) or \
           (self.__category == td.get_category() and self.__description == td.get_description() and self.__due_date < td.get_due_date()) \
           )

if __name__ == '__main__':
  tasks = [ToDo("reading", "Try some Shakespeare"), ToDo("shopping","Consider items to recycle"), ToDo("reading", "Search on the web"), ToDo("reading", "Go to the library")]
  
