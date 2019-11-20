import getpass 
from models import users_model as Users

def login():
    username = input("\nUsuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    
    Users.login(username,not_crypted_pass)
