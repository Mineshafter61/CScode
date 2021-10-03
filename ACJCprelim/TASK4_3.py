from flask import *
import sqlite3

app = Flask(__name__, template_folder="TASK4_3")

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':  # submitted form
    #print(request.form)
    # get location and allergies
    if 'location' not in request.form.keys():
      return render_template('index.html')  # form has not been submitted correctly
    # else
    location = request.form['location']  # location
    egg = 'egg' in request.form.keys()  # true if allergic
    nut = 'nut' in request.form.keys()  # true if allergic
    seafood = 'seafood' in request.form.keys()  # true if allergic

    # get the bento boxes from the database
    conn = sqlite3.connect('bento_company.db')  # connect to database
    # get the bento boxes the customer can consume
    bentos = conn.execute('select BentoName from bentobox where ContainEgg in (?, 0) and ContainNut in (?, 0) and ContainSeafood in (?, 0)', (int(not egg), int(not nut), int(not seafood) ))
    # get the location's ID
    kiosk = conn.execute('select KioskID from kiosk where Location = ?', (location,))
    for i in kiosk:
      kiosk = i[0]  # convert from cursor object to a str

    # get the prices
    bentoprices = []
    for bento in bentos:
      price = conn.execute('select SellPrice from KioskBento where KioskID = ? and BentoName = ?', (kiosk, bento[0]))
      for p in price:
        price = p[0]  # convert from cursor object to a str
      bentoprices.append((price, bento[0]))  # add to pricelist

    # displaying the results
    return render_template('result.html', location=location, bentoprices=bentoprices)

    conn.close()

  else:
    return render_template('index.html')  # form has not been submitted

if __name__ == '__main__':
  app.run()
