import sqlite3
import getpass
import hashlib


conn = sqlite3.connect('users_data.db')
curs = conn.cursor()
curs.execute( '''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username varchar(255) NOT NULL,
        password varchar(255) NOT NULL)''')


#getting data from old database
curs.execute('SELECT * FROM users')
rows = curs.fetchall()

#Getting of old username
users_list = []
for i in rows:
    users_list.append(i[1])
print(users_list)


while True:

    username = input("Enter your username : ")

    if username in users_list:
        print("This username already present please pick a different username")
    else:
        p = getpass.getpass()
        #generate hash for password
        phash = hashlib.sha256(p.encode('utf-8')).hexdigest()
        #put data
        curs.execute('INSERT INTO users ( username, password) VALUES(?,? )',(str(username),str(phash)))
        break


curs.close()
conn.commit()
conn.close()


