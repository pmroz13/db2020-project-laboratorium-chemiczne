-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Cze 2020, 22:37
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
  `obecny_stan_w_magazynie` int(11) DEFAULT NULL,
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
(1, 'H2O', 'woda', 'ciecz', 'taka fajna woda2020-06-11 18:25:24.745717uwaga2', 2, 90, 0, 'jakies napewno', 100, 30, 2),
(2, 'HCl', 'kwas solny', 'jakis', 'silnie zracy\n2020-06-11 18:28:03.561103\nuwaga2', 19.84, 3, 0, 'jakies inne niz woda', 84, -43, 36.9);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `odbior_odpadow`
--

CREATE TABLE `odbior_odpadow` (
  `data_zgloszenia` date DEFAULT NULL,
  `cena_za_wiaderko` float DEFAULT NULL,
  `ilosc_zadeklarowanych_wiaderek` int(5) DEFAULT NULL,
  `id_odbioru` int(10) NOT NULL
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
(8, 'qqq', 'qqq', 1111, 0, 'qqq', '0000-00-00', 0, 0, '', 'qqq', 'qqq', 'qqq', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rezerwacje_lab`
--

CREATE TABLE `rezerwacje_lab` (
  `id_pracownika` int(11) NOT NULL,
  `termin` date NOT NULL,
  `status` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

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

--
-- Zrzut danych tabeli `sprzet_lab`
--

INSERT INTO `sprzet_lab` (`id_sprzetu`, `nazwa`, `ilosc`, `uwagi`) VALUES
(1, 'pipeta', 17, 'uwaga do pipety'),
(2, 'probowka', 3, 'uwaga do probowki'),
(3, 'szkielko', 0, 'uwaga do szkielka');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `wydatki`
--

CREATE TABLE `wydatki` (
  `id_wydatku` int(11) NOT NULL,
  `typ_wydatku` text COLLATE utf8mb4_polish_ci NOT NULL,
  `cena` float NOT NULL,
  `data` date NOT NULL,
  `id_zakupu` int(11) NOT NULL,
  `id_pracownika` int(11) NOT NULL,
  `id_odbioru` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zakupy`
--

CREATE TABLE `zakupy` (
  `id_zakupu` int(11) NOT NULL,
  `id_zwiazku` int(11) NOT NULL,
  `id_sprzetu` int(11) NOT NULL,
  `data_zakupu` date NOT NULL,
  `ilosc` int(11) NOT NULL,
  `cena` float NOT NULL,
  `stan_zamowienia` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

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
-- Zrzut danych tabeli `zuzyte_zwiazki`
--

INSERT INTO `zuzyte_zwiazki` (`id_pracownika`, `id_zwiazku`, `data_zuzycia`, `ilosc_zuzycia`) VALUES
(4, 1, '2020-06-11', 3),
(4, 1, '2020-06-11', 3),
(4, 1, '2020-06-11', 2),
(4, 1, '2020-06-11', 2),
(4, 1, '2020-06-11', 3),
(4, 2, '2020-06-11', 2);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `info_o_zwiazku`
--
ALTER TABLE `info_o_zwiazku`
  ADD PRIMARY KEY (`id_zwiazku`);

--
-- Indeksy dla tabeli `odbior_odpadow`
--
ALTER TABLE `odbior_odpadow`
  ADD PRIMARY KEY (`id_odbioru`);

--
-- Indeksy dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  ADD PRIMARY KEY (`id_pracownika`);

--
-- Indeksy dla tabeli `rezerwacje_lab`
--
ALTER TABLE `rezerwacje_lab`
  ADD KEY `id_pracownika` (`id_pracownika`);

--
-- Indeksy dla tabeli `sprzet_lab`
--
ALTER TABLE `sprzet_lab`
  ADD PRIMARY KEY (`id_sprzetu`);

--
-- Indeksy dla tabeli `wydatki`
--
ALTER TABLE `wydatki`
  ADD PRIMARY KEY (`id_wydatku`),
  ADD KEY `id_zakupu` (`id_zakupu`),
  ADD KEY `id_pracownika` (`id_pracownika`),
  ADD KEY `id_odbioru` (`id_odbioru`);

--
-- Indeksy dla tabeli `zakupy`
--
ALTER TABLE `zakupy`
  ADD PRIMARY KEY (`id_zakupu`),
  ADD KEY `id_zwiazku` (`id_zwiazku`),
  ADD KEY `id_sprzetu` (`id_sprzetu`);

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
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT dla tabeli `sprzet_lab`
--
ALTER TABLE `sprzet_lab`
  MODIFY `id_sprzetu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT dla tabeli `wydatki`
--
ALTER TABLE `wydatki`
  MODIFY `id_wydatku` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT dla tabeli `zakupy`
--
ALTER TABLE `zakupy`
  MODIFY `id_zakupu` int(11) NOT NULL AUTO_INCREMENT;

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
