import mysql.connector
import datetime
from mysql.connector import errorcode
import time

class Pracownik():

    def __init__(self,id_pracownika):
        self.id_pracownika = id_pracownika

    def wyswietl_info_o_sobie(self, id_pracownika):
        query = "SELECT haslo FROM pracownicy WHERE pracownicy.id_pracownika ='%d';"%(id_pracownika)
        cursor.execute(query)
        hasloSQL = cursor.fetchall()
        for numer in hasloSQL:
            hasloSQL = numer[0]
        proba = 3
        while (proba):
            haslo = input("Podaj swoje haslo: ")
            if (haslo == hasloSQL):
                query = "SELECT imie, nazwisko, stanowisko, adres, pensja, numer_konta, data_zatrudnienia, " \
                        "godzina_rozpoczecia_pracy, godzina_zakonczenia_pracy, login, email, admin " \
                        "FROM pracownicy WHERE pracownicy.id_pracownika ='%d';" % (id_pracownika)
                cursor.execute(query)
                dane = cursor.fetchall()
                print("----------------------------")
                for dana in dane:
                    print("Imie: ", dana[0])
                    print("Nazwisko: ", dana[1])
                    print("Stanowisko: ", dana[2])
                    print("Adres: ", dana[3])
                    print("Pensja: ", dana[4], "zl")
                    print("Twoje konto bankowe: ", dana[5])
                    print("Data zatrudnienia: ", dana[6])
                    print("Godzina rozpoczecia pracy: ", dana[7])
                    print("Godzina zakonczenia pracy: ", dana[8])
                    print("Twoj login: ", dana[9])
                    print("Twoj e-mail: ", dana[10])
                    if (dana[11] == True):
                        print("Posiadasz uprawnienia administratora")
                    else:
                        print("Nie posiadasz uprawnien administratora")

                while True:
                    print("Wybierz co chcesz zmienić\n1.Imie\n2.Nazwisko\n3.Numer konta\n4.Adres\n"
                          "5.login\n6.haslo\n 7.email")
                    wybor2 = input("Wybór:")
                    if (wybor2 != '6'):
                        zmienna = input('Na jakaką wartość chcesz zmienić wybraną zmienną:')
                    if (wybor2 == '1'):
                        temp1 = 'imie'
                    elif (wybor2 == '2'):
                        temp1 = 'nazwisko'
                    elif (wybor2 == '3'):
                        temp1 = 'numer_konta'
                    elif (wybor2 == '4'):
                        temp1 = 'adres'
                    elif (wybor2 == '5'):
                        temp1 = 'login'
                    elif (wybor2 == '6'):
                        zmiana = input("Czy chcesz zmienic swoje haslo? T/N ")
                        zmiana = zmiana.upper()
                        if (zmiana == 'T'):
                            petla1 = True
                            while (petla1):
                                hasloStare = input("Podaj stare haslo:\n")
                                query = "SELECT haslo FROM pracownicy WHERE id_pracownika = '{}'".format(id_pracownika)
                                cursor.execute(query)
                                hasloSQL = cursor.fetchall()
                                for h in hasloSQL:
                                    hasloSQL = h[0]
                                if (hasloStare == hasloSQL):
                                    nowe1 = input("Podaj nowe haslo\n")
                                    nowe2 = input("Powtorz nowe haslo\n")
                                    petla = True
                                    while (petla):
                                        if (nowe1 == nowe2):
                                            query = "UPDATE pracownicy SET haslo='{}' WHERE id_pracownika='{}'".format(
                                                nowe1, id_pracownika)
                                            cursor.execute(query)
                                            mydb.commit()
                                            petla = False
                                        else:
                                            print("Podano dwa rozne hasla")
                                    petla1 = False
                                else:
                                    print("Podano nieprawidlowe haslo\n")
                                    menu = input("Kontynuujesz zmiane hasla\nChcesz wrocic do glownego menu? T/N\n")
                                    menu - menu.upper()
                                    if (menu == 'T'):
                                        petla1 = False

                    elif (wybor2 == '7'):
                        temp1 = 'email'
                    else:
                        wybieranie2(adm.id_pracownika)
                    if (wybor2 != '6'):
                        try:
                            query = "UPDATE pracownicy SET {}={} WHERE id_pracownika={}".format(temp1, zmienna,
                                                                                                id_pracownika)
                            cursor.execute(query)
                            mydb.commit()
                            print('Dokonano zmian!')
                        except:
                            query = "UPDATE pracownicy SET {}='{}' WHERE id_pracownika={}".format(temp1, zmienna,
                                                                                                  id_pracownika)
                            cursor.execute(query)
                            mydb.commit()
                            print('Dokonano zmian!')

                    wybor3 = input('1.Zmien inne wartości 2.Powrót do MENU:')
                    if (wybor3 == '1'):
                        print('')
                    else:
                        wybieranie2(id_pracownika)


            else:
                temp = input("Podales zle haslo\n1. Sprobuj ponownie\n2. Wroc do glownego menu")
                if (temp == '1'):
                    proba = proba - 1
                elif (temp == '2'):
                    proba = -1
        cursor.close()

    def rezerwuj_termin(self, id_pracownika):
        print("Rezerwacja terminu:")

    def aktualizuj_stan_magazynu(self, id_pracownika):
        petla0 = True
        while(petla0):
            rodzaj = input("\nAktualizujesz stan magazynu\nWybierz co chesz zaktualizowac\n"
                           "1. Zwiazki chemiczne\n2. Sprzet laboratoryjny ")
            if (rodzaj == '1'):
                petla1 = True
                while(petla1):
                    id_zwiazku = IDzwiazku()
                    data = datetime.datetime.now()
                    gramy = input("Podaj ile gramow zuzyles\n")
                    query = "INSERT INTO zuzyte_zwiazki SET id_pracownika='{}',id_zwiazku='{}', " \
                            "data_zuzycia='{}',ilosc_zuzycia='{}'".format(id_pracownika, id_zwiazku, data, gramy)
                    cursor.execute(query)
                    mydb.commit()

                    query = "UPDATE info_o_zwiazku SET obecny_stan_w_magazynie=CONCAT(obecny_stan_w_magazynie-'{}')" \
                            " WHERE id_zwiazku='{}'".format(gramy, id_zwiazku)
                    cursor.execute(query)
                    mydb.commit()
                    kolejny = input("Czy chcesz dodac kolejny zwiazek? T/N\n")
                    kolejny = kolejny.upper()
                    if( kolejny == 'N'):
                        petla1 = 0

            elif (rodzaj == '2'):
                query = "SELECT nazwa FROM sprzet_lab"
                cursor.execute(query)
                sprzet = cursor.fetchall()
                for sl in sprzet:
                    print(sl[0],"\n")
                nazwa = input("Wpisz nazwe sprzetu: ")
                szt = input("Podaj ilosc sprzetu, ktora chcesz odjac: ")
                query = "UPDATE sprzet_lab SET ilosc=CONCAT(ilosc-'{}')" \
                        " WHERE nazwa='{}'".format(szt, nazwa)
                cursor.execute(query)
                mydb.commit()

    def dodaj_do_listy_zakupow(self, id_pracownika):
        print("Dodawanie do listy zakupów:")


