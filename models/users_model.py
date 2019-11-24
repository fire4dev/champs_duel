# @@@@@ IMPORTS @@@@@@
from configs import bd
import time
from views import sign_up_view,design_view,champs_adm, tournaments
# here are the area os users (normal user and admin)
# some basic informations
status = ''
def sign_up(name,username,crypted_pass,user_type):
    global status
    bd.cursor.execute("SELECT username FROM users WHERE username=%s",(username,))
    row = bd.cursor.rowcount
    if row==0:
        bd.cursor.execute("INSERT INTO users(name, username, crypted_pass, user_type) VALUES(%s,%s,%s,%s)",(name,username,crypted_pass,user_type))
        bd.connection.commit()
        status = 'created'
        print(status)
        time.sleep(2)
    else:
        status = 'not_created'
        print(status)
        time.sleep(2)
        
def login(username,not_crypted_pass):
    global status
    bd.cursor.execute("SELECT username,crypted_pass FROM users WHERE username=%s and crypted_pass=%s",(username,not_crypted_pass))
    row = bd.cursor.rowcount
    if row > 0:
        bd.cursor.execute(f"SELECT user_type FROM users WHERE username='{username}'")
        user_type = bd.cursor.fetchone()[0]

        if user_type == 'admin':
            
            logged = 1

            while logged == 1:
                design_view.clear()
                design_view.designMenuADM()
                command = input("\ninforme um comando [@comando] =>  ") 
                if command == '@criar':
                    champs_adm.create_tournament()
                if command == '@torneios':
                    tournaments.list_tournament()
                if command == '@sair':
                    print("\n Bye bye!!")
                    time.sleep(0.5)
                    logged = 0

        elif user_type == 'normal':
            design_view.designMenuNORMAL()
    else:
        status = 'not logged'
        print(status)
        time.sleep(5)
# def user():
    
