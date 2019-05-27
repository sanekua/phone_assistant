import re
import sqlite3 as lite


con = lite.connect('test.db')
def create_database():
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE Phone(Name TEXT)")
        cur.execute("INSERT INTO Phone VALUES('06$%^&*(72456845')")
        cur.execute("INSERT INTO Phone VALUES('0672178965')")
        cur.execute("INSERT INTO Phone VALUES(0982255468)")
        cur.execute("INSERT INTO Phone VALUES(067245888)")
        cur.execute("INSERT INTO Phone VALUES(06756845)")
        cur.execute("INSERT INTO Phone VALUES(067856845)")
        cur.execute("INSERT INTO Phone VALUES(0982456845)")
        cur.execute("INSERT INTO Phone VALUES(09832456845)")
        cur.execute("INSERT INTO Phone VALUES(0972456845)")
        cur.execute("INSERT INTO Phone VALUES(0992456845)")
        cur.execute("INSERT INTO Phone VALUES(099092456845)")
        cur.execute("INSERT INTO Phone VALUES(0902456845)")

def program(numbers):
    l = []
    k = 0
    n = input('Please, input beggining of the phone number : ')
    for i in numbers:
        if i.startswith(n) and re.match(r'((8|\+3)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}',i):
            l.append(i)
            k += 1
            if k == 10:
                break
    if len(l) == 0:
        return 'No such number in our database'
    else:
        return l



def main_part():
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Phone")
        l = []
        while True:
            row = cur.fetchone()
            if row == None:
                break
            l.append(row[0])
        print(program(l))


create_database()
main_part()

