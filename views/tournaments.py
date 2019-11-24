from configs import bd
import sys

def designMenuNORMAL():
    print("\n@entrar\n")

def list_tournament():
    
    bd.cursor.execute("SELECT id,name,category FROM tournament")
    lists = bd.cursor.fetchall()
    print(sys.argv[0])
    cont = 0
    print("ID   NOME          CATEGORIA\n")
    for cont in lists:
        
        print(f'{cont[0]}    {cont[1]}    \u200b{cont[2]}')

    find = input('Busque um campeonato pelo nome => ')

    bd.cursor.execute("SELECT name,id,category FROM tournament where name ilike %s", (find,))
    search = bd.cursor.rowcount
   
    if search > 0:
        designMenuNORMAL()
        enter_tournament = input('informe um comando [@comando] => ')
        if enter_tournament == '@entrar 1':
            print('idjwyhw')
    else:
        print('dont exist')

        

