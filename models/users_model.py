# @@@@@ IMPORTS @@@@@@
from configs import bd

# here are the area os users (normal user and admin)
# some basic informations
status = ''
def sign_up(name,username,crypted_pass,user_type):
    global status
    bd.cursor.execute("SELECT username FROM users WHERE username=%s",(username))
    row = bd.cursor.rowcount
    if row!=0:
        bd.cursor.execute("INSERT INTO users(name, username, crypted_pass, user_type) VALUES(%s,%s,%s,%s)",(name,username,crypted_pass,user_type))
        bd.connection.commit()
        status='created'
    else:
        status = 'not_created'
        
def login(username,not_crypted_pass):
    global status
    bd.cursor.execute("SELECT username,crypted_pass FROM users WHERE username=%s and crypted_pass=%s",(username,not_crypted_pass))
    row = bd.cursor.rowcount
    if row > 0:
        status = 'logged'
# def user():
    
