import sqlite3
import smtplib
import random
import struct
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


email = None#your reset password emailer
password = None#your email password


conn = sqlite3.connect('CopsAndRobbers.db')

c = conn.cursor()



def tableUsersCreate():
    try:
        c.execute('CREATE TABLE users (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, username CHAR NOT NULL UNIQUE, password TEXT NOT NULL, email TEXT NOT NULL UNIQUE, privilege INT NOT NULL, resetCode INT UNIQUE)')
        print('Table Users Created')
    except:
        print('Table Users Exists')

def dataEntryUsers(username, password, email, privilege):
    c.execute('INSERT INTO users (username, password, email, privilege) VALUES(?,?,?,?)',
              (username, password, email, privilege))
    print(str(username) + ' has been added')

    

#you can select all, ID, username, password, email, privilege from row
def getRowUsers(Id, column):
    if column != None:
        c.execute('SELECT * FROM users WHERE ID =?',[(Id)])
        row = c.fetchone()[column]
    else:
        row = c.fetchone()
    return row
    
def save():
    conn.commit()
#---------------------------------------------------------#
def changePasswordUsers(username):

    global email
    global password
    
    selectedRow = c.execute('SELECT email FROM users WHERE username=?',[(username)])
    email = str(c.fetchone()[0])
    resetCode = random.randint(23443, 67789)
    c.execute('UPDATE users SET resetCode=? WHERE username=?',[(resetCode),(username)])
    
    content = '\nTesting my automated reset password generator. Your reset code is ' + str(resetCode)

    print(email)
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)

    msg =  MIMEMultipart()
    msg['To'] = str(email)
    msg['Subject'] = "Reset Password"
    msg.attach(MIMEText(content))
    
    mail.sendmail(email,str(email),msg.as_string())
    mail.close()
#Not complete
#def checkResetCode(resetCode, username):
    #databaseResetCode = c.execute('SELECT resetCode FROM users WHERE username =?',(username))
    
def main():
    #'comment' means you have to enter this information
    
    tableUsersCreate()
    

    
    try:
        dataEntryUsers(#'name(char)', 'password(str)', email(str), 'server privilege(int)')

        save()
    except:
        print('User already exists')
    dictGetRow = {Id:0, username:1, password:2, email:3, privilege:4}        
    print(getRowUsers(2, None))

    print(getRowUsers(#'row id(int)',dictGetRow['column Wanted']))
main()
