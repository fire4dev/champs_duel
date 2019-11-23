# @@@@@ IMPORTS @@@@@@
import random
import time
import sys
from datetime import datetime
from models import users_model
# @@ FOLDERS @@
from views import login_view, sign_up_view, design_view,champs_adm

# main application
# loop menu 

global activeApp
activeApp = 1

while activeApp == 1:
   
    design_view.clear()
    design_view.designMenu()
    commands = input("\ninforme um comando [@comando] =>  ")
    if commands == '@entrar':
        # form area
        design_view.clear()
        login_view.login()
        
        
    if commands == '@cadastrar':
        # form area
        design_view.clear()
        sign_up_view.sign_up()
    if commands == '@admin':
        # form area
        design_view.clear()
        sign_up_view.sign_up_admin()
    if commands == '@sair':
        print("\n Bye bye!!")
        time.sleep(0.5)
        activeApp = 0


