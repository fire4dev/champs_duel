# @@@@@ IMPORTS @@@@@@
import time
# @@ FOLDERS @@
from models import users_model as Users

def clear():
    print("\n"*100)
def designMenu():
    print("¨"*40)
    print()
    print("             Champs Duel")
    print()
    print("¨"*40)
    print("\n @entrar\n @cadastrar\n @torneios\n @sair")
def designLogged():
    print("¨"*40)
    print()
    print("             Champs Duel         Tipo de usuario => {}".format(Users.user_type.upper()))
    print()
    print("¨"*40)
    if Users.user_type == 'admin':
        print("\n @amigos\n @torneios\n @minhaconta\n @criartor\n @users\n @sair")
    elif Users.user_type == 'normal':
        print("\n @amigos\n @torneios\n @minhaconta\n @sair")    


