import mysql.connector
from mysql.connector import errorcode
import time
import pymysql
import datetime

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
                          "5.login\n6.haslo\n 7.email\n")
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
                        zmiana = input("Czy chcesz zmienic swoje haslo? T/N \n")
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
                temp = input("Podales zle haslo\n1. Sprobuj ponownie\n2. Wroc do glownego menu\n")
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
                           "1. Zwiazki chemiczne\n2. Sprzet laboratoryjny\n")
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
                nazwa = input("Wpisz nazwe sprzetu:\n")
                szt = input("Podaj ilosc sprzetu, ktora chcesz odjac:\n")
                query = "UPDATE sprzet_lab SET ilosc=CONCAT(ilosc-'{}')" \
                        " WHERE nazwa='{}'".format(szt, nazwa)
                cursor.execute(query)
                mydb.commit()

    def dodaj_do_listy_zakupow(self, id_pracownika):
        element = input("\nCo chcesz dodac do list zakupow?\n1. Zwiazek chemiczny\n2. Sprzet laboratoryjny\n")
        petla = True
        while(petla):
            data = datetime.datetime.now()
            if (element == '1'):
                id_zwiazku = IDzwiazku()
                ilosc = input("Podaj ilosc:\n")
                ilosc = int(ilosc)
                query = "SELECT cena_za_gram FROM info_o_zwiazku WHERE id_zwiazku='{}'".format(id_zwiazku)
                cursor.execute(query)
                cena = cursor.fetchall()
                for c in cena:
                    cena = int(c[0])
                query = "SELECT admin FROM pracownicy WHERE id_pracownika='{}'".format(id_pracownika)
                cursor.execute(query)
                admin = cursor.fetchall()
                for a in admin:
                    admin = int(a[0])
                cena = float(cena) * float(ilosc)
                query = "INSERT INTO zakupy SET id_zwiazku='{}',data_zakupu='{}', " \
                        "ilosc='{}', cena='{}', stan_zamowienia=0; ".format(id_zwiazku, data, ilosc, cena)
                cursor.execute(query)
                mydb.commit()
                if(admin):
                    query = "SELECT id_zakupu FROM zakupy ORDER BY data_zakupu DESC LIMIT 1 "
                    cursor.execute(query)
                    id = cursor.fetchall()
                    for ID in id:
                        id = ID[0]
                    query = "UPDATE zakupy SET stan_zamowienia=1 WHERE id_zakupu='{}'".format(id)
                    cursor.execute(query)
                    mydb.commit()
                    query = "INSERT INTO wydatki SET typ_wydatku='zwiazek', cena='{}', id_zakupu='{}'".format(cena, id)
                    cursor.execute(query)
                    mydb.commit()
                    print("Dodano")
                else:
                    print("Twoje zamowienie zostalo dodane do listy zakupow\nOczekuje na "
                          "zatwierdzenie przez administratora")
                petla = False
            elif (element == '2'):
                query = "SELECT nazwa FROM sprzet_lab"
                cursor.execute(query)
                sprzet = cursor.fetchall()
                for sl in sprzet:
                    print(sl[0])
                nazwa = input("Wpisz nazwe sprzetu:\n")
                query = "SELECT id_sprzetu FROM sprzet_lab WHERE nazwa='{}'".format(nazwa)
                cursor.execute(query)
                id_sprzetu = cursor.fetchall()
                for numer in id_sprzetu:
                    id_sprzetu = numer[0]
                ilosc = input("Podaj ilosc:\n")
                ilosc = int(ilosc)
                cena = int(input("Podaj cene za 1 szt\n"))
                query = "SELECT admin FROM pracownicy WHERE id_pracownika='{}'".format(id_pracownika)
                cursor.execute(query)
                admin = cursor.fetchall()
                for a in admin:
                    admin = int(a[0])
                cena = float(cena) * float(ilosc)
                query = "INSERT INTO zakupy SET id_sprzetu='{}',data_zakupu='{}', " \
                        "ilosc='{}', cena='{}', stan_zamowienia=0; ".format(id_sprzetu, data, ilosc, cena)
                cursor.execute(query)
                mydb.commit()
                if (admin):
                    query = "SELECT id_zakupu FROM zakupy ORDER BY data_zakupu DESC LIMIT 1 "
                    cursor.execute(query)
                    id = cursor.fetchall()
                    for ID in id:
                        id = ID[0]
                    query = "UPDATE zakupy SET stan_zamowienia=1 WHERE id_zakupu='{}'".format(id)
                    cursor.execute(query)
                    mydb.commit()
                    query = "INSERT INTO wydatki SET typ_wydatku='sprzet', cena='{}', id_zakupu='{}'".format(cena, id)
                    cursor.execute(query)
                    mydb.commit()
                    print("Dodano")
                else:
                    print("Twoje zamowienie zostalo dodane do listy zakupow\nOczekuje "
                          "zatwierdzenia przez administratora")
                petla = False
            else:
                print("Wybrano zla opcje")


