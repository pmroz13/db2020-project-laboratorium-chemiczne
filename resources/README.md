# Laboratorium chemiczne

| Nazwisko i imię | Wydział | Kierunek | Semestr | Grupa | Rok akademicki |
| :-------------: | :-----: | :------: | :-----: | :---: | :------------: |
| Paulina Mróz    | WIMiIP  | IS       |   4     | 3     | 2019/2020      |
| Artur Hamerski  | WIMiIP  | IS       |   4     | 1     | 2019/2020      |

## Projekt bazy danych

![Schemat bazy](https://github.com/phajder-databases/db2020-project-laboratorium-chemiczne/blob/master/resources/labChemDB.svg)

## Zapytania 
Przykładowe zapytanie tworzące tabelę
```sql
CREATE TABLE IF NOT EXISTS zakupy( 
id_zakupu INT(20) AUTO_INCREMENT, 
id_sprzetu INT(20), 
id_zwiazku INT(20), 
data_zakupu DATE, 
ilosc INT(20), 
cena FLOAT(20), 
stan_zamowienia INT(20), 
PRIMARY KEY(id_zakupu), 
FOREIGN KEY (id_sprzetu) REFERENCES sprzet_lab(id_sprzetu), 
FOREIGN KEY (id_zwiazku) REFERENCES info_o_zwiazku(id_zwiazku) 
);
```

## Implementacja zapytań SQL
Poniżej przedstawiono przykłady zapytań użytych w projekcie.

Wybranie jednej instancji:
```sql
SELECT haslo FROM pracownicy 
WHERE pracownicy.id_pracownika ='{id_pracownika}';
```
Zmiana instancji:
```sql
UPDATE pracownicy SET haslo='{haslo}' 
WHERE id_pracownika='{id_pracownika}';
```
Zmiana instancji w oparciu o istniejące dane:
```sql
UPDATE sprzet_lab SET ilosc=CONCAT(ilosc-'{ilosc}') 
WHERE nazwa='{nazwa}';
UPDATE info_o_zwiazku SET uwagi = CONCAT(uwagi,'\n','{data}', '\n', '{uwaga}')
WHERE id_zwiazku = '{}';
```
Dodanie rekordu:
```sql
INSERT INTO zuzyte_zwiazki SET id_pracownika='{id_pracownika}',
id_zwiazku='{id_zwiazku}', data_zuzycia='{data}', ilosc_zuzycia='{ilosc}';
```
Uzyskanie id ostatnio dodanego rekordu:
```sql
SELECT id_zakupu FROM zakupy ORDER BY data_zakupu DESC LIMIT 1;
```
Użycie grupowania w celu wyświetlenia liczby dodanych zamównień w zależności od daty dodania:
```sql
SELECT zakupy.data_zakupu, zakupy.stan_zamowienia, 
COUNT(stan_zamowienia) FROM zakupy 
GROUP BY zakupy.data_zakupu DESC 
HAVING zakupy.stan_zamowienia=0;
```
Wybranie instancji po połączeniu tabel używając LEFT JOIN
```sql
SELECT id_zakupu, zakupy.id_zwiazku, zakupy.id_sprzetu, info_o_zwiazku.nazwa_zwiazku, 
sprzet_lab.nazwa, data_zakupu, zakupy.ilosc, cena 
FROM zakupy 
LEFT JOIN info_o_zwiazku USING (id_zwiazku)
LEFT JOIN sprzet_lab USING (id_sprzetu) 
WHERE zakupy.stan_zamowienia=0;
```
Wybranie instancji po połączeniu tabel używając INNER JOIN:
```sql
SELECT rezerwacje_lab.termin,pracownicy.imie, pracownicy.nazwisko 
FROM rezerwacje_lab 
INNER JOIN pracownicy ON rezerwacje_lab.id_pracownika = pracownicy.id_pracownika 
WHERE rezerwacje_lab.termin > CURRENT_TIME ORDER BY termin;
```

Usuwanie pojedynczego rekordu według id_zakupu:
```sql
DELETE FROM zakupy WHERE id_zakupu='{id_zakupu}';
```
Wybranie sumy pensji pracowników:
````sql
SELECT SUM(pensja) FROM pracownicy;
````
Wybieranie brakującego sprzętu laboratoryjnego w kolejności alfabetycznej:
```sql
SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku 
WHERE info_o_zwiazku.obecny_stan_w_magazynie=0 ORDER BY nazwa_zwiazku ASC;
```
Wybieranie związków chemicznych będących w magazynie w kolejności malejącej:
```sql
SELECT nazwa_zwiazku, obecny_stan_w_magazynie FROM info_o_zwiazku 
WHERE info_o_zwiazku.obecny_stan_w_magazynie>0 
ORDER BY obecny_stan_w_magazynie DESC;
```
Użycie podzapytań SQL:
```sql
SELECT id_wydatku, typ_wydatku, wydatki.cena, data, 
pracownicy.imie, pracownicy.nazwisko,
(SELECT nazwa_zwiazku FROM info_o_zwiazku WHERE id_zwiazku=zakupy.id_zwiazku),
(SELECT nazwa FROM sprzet_lab WHERE id_sprzetu=zakupy.id_sprzetu), 
zakupy.ilosc, odbior_odpadow.ilosc_zadeklarowanych_wiaderek FROM wydatki 
LEFT JOIN pracownicy USING (id_pracownika) 
LEFT JOIN zakupy USING (id_zakupu) 
LEFT JOIN odbior_odpadow USING (id_odbioru) ORDER BY {id_odbioru}
```
## Aplikacja
Do napisania aplikacji został wykorzystany język Python.
Aplikacja została napisana obiektowo.
W aplikacji wykorzystano 5 klas:
- Pracownik;
- Administrator- dziedziczy z klasy Pracownik;
- Zwiazek_Chemiczny;
- Magazyn;
- Konto.

Zimportowano następujące moduły w celu połaczenia z bazą danych:
```python
import mysql.connector
import pymysql
```