# @@@@@ IMPORTS @@@@@@
import getpass 
import time
# @@ FOLDERS @@
from models import users_model as Users
from models import champs_admin_model
from views import design_view,users_view
import hashlib

def login():
    username = input("\nUsuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    # encoding the password
    md5pass = hashlib.md5(str(not_crypted_pass).encode('utf-8'))
    crypted_pass = md5pass.hexdigest()
    design_view.clear()
    Users.login(username,crypted_pass)

    logged = 1
    if Users.status == 'logged':
        while logged==1:
            design_view.designLogged
            command = input("\ninforme um comando [@comando] =>  ") 
            if command == '@criar':
                champs_admin_model.create_tournament()
            elif command == '@torneios':
                tournaments.list_tournament()
            elif command == '@users':
                users_view.index
            elif command == '@sair':
                break
            else:
                print('\n comando inválido')
                time.sleep(2)
    elif Users.status == 'not logged':
        print("\n usuário ou senha inválidos :(")
        time.sleep(1)
