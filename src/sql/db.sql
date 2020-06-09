-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 09 Cze 2020, 16:13
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.2.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `laboratorium`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `info_o_zwiazku`
--

CREATE TABLE `info_o_zwiazku` (
  `id_zwiazku` int(11) NOT NULL,
  `wzor` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `nazwa_zwiazku` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `stan_skupienia` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `uwagi` varchar(300) COLLATE utf8_polish_ci DEFAULT NULL,
  `cena_za_gram` float DEFAULT NULL,
  `obecny_stan_w_magazynie` float DEFAULT NULL,
  `pH` int(5) DEFAULT NULL,
  `rodzaj_wiazania_w_zwiazku` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `temp_wrzenia` float DEFAULT NULL,
  `temp_topnienia` float DEFAULT NULL,
  `masa_molowa` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Zrzut danych tabeli `info_o_zwiazku`
--

INSERT INTO `info_o_zwiazku` (`id_zwiazku`, `wzor`, `nazwa_zwiazku`, `stan_skupienia`, `uwagi`, `cena_za_gram`, `obecny_stan_w_magazynie`, `pH`, `rodzaj_wiazania_w_zwiazku`, `temp_wrzenia`, `temp_topnienia`, `masa_molowa`) VALUES
(1, 'H2O', 'woda', 'ciecz', 'taka fajna woda', 2, 100, 0, 'jakies napewno', 100, 30, 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `odbiorcy_odpadow_chemicznych`
--

CREATE TABLE `odbiorcy_odpadow_chemicznych` (
  `nazwa_firmy` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `data_odbioru` date DEFAULT NULL,
  `cena_za_wiaderko` float DEFAULT NULL,
  `ilosc_odebranych_wiaderek` int(20) DEFAULT NULL,
  `id_odbioru` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownicy`
--

CREATE TABLE `pracownicy` (
  `id_pracownika` int(11) NOT NULL,
  `imie` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `nazwisko` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `numer_konta` bigint(20) NOT NULL,
  `pensja` int(11) NOT NULL,
  `adres` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `data_zatrudnienia` date NOT NULL,
  `godzina_rozpoczecia_pracy` tinyint(4) NOT NULL,
  `godzina_zakonczenia_pracy` tinyint(4) NOT NULL,
  `stanowisko` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `login` text COLLATE utf8mb4_polish_ci NOT NULL,
  `haslo` text CHARACTER SET utf32 COLLATE utf32_polish_ci NOT NULL,
  `email` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL,
  `admin` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `pracownicy`
--

INSERT INTO `pracownicy` (`id_pracownika`, `imie`, `nazwisko`, `numer_konta`, `pensja`, `adres`, `data_zatrudnienia`, `godzina_rozpoczecia_pracy`, `godzina_zakonczenia_pracy`, `stanowisko`, `login`, `haslo`, `email`, `admin`) VALUES
(1, 'karol', 'krol', 0, 0, '', '0000-00-00', 0, 0, '', '', '', '', 0),
(2, 'arrrtur', 'haaamerski', 0, 0, '', '0000-00-00', 0, 0, '', '', '', '', 0),
(3, 'imie', 'nazwiko', 41241241, 0, 'krakow', '0000-00-00', 0, 0, '', 'admin', 'admin', 'emejl', 1),
(4, 'a', 'a', 0, 0, 'a', '0000-00-00', 0, 0, '', 'a', 'a', 'a', 0),
(7, 'b', 'b', 4, 0, 'b', '0000-00-00', 0, 0, '', 'b', 'dada', 'b', 0),
(8, 'c', 'c', 0, 0, 'c', '0000-00-00', 0, 0, '', 'c', 'c', 'c', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `sprzet_lab`
--

CREATE TABLE `sprzet_lab` (
  `id_sprzetu` int(11) NOT NULL,
  `nazwa` varchar(20) COLLATE utf8_polish_ci DEFAULT NULL,
  `ilosc` int(20) DEFAULT NULL,
  `uwagi` varchar(300) COLLATE utf8_polish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zuzyte_zwiazki`
--

CREATE TABLE `zuzyte_zwiazki` (
  `id_pracownika` int(20) DEFAULT NULL,
  `id_zwiazku` int(20) DEFAULT NULL,
  `data_zuzycia` date DEFAULT NULL,
  `ilosc_zuzycia` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `info_o_zwiazku`
--
ALTER TABLE `info_o_zwiazku`
  ADD PRIMARY KEY (`id_zwiazku`);

--
-- Indeksy dla tabeli `odbiorcy_odpadow_chemicznych`
--
ALTER TABLE `odbiorcy_odpadow_chemicznych`
  ADD PRIMARY KEY (`id_odbioru`);

--
-- Indeksy dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  ADD PRIMARY KEY (`id_pracownika`);

--
-- Indeksy dla tabeli `sprzet_lab`
--
ALTER TABLE `sprzet_lab`
  ADD PRIMARY KEY (`id_sprzetu`);

--
-- Indeksy dla tabeli `zuzyte_zwiazki`
--
ALTER TABLE `zuzyte_zwiazki`
  ADD KEY `id_pracownika` (`id_pracownika`),
  ADD KEY `id_zwiazku` (`id_zwiazku`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `info_o_zwiazku`
--
ALTER TABLE `info_o_zwiazku`
  MODIFY `id_zwiazku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT dla tabeli `odbiorcy_odpadow_chemicznych`
--
ALTER TABLE `odbiorcy_odpadow_chemicznych`
  MODIFY `id_odbioru` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `sprzet_lab`
--
ALTER TABLE `sprzet_lab`
  MODIFY `id_sprzetu` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `zuzyte_zwiazki`
--
ALTER TABLE `zuzyte_zwiazki`
  ADD CONSTRAINT `zuzyte_zwiazki_ibfk_1` FOREIGN KEY (`id_pracownika`) REFERENCES `pracownicy` (`id_pracownika`),
  ADD CONSTRAINT `zuzyte_zwiazki_ibfk_2` FOREIGN KEY (`id_zwiazku`) REFERENCES `info_o_zwiazku` (`id_zwiazku`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
