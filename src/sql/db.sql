create database DB;

CREATE TABLE IF NOT EXISTS info_o_zwiazku (
    id_zwiazku int AUTO_INCREMENT,
    PRIMARY KEY (id_zwiazku),
    wzor varchar(20),
    nazwa_zwiazku varchar(20),
    stan_skupienia varchar(20),
    uwagi varchar(300),
    cena_za_gram float(20),
    obecny_stan_w_magazynie float(20),
    pH int(5),
    rodzaj_wiazania_w_zwiazku varchar(20),
    temp_wrzenia float(20),
    temp_topnienia float(20),
    masa_molowa float(20)
);


CREATE TABLE IF NOT EXISTS sprzet_lab(
	id_sprzetu int AUTO_INCREMENT,
    PRIMARY KEY (id_sprzetu),
    nazwa varchar(20),
    ilosc int(20),
    uwagi varchar(300)
);


INSERT INTO info_o_zwiazku(wzor, nazwa_zwiazku, stan_skupienia, uwagi, cena_za_gram, obecny_stan_w_magazynie, pH, rodzaj_wiazania_w_zwiazku, temp_wrzenia, temp_topnienia, masa_molowa) VALUES('H2O','woda','ciecz','taka fajna woda', '2','100','0','jakies napewno','100','30','2');
INSERT INTO sprzet_lab(nazwa, ilosc, uwagi) VALUES ('probowka', '20', 'zadnych uwag');
