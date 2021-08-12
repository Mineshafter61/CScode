class Person:
    def __init__(self, full_name: str, date_of_birth: str):
        self.__full_name__ = full_name
        self.__date_of_birth__ = date_of_birth

    # using 'private' variables, so getter functions are required

    def get_full_name(self):
        return self.__full_name__

    def get_date_of_birth(self):
        return self.__date_of_birth__

    def is_adult(self):
        import datetime
        this_year = datetime.datetime.today().year
        dob_year, dob_month, dob_day = self.__date_of_birth__.split('-')
        return int(this_year) - int(dob_year) > 18

    def screen_name(self):
        month = str(self.__date_of_birth__[5:7])
        day = str(self.__date_of_birth__[8:10])
        finalname = ''.join([l for l in self.__full_name__ if l.isalpha()])
        return finalname+month+day

class Staff(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)

    def is_adult(self):
        return True

    def screen_name(self):
        return super().screen_name()[:-4]+"Staff"

class Student(Person):
    def __init__(self, full_name, date_of_birth):
        super().__init__(full_name, date_of_birth)

    def is_adult(self):
        return False

if __name__ == '__main__':

  with open('people.txt', 'r') as inf:
    person_list = []
    for line in inf:
        name, date_of_birth, person_type = line.strip().split(',')
        if person_type == 'Staff':
            person_class = Staff(name, date_of_birth)
            person_list.append(person_class)
        elif person_type == 'Person':
            person_class = Person(name, date_of_birth)
            person_list.append(person_class)
        elif person_type == 'Student':
            person_class = Student(name, date_of_birth)
            person_list.append(person_class)

  import sqlite3

  connection = sqlite3.connect('school.db')

  for i in range(len(person_list)):
    connection.execute('INSERT INTO People(FullName, DateOfBirth, ScreenName, IsAdult) VALUES (?, ?, ?, ?)',
                (person_list[i].get_full_name(), person_list[i].get_date_of_birth(), person_list[i].screen_name(), person_list[i].is_adult() ))
  connection.commit()
  connection.close()
