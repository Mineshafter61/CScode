import sqlite3;

connection = sqlite3.connect('D:\library.db');
connection.execute('drop table Book')
connection.execute('CREATE TABLE Book (ID INTEGER PRIMARY KEY, Title TEXT)')
connection.commit();
connection.execute('insert into Book (ID, Title) VALUES (1, "Rollback Book")')
connection.execute('insert into Book (ID, Title) VALUES (2, "Also Rollback Book")')
connection.rollback();
connection.execute('insert into Book (ID, Title) VALUES (3, "Committed Book")')

connection.commit(); connection.close();
