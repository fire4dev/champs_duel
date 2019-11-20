from models import users_model as Users
def login():
    username = input("Usuário =>  ")
    crypted_pass = input("Senha =>  ")
    
    # Users.login(username,crypted_pass)
