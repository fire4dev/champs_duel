# @@@@@ IMPORTS @@@@@@
import getpass 
import time
# @@ FOLDERS @@
from models import friends_model as Friends
# from views import sign_up_view
from views import design_view

def index():
    print("                    SEUS AMIGOS\n")
    Friends.friends()
    if Friends.status == 'no_friends':
        print("  Voce ainda nao possui amigos :(")
    elif Friends.status == 'have_friends':
        print("  NAME          USERNAME       USER_TYPE")
        for friend in Friends.friends():
            print("  {}       {}          {}".format(friend[0][0],friend[0][1],friend[0][2]))
    print("\n @adicionar\n @solicitacoes\n @voltar")

    # go back validation
    command = input("\ninforme um comando [@comando] =>  ") 
    options_response(command)


def options_response(command):
    while command != '@voltar':
        if command == '@adicionar':
            design_view.clear()
            print("\n  Enviar solicitação")
            searched_username = input("\n username do usuario =>  ")
            Friends.add_friend(searched_username)
            if Friends.status == 'sended':
                print("\n  solicitação enviada com sucesso")
                time.sleep(3)
                break
            elif Friends.status == 'already_sended':
                print("\n  solicitação já enviada")
                time.sleep(3)
                break
            elif Friends.status == 'user_dont_exists':
                print("\n  não foi possível encontrar nenhum usuário com este username")
                time.sleep(3)
                break
        elif command == '@solicitacoes':
            design_view.clear()
            print("    Solicitações recebidas\n")
            Friends.show_solicitations()
            if Friends.status == 'no_solicitations':
                print("  Sem solicitações no momento")
                time.sleep(4)
                break
            elif Friends.status == 'have_solicitations':
                print("  NAME           USERNAME            USER_TYPE")
                for solicitation in Friends.show_solicitations():
                    print("  {}       {}               {}".format(solicitation[0][0],solicitation[0][1],solicitation[0][2]))
                friend_accept = input("\n username para aceitar =>  ")
                if friend_accept:
                    Friends.accept_solicitations(friend_accept)
                    if Friends.status == 'accepted':
                        print("\n  Solicitação aceita\n Agora, {} é seu mais novo amigo :)".format(friend_accept))
                        time.sleep(3)
                    elif Friends.status == 'user_dont_sended_solicitation':
                        print("\n  o usuário informado  não está pedindo solicitação de amizade")
                        time.sleep(3)
                    elif Friends.status == 'user_dont_exists':
                        print("\n  não foi possível encontrar nenhum usuário com este username")
                        time.sleep(3)
                else:
                    break
        else:
            print('\n comando inválido')
            time.sleep(2) 
            break
    