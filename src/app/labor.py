import mysql.connector
from mysql.connector import errorcode
import time


class Pracownik():

    def __init__(self, id_pracownika):
        self.id_pracownika = id_pracownika

    def wyswietl_info_o_sobie(id_pracownika):
        print("Informacje:")

    def rezerwuj_termin(id_pracownika):
        print("Rezerwacja terminu:")

    def aktualizuj_stan_magazynu():
        print("Aktualizuj stan magazynu:")

    def dodaj_do_listy_zakupow():
        print("Dodawanie do listy zakupów:")

    def utworz_konto():
        print("Tworzenie konta:")


class Administrator(Pracownik):
    def _init_(self, id_pracownika):
        super()._init_(id_pracownika)

    def nadzor_nad_lista_zakupow():
        print("Zarządzanie lista zakupów")

    def aktualizuj_dane_pracownika():
        print("Zmień dane pracownika")

    def wyswietl_wydatki():
        print("Wydatki:")

    def aktualizuj_dane_odbiorcow():
        print("Aktualizowanie danych odbiorców:")


class Zwiazek_chemiczny():
    def _init_(self, id_zwiazku):
        self.id_zwiazku = id_zwiazku

    def wyswietl_infrmacje_chemiczne(id_zwiazku):
        print("Informacje chemiczne:")

    def wyswietl_cene_i_stan(id_zwiazku):
        print("Cena i stan:")


class Magazyn():

    def wyswietl_sprzet_lab():
        print("Dostepny sptrzet:")

    def wyswietl_dostepne_zwiazki():
        print("Dostepne zwiazki:")


class Konto():

    def zaloguj(account):
        print("*****Logowanie*****")
        nick = input("Wprowadź nick: ")
        haslo = input("Wprowadź hasło: ")

        query = "SELECT haslo FROM pracownicy WHERE login = '{}'".format(nick)
        cursor.execute(query)
        haselka=cursor.fetchall()
        odpowiedz_bazy=1
        for haselko in haselka:
            if haselko[0]==haslo:
                odpowiedz_bazy=2
                print('22222')
            else:
                odpowiedz_bazy=1
                print('11111')

        if (odpowiedz_bazy == 1):
            print("Błędny login lub hasło. Jeśli nie pamiętasz hasła wybierz 1,"
                  "Jeśli chcesz spróbować ponownie wybierz 2")
            wybor = input("Twoj wybor: ")
            if (wybor == '1'):
                account.resetuj_haslo()
            elif (wybor == '2'):
                account.zaloguj()
        elif (odpowiedz_bazy == 2):
            query = "SELECT id_pracownika,admin FROM pracownicy WHERE login = '{}'".format(nick)
            cursor.execute(query)
            dane = cursor.fetchall()
            for (id_pracownika,admin) in dane:
                if(admin==0):
                    global worker
                    worker=Pracownik(id_pracownika)
                    wybieranie2(id_pracownika,admin)
                else:
                    global adm
                    adm = Administrator(id_pracownika)
                    wybieranie2(id_pracownika, admin)

            return 0

    def zarejestruj(account):
        print("*****Rejestracja*****")

        login = input("Login: ")
        email = input("email: ")
        haslo = input("Hasło: ")
        haslo2 = input("Powtorz haslo:")

        query = "SELECT login FROM pracownicy WHERE login = '{}'".format(login)
        cursor.execute(query)
        nicki = cursor.fetchall()
        if nicki:
            print('Podany login jest juz zajety, wybierz inny')
            account.zarejestruj()


        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        adres = input("Adres(Kod pocztowy, Miejscowość, Ulica, nr mieszkania): ")
        numer_konta = input("Numer konta bankowego: ")

        print("Teraz dodajemy konto do bazy danych")
        query = "INSERT INTO pracownicy SET imie='{}', nazwisko='{}',adres='{}',numer_konta='{}',login='{}',haslo='{}',\
                email='{}'".format(imie,nazwisko,adres,numer_konta,login,haslo,email)
        cursor.execute(query)
        mydb.commit()
        print("Pomyślnie utworzono konto!!!")
        wybieranie1(account)



    def resetuj_haslo(account):
        print("******Resetowanie hasła******")
        email = input("Podaj email: ")

        query = "SELECT email FROM pracownicy WHERE email = '{}'".format(email)
        cursor.execute(query)
        emejle = cursor.fetchall()
        if emejle:
            print('Na adres '+email+' zostal wyslany KOD, ktory należy wpisać, aby zresetować hasło'
                  '(domyslny kod to 1234)')
            kod=input("Wprowadz kod:")
            if(kod=='1234'):
                nowehaslo=input("Wprowadz teraz nowe haslo do konta:")
                nowehaslo2=input("Powtórz hasło:")
                query = "UPDATE pracownicy SET haslo='{}' WHERE email='{}'".format(nowehaslo,email)
                cursor.execute(query)
                mydb.commit()
            else:
                print('BŁĘDNY KOD! Powrót do MENU')
                wybieranie1(account)


        else:
            print("Podanego adreu email nie ma w naszej bazie")
            wybieranie1(account)






# /////////////////////Funkcje/////////////////
def main():

    # odczyt
    global mydb
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="laboratorium")
    global cursor
    cursor = mydb.cursor()
    account = Konto()
    wybieranie1(account)





def wybieranie1(account):
    print("Witamy w laboratorium chemicznym\n1.Zaloguj"
          "\n2.Zarejestruj.\n3.Zapomniałem hasła."
          "\n4.Zamknij")
    wybor = input("Wprowadź wartość: ")
    if (wybor == '1'):
        account.zaloguj()
    elif (wybor == '2'):
        account.zarejestruj()
    elif (wybor == '3'):
        account.resetuj_haslo()
    elif (wybor == '4'):
        return 0
    else:
        print("Wybrano zla wartosc, WYBIERZ OPCJĘ OD 1 do 4:")
        wybieranie1()

def wybieranie2(id_pracownika, admin):
    query = "SELECT imie,nazwisko FROM pracownicy WHERE id_pracownika = {}".format(id_pracownika)
    cursor.execute(query)
    dane = cursor.fetchall()
    for (imie, nazwisko) in dane:
        print("WITAJ "+imie+" "+nazwisko+"!!!")






main()