class Administrator(Pracownik):
    def __init__(self, id_pracownika):
        super().__init__(id_pracownika)

    def nadzor_nad_lista_zakupow(self):
        print("\nZarządzanie lista zakupów\nDo zaakceptowaia czeka:")
        query = "SELECT zakupy.data_zakupu, zakupy.stan_zamowienia, COUNT(stan_zamowienia) " \
                "FROM zakupy GROUP BY zakupy.data_zakupu DESC HAVING zakupy.stan_zamowienia=0"
        cursor.execute(query)
        zam = cursor.fetchall()
        for z in zam:
            print("Data: ", z[0])
            print("Ilosc zamowien: ", z[2])
        print("-----")
        data = datetime.datetime.now()
        query = "SELECT id_zakupu, zakupy.id_zwiazku, zakupy.id_sprzetu, info_o_zwiazku.nazwa_zwiazku, " \
                "sprzet_lab.nazwa, data_zakupu, zakupy.ilosc, cena " \
                "FROM zakupy " \
                "LEFT JOIN info_o_zwiazku USING (id_zwiazku)" \
                "LEFT JOIN sprzet_lab USING (id_sprzetu) " \
                "WHERE zakupy.stan_zamowienia=0"
        cursor.execute(query)
        lista = cursor.fetchall()
        for numer in lista:
            print("-----")
            print("Nr: ", numer[0])
            if(numer[1]=='NULL'):
                print("Nazwa sprzetu: ", numer[4])
            if(numer[2]=='NULL'):
                print("Nazwa zwiazku: ", numer[3])
            print("Data zamowienia: ",numer[5])
            print("Zamowiona ilosc: ", numer[6])
            print("Cena: ", numer[7])
            cena = numer[7]
        calosc = input("Czy chcesz:\n1. Modyfikowac pojedynczo\n2. Modyfikowac calosc\n")
        if(calosc == '1'):
            petla = True
            while(petla):
                potwierdz = input("Podaj nr ktory chcesz modyfikowac\n")
                modyfikacja = input("Wybierz czy chcesz:\n1. Zatwierdzic\n2. Usunac\n")
                petla1 = True
                while(petla1):
                    if(modyfikacja == '1'):
                        query = "UPDATE zakupy SET stan_zamowienia=1 WHERE id_zakupu='{}'".format(potwierdz)
                        cursor.execute(query)
                        mydb.commit()

                        query = "SELECT id_zwiazku FROM zakupy " \
                                "WHERE id_zakupu='{}'".format(potwierdz)
                        cursor.execute(query)
                        lista = cursor.fetchall()
                        typW = "a"
                        for l in lista:
                            for ll in l:
                                typW = "sprzet"
                                if (ll != '0'):
                                    typW = "zwiazek"
                                query = "INSERT INTO wydatki SET wydatki.typ_wydatku='{}', cena='{}'," \
                                        " id_zakupu='{}', data='{}'".format(typW, cena, potwierdz, data)
                                cursor.execute(query)
                                mydb.commit()

                    elif(modyfikacja == '2'):
                        query = "DELETE FROM zakupy WHERE id_zakupu='{}'".format(potwierdz)
                        cursor.execute(query)
                        mydb.commit()
                        print("Zmodyfikowano")
                    dalej = input("czy chcesz dalej modyfikowac? T/N\n")
                    dalej = dalej.upper()
                    if(dalej == 'N'):
                        petla1 = False
                        petla = False
                    elif(dalej == 'T'):
                        petla1 = True
                        potwierdz = input("Podaj nr ktory chcesz modyfikowac\n")

        elif(calosc == '2'):
            modyfikacja = input("Wybierz czy chcesz:\n1. Zatwierdzic\n2. Usunac\n")
            if(modyfikacja == '1'):
                query = "UPDATE zakupy SET stan_zamowienia=1 WHERE stan_zamowienia=0"
                cursor.execute(query)
                mydb.commit()
                query = "SELECT id_zwiazku, id_sprzetu, zakupy.cena, zakupy.id_zakupu " \
                        "FROM zakupy WHERE stan_zamowienia=0"
                cursor.execute(query)
                lista = cursor.fetchall()
                typW = "a"
                for l in lista:
                    for ll in l:
                        typW = "sprzet"
                        if (ll != '0'):
                            typW = "zwiazek"
                        cena = l[2]
                        idZ = l[3]
                        print("CEna", cena)
                        query = "INSERT INTO wydatki SET wydatki.typ_wydatku='{}', cena='{}'," \
                                " id_zakupu='{}', data='{}'".format(typW, cena, idZ, data)
                        cursor.execute(query)
                        mydb.commit()
                print("Zmodyfikowano")

            elif(modyfikacja == '2'):
                query = "DELETE FROM zakupy WHERE stan_zamowienia=0"
                cursor.execute(query)
                mydb.commit()
                print("Zmodyfikowano")




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





    def wyswietl_wydatki(self):
        print("Wydatki:")
        query = "SELECT id_wydatku, typ_wydatku, wydatki.cena, data, " \
                    "pracownicy.imie, pracownicy.nazwisko, zakupy.ilosc, " \
                    "odbior_odpadow.ilosc_zadeklarowanych_wiaderek FROM wydatki " \
                    "LEFT JOIN pracownicy USING (id_pracownika) " \
                    "LEFT JOIN zakupy USING (id_zakupu) " \
                    "LEFT JOIN odbior_odpadow USING (id_odbioru)"
        cursor.execute(query)


    def zamow_odbior_wiaderek(self):
        print("\nZamawianie odbioru wiaderek")
        petla0 = True
        while(petla0):
            ilosc = input("Ile wiaderek chcesz zamowic?\n")
            petla = True
            if (ilosc > '0'):
                while (petla):
                    data = datetime.datetime.now()
                    cena = input("Podaj cene za wiaderko\n")
                    if (cena > '0'):
                        query = "INSERT INTO odbior_odpadow SET data_zgloszenia='{}',cena_za_wiaderko='{}', " \
                        "ilosc_zadeklarowanych_wiaderek='{}'".format(data, cena, ilosc)
                        cursor.execute(query)
                        mydb.commit()
                        query = "SELECT id_odbioru FROM odbior_odpadow ORDER BY data_zgloszenia DESC LIMIT 1 "
                        cursor.execute(query)
                        id = cursor.fetchall()
                        for ID in id:
                            id = ID[0]
                        petla = False
                        petla0 = False
                        cena = float(cena) * float(ilosc)
                        query = "INSERT INTO wydatki SET typ_wydatku='odpady', cena='{}', " \
                                "data='{}', id_odbioru='{}'".format(cena,data, id )
                        cursor.execute(query)
                        mydb.commit()

                    else:
                        print("Podaj cene wieksza od 0")
            else:
                print("Podaj prawidlowa ilosc wiaderek do odbioru")


