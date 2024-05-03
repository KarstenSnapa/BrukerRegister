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
Admin = False

def les_bruker(bruker_login):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Liste WHERE Navn = %s", (bruker_login))
        navn_liste = cursor.fetchone()
    if navn_liste and bruker_login in navn_liste['Navn']:
        print("bruker finnes")
        les_passord()
    else:
        print("bruker ikke tilgjengelig")
        login()


def les_passord():
    global forsøk_passord, Admin
    print("Skriv passord")
    passord_login = input()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Liste WHERE Passord = %s", (passord_login))
        passord_liste = cursor.fetchone()
    if passord_liste and passord_login in passord_liste['Passord']:
        print("du er logget inn!")
        Admin = True
    else:
        Admin = False
        print("feil passord")
        print(forsøk_passord, "forsøk igjen på riktig passord")
        forsøk_passord -= 1
        if forsøk_passord != 0:
            les_passord()
        else:
            print("Du er tom for forsøk!")


def login():
    forsøk_passord = 10
    print("logg inn med epost eller navn:")
    bruker_login = input()
    les_bruker(bruker_login)

login()



terminal = ''
nybruker_epost = ''
nybruker_navn = ''
nybruker_passord = ''
nybruker_tilgang = ''


def lag_bruker(nybruker_epost, nybruker_navn, nybruker_passord, nybruker_tilgang):
    print("lager bruker")
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Liste (Epost, Navn, Passord, tilgang) VALUES (%s, %s, %s, %s)", (nybruker_epost, nybruker_navn, nybruker_passord, nybruker_tilgang))
        connection.commit()



while Admin == True:
    terminal = ''
    nybruker_epost = ''
    nybruker_navn = ''
    nybruker_passord = ''
    nybruker_tilgang = ''


    terminal = input()
    if terminal == 'CREATE USER':
        print("skriv inn epost")
        nybruker_epost = input()
        print("skriv inn navn")
        nybruker_navn = input()
        print("skriv inn passord")
        nybruker_passord = input()

        print("hvilken tilgang skal bruker ha? bruker/ansatt/admin")
        nybruker_tilgang = input().lower()
        print("nybruker tilgang er ", nybruker_tilgang)
        if nybruker_tilgang == 'bruker' or nybruker_tilgang == 'ansatt' or nybruker_tilgang == 'admin':
            lag_bruker(nybruker_epost, nybruker_navn, nybruker_passord, nybruker_tilgang)
        else:
            print("kunne ikke lage bruker")
            print("ingen tilgang med navn:", nybruker_tilgang)
            nybruker_tilgang = ''