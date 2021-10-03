import sqlite3

kioskf = open('KIOSK.txt', 'r')
bentof = open('BENTOBOX.txt', 'r')
conn = sqlite3.connect('bento_company.db')

# Insert kiosk info
kiosks = []
for line in kioskf:
  kiosk = line.strip().split(',')
  conn.execute('insert into kiosk(KioskID, Location, Rating) values (?, ?, ?)', kiosk)
  kiosks.append(kiosk)

# Insert bento info
bentos = []
for line in bentof:
  bento = line.strip().split(',')
  conn.execute('insert into bentobox(BentoName, ProductionCost, ContainEgg , ContainNut, ContainSeafood) values (?, ?, ?, ?, ?)', bento)
  bentos.append(bento)

kioskf.close()
bentof.close()

# Insert KioskBento info
for kiosk in kiosks:
  kioskID = kiosk[0]
  for bento in bentos:
    bento_name = bento[0]
    production_cost = bento[1]
    if kioskID == '1':
      conn.execute('insert into KioskBento(KioskID, BentoName, SellPrice) values (?, ?, ?)', (kioskID, bento_name, float(production_cost) + 2.6))
    elif kioskID == '2':
      conn.execute('insert into KioskBento(KioskID, BentoName, SellPrice) values (?, ?, ?)', (kioskID, bento_name, float(production_cost) + 2.9))
    elif kioskID == '3':
      conn.execute('insert into KioskBento(KioskID, BentoName, SellPrice) values (?, ?, ?)', (kioskID, bento_name, float(production_cost) + 2.4))
    elif kioskID == '4':
      conn.execute('insert into KioskBento(KioskID, BentoName, SellPrice) values (?, ?, ?)', (kioskID, bento_name, float(production_cost) + 3.1))

conn.commit()
conn.close()
