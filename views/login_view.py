import getpass 
from champs_duel_lib.models import users_model as Users

def login():
    username = input("Usuario =>  ")
    not_crypted_pass = getpass.getpass(prompt='Senha =>  ', stream=None) 
    
    Users.login(username,crypted_pass,not_crypted_pass)
