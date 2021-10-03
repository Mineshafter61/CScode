from flask import *
import sqlite3
import datetime

app = Flask(__name__, template_folder='task4')

@app.route('/<location_id>')
def ret_form(location_id):
  return render_template('checkin.html', LocationID='location_id')

@app.route("/check_in/<location_id>", methods=["POST"])
def check_in(location_id):
  try:
    con = sqlite3.connect('EntryDB.db')
    con.row_factory = sqlite3.Row
    today = datetime.datetime.now()
    date = today.strftime('%d/%m/%y')
    time = today.strftime('%H%M')
    NRIC = request.form['NRIC']
    name = request.form['Name']
    contact = request.form['Contact']
    con.execute('INSERT INTO Visitor (NRIC, LocationID, Name, Contact, Date, Time) VALUES (?, ?, ?, ?, ?, ?)', (NRIC, location_id, name, contact, date, time))
    con.commit()

  except sqlite3.Error as ex:
    print(ex)
  con.close()

if __name__ == '__main__':
  app.run()
