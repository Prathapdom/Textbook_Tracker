import sqlite3
conn = sqlite3.connect('textbook_tracker.db')
#conn.execute('''CREATE TABLE COMPANY(Alphabet INT PRIMARY KEY NOT NULL,Book TEXT NOT NULL);''')
#print('Table created successfully')
cursor = conn.execute('''SELECT * FROM COMPANY;''')
#conn.execute('''INSERT INTO COMPANY VALUES ('A','Aliens - Resistance 001 (2019) (digital) (F) (The Magicians-Empire).cbr');''')

for row in cursor:
   print('ID = ', row[0])
   print('NAME = ', row[1])

#conn.commit()
print('Operation done successfully');
conn.close()