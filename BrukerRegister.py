import pymysql.cursors

connection = pymysql.connect(host='172.20.128.79',
                            user='karsten',
                            password='123Akademiet',
                            database='BrukerRegister',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

adminer_navn = 'adminer'
adminer_passord = 'passord'
adminer_tilgang = 'admin'


def create_adminer(adminer_navn, adminer_passord, adminer_tilgang):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Liste (navn, passord, tilgang) VALUES (%s, %s, %s)", (adminer_navn, adminer_passord, adminer_tilgang))
    connection.commit()

create_adminer(adminer_navn, adminer_passord, adminer_tilgang)