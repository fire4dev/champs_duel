# @@@@@ IMPORTS @@@@@@
import sys
sys.path.insert(0, "..\..\Python34\Lib\site-packages")
import psycopg2


try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "post",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "champs_duel")

    cursor = connection.cursor()
    # create tables if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
                id serial primary key,
                name varchar(120) not null,
                username varchar(120) unique not null,
                crypted_pass varchar(300) not null,
                points integer not null,
                victories integer not null,
                user_type varchar(20) not null DEFAULT 'normal',
                created_at varchar(100) not null
        );
        CREATE TABLE IF NOT EXISTS tournament(
                id serial primary key,
                name varchar(120) not null,
                category varchar(120) not null,
                created_by_id integer REFERENCES users(id),
                participants varchar(300) not null,
                crypted_password varchar(50),
                type_tournament varchar(50) not null,
                description varchar(300) not null,
                created_at varchar(100) not null
        );
        CREATE TABLE IF NOT EXISTS users_activities(
                id serial primary key,
                user_id integer REFERENCES users(id),
                notice varchar(200) not null
        );

    ''')
    connection.commit()
    # Print PostgreSQL Connection properties
    print("\nINFO: ")
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL:", error)

