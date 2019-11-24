#@@@ IMPORTS @@@
from configs import bd
from datetime import datetime
import time
from views import design_view
def create_tournament():
    data = datetime.today()

    name_tournament = input('Nome do torneio => ')
    type_tournament = input('Diga o tipo de torneio que deseja criar => ')
    category_tournament = input('Categoria do torneio => ')
    description = input('Descrição do torneio => ')
    password_ = input('Irá ter senha? (s/n) ')
    
    if password_ == 's':
        password_tournment = input('Insira a senha do torneio => ')
    
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,crypted_password,type_tournament,description,created_at)
        values (%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, password_tournment, type_tournament, description, data))
        bd.connection.commit()

        print('Torneio registrado.')
        time.sleep(1)
        design_view.clear()
        design_view.designMenuADM()
    else:
    
        bd.cursor.execute("""
        INSER INTO tournament(name,category,type_tournament,description,created_at)
        values (%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, type_tournament, description, data))
        bd.connection.commit()

        print('Torneio registrado.')
        time.sleep(1)
        design_view.clear()
        design_view.designMenuADM()
    
        