def IDzwiazku():
    form = input("Wybierz format wyszukiwania zwiazku:\n1.Wzor zwiazku\n2.Nazwa zwiazku\n")
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
        query = "SELECT nazwa, ilosc, uwagi FROM sprzet_lab " \
                "WHERE ilosc >0 ORDER BY nazwa ASC;"
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
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku " \
                    "WHERE info_o_zwiazku.obecny_stan_w_magazynie>0 ORDER BY obecny_stan_w_magazynie DESC;"
        elif(dec == '2'):
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku " \
                    "WHERE info_o_zwiazku.obecny_stan_w_magazynie=0 ORDER BY nazwa_zwiazku ASC;"
        elif(dec == '3'):
            query = "SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku ORDER BY nazwa_zwiazku ASC;"
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
    wybor = input("Wprowadź wartość:\n")
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
            "1. Wyświetl informacje o sobie\n2. Zarezerwuj laboratorium"
            "\n3. Aktualizuj stan magazynu\n4. Dodaj do listy zakupów\n5. Przejdz do magazynu\n")
        if (admin == 1):
            print("###### FUNKCJE ADMINA ######\n6. Zatwierdz zakupy\n7. Aktualizuj dane pracownika"
                  "\n8. Wyswietl wydatki\n9. Aktualizuj dane odbiorcow\n10. Wyplac pensje\n11. Zatwierdz liste zakupow")
        wybor = input("Wybór\n")

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
            adm. zamow_odbior_wiaderek()
        elif (wybor == '10'):
            adm.wyplac_pensje()
        elif(wybor=='11'):
            adm.nadzor_nad_lista_zakupow()

        else:
            print("Błąd! Wybierz jedną z dostępnych opcji!")
            wybieranie2(id_pracownika)
            #wybieranie2(id_pracownika, admin)


def przejdz_do_magazynu(admin):
    print("\n##### MAGAZYN #####\n1. Wyswietl informacje chemiczne\n2. Wyswietl cene i stan"
          "\n3. Wyswietl dostepny sprzet\n4. Wyswietl dostepne zwiazki\n5. Powrot do menu\n")
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








