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