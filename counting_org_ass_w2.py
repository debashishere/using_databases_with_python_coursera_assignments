import sqlite3

conn  = sqlite3.connect('ass_email.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From:') : continue
    pieces = line.split()
    email = pieces[1]
    email_pieces = email.split('@')
    emailname = email_pieces[0]
    organisation = email_pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org=?',(organisation,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(org, count) VALUES(?,1)''',(organisation,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(organisation,))
            
conn.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()

# git link :- https://github.com/AlexGascon/Using-Databases-with-Python---Coursera/blob/master/Unit%202%20-%20Basic%20SQL%20(Structured%20Query%20Language)/A.2.2.%20-%20Counting%20email.py    
        



 
