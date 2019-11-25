# @@@@@ IMPORTS @@@@@@
import getpass 
import time
# @@ FOLDERS @@
from models import users_model as Users

def index():
    print("                    USERS\n")
    print("  ID       NAME        USERNAME       USER_TYPE\n")
    for users in Users.users():
        id = users[0]
        name = users[1]
        username = users[2]
        user_type = users[3]
        print("  {}       {}       {}        {}".format(id,name,username,user_type))
    print("\n @voltar")
    # go back validation
    command = input("\ninforme um comando [@comando] =>  ") 
    while command != '@voltar':
        print('\n comando inválido')
        time.sleep(2)
        command = input("\ninforme um comando [@comando] =>  ") 

