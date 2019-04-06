import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

result = c.execute('SELECT * FROM readings')
for val in result:
    print (val)
conn.close()
