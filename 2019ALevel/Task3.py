class ToDo:

  
  ## Task 3.1
  def __init__(self, c: str, d: str): # Constructor
    self.__category = c
    self.__description = d

  def set_category(self, s: str):
    self.__category = s

  def set_description(self, s: str):
    self.__description = s

  def get_category(self):
    return self.__category

  def set_category(self):
    return self.__description

  def summary(self):
    return self.__category+'|'+self.__description

  def __str__(self):
    return self.summary()


  ## Task 3.2

  def compare_with(self, td: DatedToDo):
    # First few lines for greater than (we add this to the return statement)
    # Next few lines for less than (we subtract this from the return statement)
    return ( \
           (self.__category > other.get_category()) or \
           (self.__category == other.get_category() and self.__description > other.get_description()) \
           ) - ( \
           (self.__category < other.get_category()) or \
           (self.__category == other.get_category() and self.__description < other.get_description()) \
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
    return self.__category+'|'+self.__description+'|'+self.__due_date

  def __str__(self):
    return self.summary()

  def compare_with(self, td: DatedToDo):
    # First few lines for greater than (we add this to the return statement)
    # Next few lines for less than (we subtract this from the return statement)
    return ( \
           (self.__category > other.get_category()) or \
           (self.__category == other.get_category() and self.__description > other.get_description()) or \
           (self.__category == other.get_category() and self.__description == other.get_description() and self.__due_date > other.get_due_date()) \
           ) - ( \
           (self.__category < other.get_category()) or \
           (self.__category == other.get_category() and self.__description < other.get_description()) or \
           (self.__category == other.get_category() and self.__description == other.get_description() and self.__due_date < other.get_due_date()) \
           )

if __name__ == '__main__':
  # open text file and do stuff