class Administrator(Pracownik):
    def _init_(self, id_pracownika):
        super()._init_(id_pracownika)

    def nadzor_nad_lista_zakupow(self):
        print("Zarządzanie lista zakupów")
    def wyplac_pensje(self):
        query = "SELECT SUM(pensja) FROM pracownicy"
        cursor.execute(query)
        pensja=cursor.fetchall()
        print("Czy chcesz wypłacić pensję wszystkim pracownikom? Koszt operacji to: {} zł".format(pensja))#JAK ZROBIĆ BEZ DECIMAL??????
        wybor=input("T/N?:")
        if(wybor.upper()=='T'):
            print("przenoszenie tego wszystkiego do tablicy wydatkow")
        else:
            wybieranie2(adm.id_pracownika)

    def aktualizuj_dane_pracownika(self):
        print("Zmień dane pracownika")
        query = "SELECT * FROM pracownicy"
        cursor.execute(query)
        print("Lista Pracowników:")
        for (id) in cursor:
            print("{}".format(id))
        szukana = input("Wyszukaj pracownika:")
        query = "SELECT * FROM pracownicy WHERE imie LIKE '{}' OR nazwisko LIKE '{}' OR stanowisko LIKE '{}' OR login LIKE '{}'".format(
            szukana, szukana, szukana, szukana)
        cursor.execute(query)
        for (id) in cursor:
            print("{}".format(id))

        wybor = input("Wprowadz ID pracownika, któremu chcesz zmienić dane lub zapłacić pieniądze, lub M jeśli chcesz wrócić do MENU:")
        if (wybor == 'M' or wybor == 'm'):
            wybieranie2(adm.id_pracownika)
        else:
            while True:
                print("Wybierz co chcesz zmienić\n1.Imie\n2.Nazwisko\n3.Numer konta\n4.Pensję\n5.Adres"
                      "\n6.Godzinę rozpoczęcia pracy\n7.Godzinę zakończenia pracy\n8.stanowisko\n9.login\n10.haslo"
                      "\n11.email\n12.Nadaj uprawnienia administratora\n13.Zapłać")
                wybor2 = input("Wybór:")
                if (wybor2 != '12' and wybor2 != '13'):
                    zmienna = input('Na jakaką wartość chcesz zmienić wybraną zmienną:')

                if (wybor2 == '1'):
                    temp1 = 'imie'
                elif (wybor2 == '2'):
                    temp1 = 'nazwisko'
                elif (wybor2 == '3'):
                    temp1 = 'numer_konta'
                elif (wybor2 == '4'):
                    temp1 = 'pensja'
                elif (wybor2 == '5'):
                    temp1 = 'adres'
                elif (wybor2 == '6'):
                    temp1 = 'godzina_rozpoczecia_pracy'
                elif (wybor2 == '7'):
                    temp1 = 'godzina_zakonczenia_pracy'
                elif (wybor2 == '8'):
                    temp1 = 'stanowisko'
                elif (wybor2 == '9'):
                    temp1 = 'login'
                elif (wybor2 == '10'):
                    temp1 = 'haslo'
                elif (wybor2 == '11'):
                    temp1 = 'email'
                elif (wybor2 == '12'):
                    query = "UPDATE pracownicy SET admin=1 WHERE id_pracownika={}".format(wybor)
                    cursor.execute(query)
                    mydb.commit()
                    print('Nadano uprawnienia administratora!')
                elif (wybor2 == '13'):
                    kwota=input("Wpisz kwotę, którą chcesz mu zapłacić:")
                    if(kwota!='0'):
                        print("dodawanie do historii wydatkow")

                else:
                    wybieranie2(adm.id_pracownika)
                if (wybor2 != '12' and wybor2 != '13'):
                    try:
                        query = "UPDATE pracownicy SET {}={} WHERE id_pracownika={}".format(temp1, zmienna, wybor)
                        cursor.execute(query)
                        mydb.commit()
                        print('Dokonano zmian!')
                    except:
                        query = "UPDATE pracownicy SET {}='{}' WHERE id_pracownika={}".format(temp1, zmienna, wybor)
                        cursor.execute(query)
                        mydb.commit()
                        print('Dokonano zmian!')

                wybor3 = input('1.Kontynuuj zarządzanie 2.Powrót do MENU:')
                if (wybor3 == '1'):
                    print('')
                else:
                    wybieranie2(adm.id_pracownika)





    def wyswietl_wydatki():
        print("Wydatki:")

    def aktualizuj_dane_odbiorcow():
        print("Aktualizowanie danych odbiorców:")


