'''
This script register a new user with corresponding password.
Build Date : 17/05/2021
Builder Name : Bapon Kar
Github Page : https://github.com/baponkar
Last Update : 17/05/2021
'''



import sqlite3
import getpass
import hashlib

conn = sqlite3.connect('users_data.db')
curs = conn.cursor()
curs.execute('SELECT * FROM users')
rows = curs.fetchall()

users_list = []
pass_list = []
for i in rows:
    users_list.append(i[1])
    pass_list.append(i[2])

#print(users_list,pass_list)
#print(users_list.index('bittu'))
while True:
    username = input("Please enter your username : ")
    if username in users_list:
        n = users_list.index(username)
        testpass = pass_list[int(n)]
        p = getpass.getpass()
        phash = hashlib.sha256(p.encode('utf-8')).hexdigest()

        if str(phash) == str(testpass):
            print("\n")
            print("Welcome ", username,'!')
            print("Sign in processed successfully!")
            break
        else:
            print(testpass,',',p)
            print("You typed wrong password")
    else:
        print (username,"Sorry no username have registered with this username")

