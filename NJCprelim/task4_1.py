import sqlite3

conn = sqlite3.connect('EntryDB.db')
file = open('Locations.csv')
for line in file:
  a,b,c,d = line.split(',')
  conn.execute('INSERT INTO Location(LocationID,Name,Address,URL)' + 'VALUES (?, ?, ?, ?)',(a,b,c,d))
  conn.commit()
conn.close()
file.close()
