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

    def aktualizuj_stan_magazynu(id_pracownika):
        print("Aktualizuj stan magazynu:")

    def dodaj_do_listy_zakupow(id_pracownika):
        print("Dodawanie do listy zakupów:")




class Administrator(Pracownik):
    def _init_(self, id_pracownika):
        super()._init_(id_pracownika)

    def nadzor_nad_lista_zakupow(self):
        print("Zarządzanie lista zakupów")

    def aktualizuj_dane_pracownika(self):
        print("Zmień dane pracownika")
        query = "SELECT * FROM pracownicy"
        cursor.execute(query)
        for (id) in cursor:
            print("{}".format(id));

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

            else:
                odpowiedz_bazy=1


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
                    wybieranie2(id_pracownika)
                else:
                    global adm
                    adm = Administrator(id_pracownika)
                    wybieranie2(id_pracownika)

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

def wybieranie2(id_pracownika):
      #sprawdzenie czy osoba pod danym ID ma uprawnienia admina
    query = "SELECT admin FROM pracownicy WHERE id_pracownika = {}".format(id_pracownika)
    cursor.execute(query)
    uprawnienia = cursor.fetchall()
    for uprawnienie in uprawnienia:
        admin=uprawnienie[0]

        #Przywitanie po zalogowaniu
    query = "SELECT imie,nazwisko FROM pracownicy WHERE id_pracownika = {}".format(id_pracownika)
    cursor.execute(query)
    dane = cursor.fetchall()
    for (imie, nazwisko) in dane:
        print("WITAJ "+imie+" "+nazwisko)
        print(
            "1.Wyświetl informacje o sobie\n2.Zarezerwuj laboratorium"
            "\n3.Aktualizuj stan magazynu\n4.Dodaj do listy zakupów\n5.Przejdz do magazynu")
        if(admin==1):
            print("###### FUNKCJE ADMINA ######\n6.Zatwierdz zakupy\n7.Aktualizuj dane pracownika"
                  "\n8.Wyswietl wydatki\n9.Aktualizuj dane odbiorcow")
        wybor=input("Wybór(wiekszosc wyrzuci blad narazie, 5 bezpieczna jak cos")
        if (wybor == '1'):
            if(admin==1):
                adm.wyswietl_info_o_sobie(id_pracownika)
            else:
                worker.wyswietl_info_o_sobie(id_pracownika)
        elif (wybor == '2'):
            if (admin == 1):
                adm.rezerwuj_termin(id_pracownika)
            else:
                worker.rezerwuj_termin(id_pracownika)

        elif (wybor == '3'):
            if (admin == 1):
                adm.aktualizuj_stan_magazynu(id_pracownika)
            else:
                worker.aktualizuj_stan_magazynu(id_pracownika)
        elif (wybor == '4'):
            if (admin == 1):
                adm.dodaj_do_listy_zakupow(id_pracownika)
            else:
                worker.dodaj_do_listy_zakupow(id_pracownika)
        elif (wybor == '5'):
            przejdz_do_magazynu(admin)
        elif (wybor == '6'):
            adm.nadzor_nad_lista_zakupow()
        elif (wybor == '7'):
            adm.aktualizuj_dane_pracownika()
        elif (wybor == '8'):
            adm.wyswietl_wydatki()
        elif (wybor == '9'):
            adm.aktualizuj_dane_odbiorcow()

        else:
            print("Błąd! Wybierz jedną z dostępnych opcji!")
            wybieranie2(id_pracownika, admin)

def przejdz_do_magazynu(admin):
    print("##### MAGAZYN #####\n1.Wyswietl informacje chemiczne\n2.Wyswietl cene i stan"
          "\n3.Wyswietl dostepny sprzet\n4.Wyswietl dostepne zwiazki\n5.Powrot do menu")
    wybor=input("Wybor:")
    print("To już Tobie zostawiam ;)")

    if(wybor=='5'):
        try:
            wybieranie2(adm.id_pracownika)
        except:
            wybieranie2(worker.id_pracownika)

main()








