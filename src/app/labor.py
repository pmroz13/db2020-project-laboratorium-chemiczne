import os
import sys
#sys.path.insert(0,"C:\Users\Dell\AppData\Roaming\Python\Python37\site-packages")
import pymysql

class Pracownik():

    def __init__(self,id_pracownika):
        self.id_pracownika=id_pracownika

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
    def _init_(self,id_pracownika):
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
    def _init_(self,id_zwiazku):
        self.id_zwiazku=id_zwiazku
        self.__con = pymysql.connect('localhost', 'user', 'password', 'db.sql')
        self.__cursor = self.__con.cursor()

    def wyswietl_infrmacje_chemiczne(id_zwiazku):
        def wyswietlInformacjeChemiczne(self, id_zwiazku):
            connection = polaczenie()
            with connection.cursor() as cursor:
                sql = f"SELECT nazwa_zwaizku, stan_skupienia, rodzaj_wiazania_w_zwiazku, temp_wrzenia, temp_topnienia, masa_molowa, pH, uwagi FROM info_o_zwiazku WHERE info_o_zwiazku.id_zwiazku=id_zwiazku; "
                # self.__cursor.execute('SELECT nazwa_zwaizku, stan_skupienia, rodzaj_wiazania_w_zwiazku,'
                #                     ' temp_wrzenia, temp_topnienia, masa_molowa, pH, uwagi FROM info_o_zwiazku'
                #                     ' WHERE info_o_zwiazku.id_zwiazku=id_zwiazku')
                # zwiazek = self.__cursor.fetchall()
                cursor.execute(sql)
                result = cursor.fetchall()
            print('Nazwa zwiazku: {}')
            print('Stan skupienia: {}')
            print('Rodzaj wiazania w zwiazku: {}')
            print('Temperatura wrzenia: {}')
            print('Temperatura topnienia: {}')
            print('Masa molowa: {}')
            print('pH: {}')
            print('Uwagi: {}')

    def wyswietlCeneIStan(self, id_zwiazku):
        self.__cursor.execute('SELECT cena_za_gram, obecny_stan_w_magazynie FROM info_o_zwiazku WHERE info_o_zwiazku.id_zwiazku=id_zwiazku ')
        cena = self.__cursor.fetchall()
        print('Cena za gram: {}')
        print('Obecna ilosc w magazynie: {}')


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
        print("Tutaj łączymy się z bazą danych a ona nam zwraca albo błąd, "
              "albo ID tej osoby.")
        odpowiedz_bazy = input("Wybierz 1 jesli chcesz BŁĄD lub Wybierz 2 "
              "jeśli chesz poprawne zalogowanie, 3 poprawne zalogowanie admina: ")
        if(odpowiedz_bazy=='1'):
            print("Błędny login lub hasło. Jeśli nie pamiętasz hasła wybierz 1,"
                  "Jeśli chcesz spróbować ponownie wybierz 2")
            wybor = input("Twoj wybor: ")
            if(wybor=='1'):
                account.resetuj_haslo()
            elif(wybor=='2'):
                account.zaloguj()
        elif (odpowiedz_bazy == '2'):
            print("Po poprawnym zalogowaniu na zwyklego uzytkownika"
                  "następuje pobranie jego ID i utworzenie obiektu klasy pracownik"
                  "o tym ID")
            worker=Pracownik(3)
           # worker.id_pracownika=4
        elif (odpowiedz_bazy == '3'):
            print("Po poprawnym zalogowaniu na admina"
                  "następuje pobranie jego ID i utworzenie obiektu "
                  "klasy administrator o tym ID")
            adm=Administrator()
            adm.id_pracownika=6
        else:
            return 0




    def zarejestruj(self):
        print("*****Rejestracja*****")

        login = input("Login: ")
        email = input("email: ")
        haslo = input("Hasło: ")
        haslo2 = input("Powtorz haslo:")
        print("Tu następuje sprawdzenie czy hasla sie zgadzaja, oraz czy mail"
              "oraz nick nie są już zajęte, jeśli nie przechodzimy do nastepnej"
              "części rejestracji")

        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        adres = input("Adres(Kod pocztowy, Miejscowość, Ulica, nr mieszkania): ")
        numer_konta= input("Numer konta bankowego: ")

        print("Teraz dodajemy konto do bazy danych")



    def resetuj_haslo(self):
        print("******Resetowanie hasła******")
        login = input("Login: ")
        email = input("email: ")
        print("Bza danych sprawdza czy taki login i hasło są w bazie,")
        odpowiedz_bazy = input("Wybierz 1 jesli chcesz BŁĄD lub Wybierz 2 "
                               "jeśli chesz zgodę na zmianę hasła")


#/////////////////////Funkcje/////////////////
def main():
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




main()
