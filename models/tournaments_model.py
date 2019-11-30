#@@@ IMPORTS @@@
from configs import bd
from datetime import datetime
import time
from views import design_view
def create_tournament(name_tournament,category_tournament,description,duration,password_):
    global status
    from views import login_view
    data = datetime.today()
    
    username = login_view.username
    bd.cursor.execute("SELECT id FROM users WHERE username = %s",(username,))
    user_id = bd.cursor.fetchone()[0]
    if password_ == 's':
        password_tournment = input('Insira a senha do torneio => ')
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,duration,created_by_id,crypted_password,description,created_at)
        values (%s,%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, duration, user_id, password_tournment, str(description), data))
        bd.connection.commit()
        status = 'registered'

    else:
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,duration,created_by_id,description,created_at)
        values (%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, duration, user_id, str(description), data))
        bd.connection.commit()
        status = 'registered'
    
        




