from flask import Flask, render_template
from TASK4_2_Haruka_6969_6969 import Person, Staff, Student

app = Flask(__name__)

@app.route('/')
def index():
    with open('people.txt', 'r') as inf:
        person_list = []
        for line in inf:
            name, date_of_birth, person_type = line.strip().split(',')
            if person_type == 'Staff':
                person_class = Staff(name, date_of_birth)
                person_list.append((person_class.get_full_name(),
                                    person_class.screen_name(), "Staff"))
            elif person_type == 'Person':
                person_class = Person(name, date_of_birth)
                person_list.append((person_class.get_full_name(),
                                    person_class.screen_name(), "Person"))
            elif person_type == 'Student':
                person_class = Student(name, date_of_birth)
                person_list.append((person_class.get_full_name(),
                                    person_class.screen_name(), "Student"))

    return render_template('index.html', people=person_list)


if __name__ == '__main__':
    app.run()
