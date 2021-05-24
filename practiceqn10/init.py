with open('students.csv') as studentsFile:
  fileList = []
  for line in studentsFile:
    fileList.append(line.strip().split(','))


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
  return render_template('form.html')

@app.route('/process/')
def process():
  if 'gender' in request.args:
    value = request.args['gender']

    ans = [student for student in students if student[1] == value]

    return render_template('results.html', gender=value, rows=students)

if __name__ == '__main__':
  app.run()
