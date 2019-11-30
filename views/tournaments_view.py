# @@@@@ IMPORTS @@@@@@
import time
# @@ FOLDERS @@
from models import tournaments_model as Champs

def index():
    print("                    CRIAR TORNEIO\n")
    name_tournament = input('Nome do torneio => ')
    category_tournament = input('Categoria do torneio => ')
    description = input('Descrição do torneio => ')
    duration = input('Duração do torneio [3h=3horas/3d=3dias] => ')
    password_ = input('Irá ter senha? (s/n) ')

    Champs.create_tournament(name_tournament,category_tournament,description,duration,password_)

    if Champs.status == 'registered':
        print("\n Torneio criado!")
        time.sleep(3)
def list_tournament():
    bd.cursor.execute("SELECT * FROM tournament")
    lists = bd.cursor.fetchall[0]

    print(lists)

