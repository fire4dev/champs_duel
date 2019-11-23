from configs import bd


def list_tournament():
    bd.cursor.execute("SELECT * FROM tournament")
    lists = bd.cursor.fetchall[0]

    print(lists)

