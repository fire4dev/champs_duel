import getpass 
from models import users_model as Users
import hashlib
def login():
    username = input("\nUsuario =>  ")

    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    # encoding the password
    md5pass = hashlib.md5(str(not_crypted_pass).encode('utf-8'))
    crypted_pass = md5pass.hexdigest()
    Users.login(username,crypted_pass)
