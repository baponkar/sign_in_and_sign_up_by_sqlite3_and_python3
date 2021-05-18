'''
This script validate a former registered user with corresponding password.
Build Date : 17/05/2021
Builder Name : Bapon Kar
Github Page : https://github.com/baponkar
Last Update : 18/05/2021
'''




import sqlite3
import getpass
import hashlib
import re



def checkUser(username):
	errors = []
	
	if not len(username) >= 4:
		errors.append("Username length should be more than or equaltu to 4")
		
	return errors


def checkPass(passWord):
		
	errors = []
	
	if not any(x.isupper() for x in passWord):
		errors.append("Your password needs at least 1 Capital")
	if not any(x.islower() for x in passWord):
		errors.append("Your password needs at least 1 Lower")
	if not any(x.isdigit() for x in passWord):
		errors.append("Your Password needs at least 1 number")
	#Checking either password string have a special character or not
	string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	if string_check.search(passWord) == None:
		errors.append("Your password needds at least a special character")
	
	if not len(passWord) >= 8:
		errors.append("Yours Password length should be at least 8")
	return errors
		

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
#print(users_list)


while True:

    username = input("Enter your username : ")
    #making lowercase
    username = username.lower()
    uerrors = checkUser(username)
	

    if username in users_list:
        print("This username already present please pick a different username")
    
    elif len(uerrors) != 0:
    	print(uerrors)
    else:
        p = getpass.getpass()
        perrors = checkPass(p)
        
        if len(perrors) != 0:
        	for i in perrors:
        		print(i)
        else:
        	#generate hash for password
        	phash = hashlib.sha256(p.encode('utf-8')).hexdigest()
        	#put data
        	curs.execute('INSERT INTO users ( username, password) VALUES(?,? )',(str(username),str(phash)))
        	break


curs.close()
conn.commit()
conn.close()


