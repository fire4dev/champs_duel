# @@@@@ IMPORTS @@@@@@
from configs import bd

# here are the area os users (normal user and admin)
# some basic informations

def sign_up(name,username,crypted_pass,user_type):
    bd.cursor.execute("INSERT INTO users(name, username, crypted_pass, user_type) VALUES(%s,%s,%s,%s)",(name,username,crypted_pass,user_type))
# def login(username,crypted_pass):
    

# def user():
    