def IDzwiazku():
    form = input("Wybierz format wyszukiwania zwiazku:\n1.Wzor zwiazku\n2.Nazwa zwiazku")
    if (form == '1'):
        wzor = input("Wpisz wzor zwiazku: ")
        query = "SELECT id_zwiazku FROM info_o_zwiazku WHERE wzor='{}'".format(wzor)
    elif (form == '2'):
        nazwa_zwiazku = input("Wpisz nazwe zwiazku: ")
        query = "SELECT id_zwiazku FROM info_o_zwiazku WHERE nazwa_zwiazku='{}'".format(nazwa_zwiazku)
    cursor.execute(query)
    id_zwiazku = cursor.fetchall()
    for numer in id_zwiazku:
        id_zwiazku = numer[0]
    return id_zwiazku



class Zwiazek_chemiczny():
    def wyswietlInformacjeChemiczne(self):
        id_zwiazku = IDzwiazku()
        query = "SELECT nazwa_zwiazku, stan_skupienia, rodzaj_wiazania_w_zwiazku, temp_wrzenia, " \
                "temp_topnienia, masa_molowa, pH , uwagi FROM info_o_zwiazku " \
                "WHERE info_o_zwiazku.id_zwiazku='%d';"%(id_zwiazku)
        cursor.execute(query)
        zwiazek_chem = cursor.fetchall()
        print("----------------------------")
        for zwiazek in zwiazek_chem:
             print("Nazwa zwiazku: ", zwiazek[0])
             print("Stan skupienia: ", zwiazek[1])
             print("Rodzaj wiazania w zwiazku: ", zwiazek[2])
             print("Temperatura wrzenia: ", zwiazek[3])
             print("Temperatura topnienia:  ", zwiazek[4])
             print("Masa molowa: ", zwiazek[5])
             print("pH: ", zwiazek[6])
             print("Uwagi: ", zwiazek[7])

        uwaga = input("Czy chcesz dodac uwage? T/N")
        uwaga = uwaga.upper()
        if (uwaga == 'T'):
            now = datetime.datetime.now()
            uwagaZwiazku = input("Dodaj swoja uwage:\n")
            query = "UPDATE info_o_zwiazku SET uwagi = CONCAT(uwagi,'\n','{}', '\n', '{}') " \
                    "WHERE id_zwiazku = '{}';".format(now, uwagaZwiazku, id_zwiazku)
            cursor.execute(query)
            mydb.commit()
        cursor.close()

    def wyswietlCeneIStan(self):
        id_zwiazku = IDzwiazku()
        query = "SELECT nazwa_zwiazku, cena_za_gram, obecny_stan_w_magazynie " \
                "FROM info_o_zwiazku WHERE info_o_zwiazku.id_zwiazku='%d';" % (id_zwiazku)
        cursor.execute(query)
        zwiazek_chem = cursor.fetchall()
        print("----------------------------")
        for zwiazek in zwiazek_chem:
            print("Nazwa zwiazku: ", zwiazek[0])
            print("Cena za gram: ", zwiazek[1],"zl")
            print("Obecna ilosc w magazynie: ",zwiazek[2],"g")
        cursor.close()



