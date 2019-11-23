# @@@@@ IMPORTS @@@@@@
import time
# @@ FOLDERS @@
from configs import bd

def clear():
    print("\n"*100)
def designMenu():
    print("¨"*40)
    print()
    print("             Champs Duel")
    print()
    print("¨"*40)
    print("\n @entrar\n @cadastrar\n @torneios\n @sair")
def designLogged(user_type):
    print("¨"*40)
    print()
    print("             Champs Duel         Tipo de usuario => {}".format(user_type.upper()))
    print()
    print("¨"*40)
    if user_type == 'admin':
        print("\n @criar (torneios)\n @torneios\n @users\n @sair")
    elif user_type == 'normal':
        print("\n @torneios\n @sair")    


