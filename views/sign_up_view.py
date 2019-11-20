from models import users_model as Users
def sign_up():
    name = input("Nome =>  ")
    username = input("Usuário =>  ")
    crypted_pass = input("Senha =>  ")
    user_type = 'normal'
    
    Users.sign_up(name,username,crypted_pass,user_type)
