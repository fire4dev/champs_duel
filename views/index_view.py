# @@@@@ IMPORTS @@@@@@
import random
import time
import sys
from datetime import datetime

# @@ FOLDERS @@
import login_view
import sign_up_view



# some def's
def clear():
    print("\n"*100)
def designMenu():
    print("¨"*20)
    print("Champs Duel")
    print("¨"*20)
    print("\n @entrar\n @cadastrar\n @campeonatos\n @sair")


# main application
# loop menu 
activeApp = 1
while activeApp == 1:
    designMenu()
    commands = input("\ninforme um comando [@comando] =>  ")
    if commands == '@entrar':
        # form area
        login_view.login()
    if commands == '@cadastrar':
        # form area
        sign_up_view.sign_up()
    if commands == '@admin':
        sign_up_view.sign_up_admin()
    if commands == '@sair':
        print("\n Bye bye!!")
        time.sleep(0.5)
        activeApp = 0
