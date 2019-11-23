# @@@@@ IMPORTS @@@@@@
import hashlib
import getpass 
import time
# @@ FOLDERS @@
from models import users_model as Users

def sign_up():
    name = input("\nNome =>  ")
    username = input("Usuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    # encoding the password
    md5pass = hashlib.md5(str(not_crypted_pass).encode('utf-8'))
    crypted_pass = md5pass.hexdigest()

    user_type = 'normal'
    Users.sign_up(name,username,crypted_pass,user_type)
    if Users.status == 'created':
        print("\n conta criada com sucesso :)")
        time.sleep(2)
    elif Users.status == 'not_created':
        print("\n nao foi possivel criar sua conta")
        time.sleep(2)
    
def sign_up_admin():
    name = input("\nNome =>  ")
    username = input("Usuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    # encoding the password
    md5pass = hashlib.md5(str(not_crypted_pass).encode('utf-8'))
    crypted_pass = md5pass.hexdigest()
    
    user_type = 'admin'
    Users.sign_up(name,username,crypted_pass,user_type)
    if Users.status == 'created':
        print("\n conta criada com sucesso :)")
        time.sleep(2)
    elif Users.status == 'not_created':
        print("\n nao foi possivel criar sua conta")
        time.sleep(2)