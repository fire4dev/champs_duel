# @@@@@ IMPORTS @@@@@@
import getpass 
import time
# @@ FOLDERS @@
from models import users_model as Users
from models import champs_admin_model
from views import design_view,users_view,friends_views
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
            design_view.clear()
            design_view.designLogged()
            command = input("\ninforme um comando [@comando] =>  ") 
            if command == '@amigos':
                friends_views.index()
            elif command == '@criartor':
                champs_admin_model.create_tournament()
            elif command == '@torneios':
                tournaments.list_tournament()
            elif command == '@users':
                design_view.clear()
                users_view.index()
                # go back validation
                command = input("\ninforme um comando [@comando] =>  ") 
                goBack(command)
                    
            elif command == '@sair':
                logged = 0
            else:
                print('\n comando inválido')
                time.sleep(2)
    elif Users.status == 'not logged':
        print("\n usuário ou senha inválidos :(")
        time.sleep(1)


def goBack(command):
    while command != '@voltar':
        print('\n comando inválido')
        time.sleep(2)
        command = input("\ninforme um comando [@comando] =>  ") 