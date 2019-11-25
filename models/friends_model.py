# @@@@@ IMPORTS @@@@@@
from datetime import datetime
# @@ FOLDERS @@
from configs import bd

# here are the area os users (normal user and admin)
# some basic informations

status = ''

def friends():
    from views import login_view
    import time
    global status
    username = login_view.username
    # descovering the id of logged user
    bd.cursor.execute("SELECT id FROM users WHERE username=%s",(username,))
    user_id = bd.cursor.fetchone()[0]
    bd.cursor.execute("SELECT solicitation_to_id FROM users_friendships WHERE user_id=%s and solicitation_status = 'accepted'",(user_id,))
    row = bd.cursor.rowcount
    if row > 0:
        status = 'have_friends'
        solicitation_to_id = bd.cursor.fetchall()[0]
        ids_list = []
        print(solicitation_to_id)
        time.sleep(9999)
        for cont in range(row):
            the_list = "".join(map(str,solicitation_to_id[cont]))    
            or_statment = "{}".format(int(the_list))
            if cont+1==row:
                or_statment = int(the_list)
            bd.cursor.execute("SELECT name,username,user_type FROM users WHERE id=%s",(or_statment,))
            friend_list = bd.cursor.fetchall()
            ids_list.append(the_list)
            cont+=1
            print(the_list)
            print(ids_list)
        # time.sleep(9999)
        
        
        return friend_list

        #verificar o id logado primeiro
        #depois validar se o id logado é diferente do solicitation_to_id
    else:
        status = 'no_friends'
def add_friend(searched_username):
    from views import login_view
    global status
    created_at = datetime.today()
    # get the foreign key
    username = login_view.username
    bd.cursor.execute("SELECT id FROM users WHERE username=%s",(username,))
    user_id = bd.cursor.fetchone()[0]
    bd.cursor.execute("SELECT id FROM users WHERE username=%s",(searched_username,))
    row = bd.cursor.rowcount
    if row > 0:
        solicitation_to_id = bd.cursor.fetchone()[0]
        bd.cursor.execute("SELECT id FROM users_friendships WHERE user_id=%s and solicitation_to_id=%s",(user_id,solicitation_to_id))
        row = bd.cursor.rowcount
        if row == 0:
            solicitation_status = 'pending'
            bd.cursor.execute("INSERT INTO users_friendships(user_id, solicitation_to_id, solicitation_status, created_at) VALUES(%s,%s,%s,%s)",(user_id,solicitation_to_id,solicitation_status,created_at))
            bd.connection.commit()
            status = 'sended'
        else:
            status = 'already_sended'
    else:
        status = 'user_dont_exists'

def show_solicitations():
    global status
    from views import login_view

    username = login_view.username
    # discovering the id of the user who sent the solicitation
    bd.cursor.execute("SELECT id FROM users WHERE username=%s",(username,))
    user_id_logged = bd.cursor.fetchone()[0]
    bd.cursor.execute("SELECT user_id FROM users_friendships WHERE solicitation_to_id=%s and solicitation_status = 'pending'",(user_id_logged,))
    row = bd.cursor.rowcount
    if row > 0:
        status = 'have_solicitations'
        user_id = bd.cursor.fetchone()[0]
        bd.cursor.execute("SELECT user_id FROM users_friendships WHERE (user_id=%s and solicitation_to_id=%s) and solicitation_status = 'pending'",(user_id,user_id_logged))
        user_id_bd = bd.cursor.fetchone()[0]
        bd.cursor.execute("SELECT name, username, user_type FROM users WHERE id=%s",(user_id_bd,))
        soli_list = bd.cursor.fetchall()
        return soli_list
    else:
        status = 'no_solicitations'

def accept_solicitations(friend_accept):
    global status
    from views import login_view
    # friend_accept is the username of accepting friendship user
    bd.cursor.execute("SELECT id FROM users WHERE username=%s",(friend_accept,))
    row = bd.cursor.rowcount
    # the user especified exists
    if row > 0:
        user_id = bd.cursor.fetchone()[0]
        # know if the user especified are sending solicitation for logged user
        bd.cursor.execute("SELECT id FROM users_friendships WHERE user_id=%s",(user_id,))
        row = bd.cursor.rowcount
        if row > 0:
            solicitation_status = 'accepted'
            created_at = datetime.today()
            bd.cursor.execute("UPDATE users_friendships SET solicitation_status=%s WHERE user_id=%s",(solicitation_status,user_id))
            bd.connection.commit()

            username = login_view.username
            bd.cursor.execute("SELECT id FROM users WHERE username=%s",(username,))
            solicitation_to_id = bd.cursor.fetchone()[0]
            bd.cursor.execute("SELECT user_id FROM users_friendships WHERE solicitation_to_id=%s",(solicitation_to_id,))
            user_id = bd.cursor.fetchone()[0]
            bd.cursor.execute("INSERT INTO users_friendships(user_id, solicitation_to_id, solicitation_status, created_at) VALUES(%s,%s,%s,%s)",(solicitation_to_id,user_id,solicitation_status,created_at))
            bd.connection.commit()

            status = 'accepted'
        else:
            status = 'user_dont_sended_solicitation'
    else:
        status = 'user_dont_exists'
