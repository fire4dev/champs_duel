# @@@@@ IMPORTS @@@@@@
from datetime import datetime
# @@ FOLDERS @@
from configs import bd
# here are the area os users (normal user and admin)
# some basic informations
status = ''
def sign_up(name,username,crypted_pass,user_type):
    global status
    bd.cursor.execute("SELECT username FROM users WHERE username=%s",(username,))
    # date today
    created_at = datetime.today()
    points = 0
    victories = 0
    row = bd.cursor.rowcount
    if row==0:
        bd.cursor.execute("INSERT INTO users(name, username, crypted_pass, points, victories, user_type, created_at) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,username,crypted_pass,points,victories,user_type,created_at))
        bd.connection.commit()
        bd.cursor.execute("INSERT INTO users(name, username, crypted_pass, points, victories, user_type, created_at) VALUES(%s,%s,%s,%s,%s,%s,%s)",(name,username,crypted_pass,points,victories,user_type,created_at))
        bd.connection.commit()
        status = 'created'
    else:
        status = 'not_created'
        
def login(username,not_crypted_pass):
    global status, user_type
    bd.cursor.execute("SELECT username,crypted_pass FROM users WHERE username=%s and crypted_pass=%s",(username,not_crypted_pass))
    row = bd.cursor.rowcount
    if row > 0:
        status = 'logged'
        bd.cursor.execute("SELECT user_type FROM users WHERE username=%s",(username,))
        user_type = bd.cursor.fetchone()[0]
    else:
        status = 'not logged'
        
def users():
    global status
    bd.cursor.execute("SELECT id,name,username,user_type FROM users")
    user_list = bd.cursor.fetchall()
    return user_list
        
    