class Magazyn():
    def wyswietl_sprzet_lab(self):
        query = "SELECT nazwa, ilosc, uwagi FROM sprzet_lab WHERE ilosc >0;"
        cursor.execute(query)
        sprzet_lab = cursor.fetchall()
        print("----------------------------")
        for sprzet in sprzet_lab:
            print("Nazwa sprzetu: ", sprzet[0])
            print("Obecna ilosc w magazynie: ", sprzet[1], " sztuk")
            print("Uwagi: ", sprzet[2])
            print("----")
        cursor.close()

    def wyswietl_dostepne_zwiazki(self):
        dec = input("Wybierz ktora opcje chceszy wyswietlic:\n1. Dostepne zwazki\n"
                    "2. Brakujace zwiazki\n3. Wszystkie zwiazki znajdujace sie w bazie ")
        if (dec == '1'):
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku WHERE info_o_zwiazku.obecny_stan_w_magazynie>0;"
        elif(dec == '2'):
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku WHERE info_o_zwiazku.obecny_stan_w_magazynie=0;"
        elif(dec == '3'):
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku;"
        else:
            print("Wybrales zla opcje\n")
            self.wyswietl_dostepne_zwiazki()

        cursor.execute(query)
        dostepne_zwiazki = cursor.fetchall()
        print("----------------------------")
        for zwiazek in dostepne_zwiazki:
            print("Nazwa sprzetu: ", zwiazek[0])
            print("Obecna ilosc w magazynie: ", zwiazek[1], " g")
            print("----")
        cursor.close()


