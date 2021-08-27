from flask import *

app = Flask(__name__, template_folder='task4')

@app.route('')
def checkin():

  return render_template('checkin.html')

if __name__ == '__main__':
  app.run()
