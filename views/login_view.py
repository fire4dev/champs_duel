# @@@@@ IMPORTS @@@@@@
import getpass 
import time
# @@ FOLDERS @@
from models import users_model as Users
from models import tournaments_model
from views import design_view,users_view,friends_views,tournaments_view
import hashlib

def login():
    global username
    username = input("\nUsuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    # encoding the password
    md5pass = hashlib.md5(str(not_crypted_pass).encode('utf-8'))
    crypted_pass = md5pass.hexdigest()
    design_view.clear()
    Users.login(username,crypted_pass)

    if Users.status == 'logged':
        logged = 1
        while logged==1:
            design_view.clear()
            design_view.designLogged()
            command = input("\ninforme um comando [@comando] =>  ") 
            if command == '@amigos':
                design_view.clear()
                friends_views.index()
            elif command == '@criartor':
                design_view.clear()
                tournaments_view.index()
            elif command == '@torneios':
                tournaments.list_tournament()
            elif command == '@users':
                design_view.clear()
                users_view.index()
            elif command == '@sair':
                logged = 0
            else:
                print('\n comando inválido')
                time.sleep(2)
    elif Users.status == 'not logged':
        print("\n usuário ou senha inválidos :(")
        time.sleep(1)