class Konto():

    def zaloguj(account):
        print("*****Logowanie*****")
        nick = input("Wprowadź nick: ")
        haslo = input("Wprowadź hasło: ")

        query = "SELECT haslo FROM pracownicy WHERE login = '{}'".format(nick)
        cursor.execute(query)
        haselka = cursor.fetchall()
        odpowiedz_bazy = 1
        for haselko in haselka:
            if haselko[0] == haslo:
                odpowiedz_bazy = 2

            else:
                odpowiedz_bazy = 1

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
            for (id_pracownika, admin) in dane:
                if (admin == 0):
                    global worker
                    worker = Pracownik(id_pracownika)
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
                email='{}'".format(imie, nazwisko, adres, numer_konta, login, haslo, email)
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
            print('Na adres ' + email + ' zostal wyslany KOD, ktory należy wpisać, aby zresetować hasło'
                                        '(domyslny kod to 1234)')
            kod = input("Wprowadz kod:")
            if (kod == '1234'):
                nowehaslo = input("Wprowadz teraz nowe haslo do konta:")
                nowehaslo2 = input("Powtórz hasło:")
                query = "UPDATE pracownicy SET haslo='{}' WHERE email='{}'".format(nowehaslo, email)
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
    # sprawdzenie czy osoba pod danym ID ma uprawnienia admina
    query = "SELECT admin FROM pracownicy WHERE id_pracownika = {}".format(id_pracownika)
    cursor.execute(query)
    uprawnienia = cursor.fetchall()
    for uprawnienie in uprawnienia:
        admin = uprawnienie[0]

        # Przywitanie po zalogowaniu
    query = "SELECT imie,nazwisko FROM pracownicy WHERE id_pracownika = {}".format(id_pracownika)
    cursor.execute(query)
    dane = cursor.fetchall()
    for (imie, nazwisko) in dane:
        print("WITAJ " + imie + " " + nazwisko)
        print(
            "1.Wyświetl informacje o sobie\n2.Zarezerwuj laboratorium"
            "\n3.Aktualizuj stan magazynu\n4.Dodaj do listy zakupów\n5.Przejdz do magazynu")
        if (admin == 1):
            print("###### FUNKCJE ADMINA ######\n6.Zatwierdz zakupy\n7.Aktualizuj dane pracownika"
                  "\n8.Wyswietl wydatki\n9.Aktualizuj dane odbiorcow")
        wybor = input("Wybór(wiekszosc wyrzuci blad narazie, 5 bezpieczna jak cos")
        if (wybor == '1'):
            if (admin == 1):
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
        elif (wybor == '10'):
            adm.wyplac_pensje()

        else:
            print("Błąd! Wybierz jedną z dostępnych opcji!")
            wybieranie2(id_pracownika, admin)


def przejdz_do_magazynu(admin):
    print("\n##### MAGAZYN #####\n1.Wyswietl informacje chemiczne\n2.Wyswietl cene i stan"
          "\n3.Wyswietl dostepny sprzet\n4.Wyswietl dostepne zwiazki\n5.Powrot do menu\n")
    wybor = input("Wybor: ")
    magazyn = Magazyn()
    zwiazek = Zwiazek_chemiczny()
    if (wybor == '1'):
        zwiazek.wyswietlInformacjeChemiczne()
        przejdz_do_magazynu(admin)
    elif (wybor == '2'):
        zwiazek.wyswietlCeneIStan()
        przejdz_do_magazynu(admin)
    elif (wybor == '3'):
        magazyn.wyswietl_sprzet_lab()
        przejdz_do_magazynu(admin)
    elif (wybor == '4'):
        magazyn.wyswietl_dostepne_zwiazki()
        przejdz_do_magazynu(admin)
    elif(wybor=='5'):
        try:
            wybieranie2(adm.id_pracownika)
        except:
            wybieranie2(worker.id_pracownika)



if __name__ == "__main__":
    main()







