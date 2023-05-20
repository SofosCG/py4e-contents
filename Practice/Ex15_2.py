import sqlite3

conn = sqlite3.connect('Assignment.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
orgs = list()
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    org = line.split()[1].split('@')[1]
    orgs.append(org)

organizations = dict()
for org in orgs:
    organizations[org] = organizations.get(org, 0) + 1

for org, count in organizations.items():
    sqlstr = "INSERT INTO Counts (org, count) VALUES ('{}', {})".format(
        org, count)
    cur.execute(sqlstr)

conn.commit()
sqltbl = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqltbl):
    print(str(row[0]), row[1])

cur.close()
