class Person(object):
  def __init__(self, name, age, sex, contact):
    self.__name = name
    self.__age  = age
    self.__sex  = sex
    self.__contact = contact

  # modifier
  def setName(self, name):
    self.__name = name
  def setAge(self, age):
    self.__age  = age
  def setSex(self, sex):
    self.__sex  = sex
  def setContact(self, contact):
    self.__contact = contact

  # accessor
  def getName(self):
    return self.__name
  def getAge(self):
    return self.__age
  def getSex(self):
    return self.__sex
  def getContact(self):
    return self.__contact

  def display(self):
    print('Name:', self.__name)
    print('Age: ', self.__age)
    print('Sex: ', self.__sex)
    print('Contact: ', self.__context)

  def setFavFood(self, food=None):
    if food == None:
      food = input("{}, what's your favourite food?".format(self.__name))
    self.__favFood = food

  def getFavFood(self):
    return self.__favFood

class Student(Person):
  def __init__(self, name, age, sex, contact,school=None):
    super().__init__(name, age, sex, contact)
    if school == None:
      school = input("{}, what's your school?".format(self.getName()))
    self.__school = school

  def display(self):
    super().display()
    print("School:", self.__school)

  def setPocketMoney(self, money=None):
    if money == None:
      money = input("{}, how much money do you get? ".format(self.getName()))
    self.__pocketMoney = money

  def getPocketMoney(self):
    return self.__pocketMoney
