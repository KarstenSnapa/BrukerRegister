import pymysql.cursors

connection = pymysql.connect(host='172.20.128.79',
                            user='karsten',
                            password='123Akademiet',
                            database='BrukerRegister',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

bruker_login = ''
passord_login = ''
forsøk_passord = 10

def les_bruker(bruker_login):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Liste WHERE Navn = %s", (bruker_login))
        navn_liste = cursor.fetchone()
    if navn_liste and bruker_login in navn_liste['Navn']:
        print("bruker finnes")
        print("Skriv passord")
        passord_login = input()
        les_passord(passord_login)
    else:
        print("bruker ikke tilgjengelig")
        les_bruker(bruker_login)


def les_passord(passord_login):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Liste WHERE Passord = %s", (passord_login))
        passord_liste = cursor.fetchone()
    if passord_liste and passord_login in passord_liste['Passord']:
        print("du er logget inn!")
    else:
        print("feil passord")
        print(forsøk_passord, "forsøk igjen på riktig passord")
        forsøk_passord -= 1
        if forsøk_passord > 0:
            les_passord()
        else:
            print("Du er tom for forsøk!")


def login():
    forsøk_passord = 10
    print("logg inn med epost eller navn:")
    bruker_login = input()
    les_bruker(bruker_login)


login()
