#@@@ IMPORTS @@@
from configs import bd
from datetime import datetime
import time
from views import design_view
def create_tournament(name_tournament,type_tournament,category_tournament,description,password_):
    global status
    from views import login_view
    data = datetime.today()
    
    if password_ == 's':
        username = login_view.username
        password_tournment = input('Insira a senha do torneio => ')
        bd.cursor.execute("SELECT id FROM users WHERE username = %s",(username,))
        user_id = bd.cursor.fetchone()[0]
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,created_by_id,crypted_password,type_tournament,description,created_at)
        values (%s,%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, user_id, password_tournment, type_tournament, description, data))
        bd.connection.commit()
        status = 'registered'
    else:
    
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,created_by_id,type_tournament,description,created_at)
        values (%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, user_id, type_tournament, description, data))
        bd.connection.commit()
        status = 'registered'
    
        




