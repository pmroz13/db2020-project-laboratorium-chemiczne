-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 09 Cze 2020, 12:33
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
(7, 'b', 'b', 4, 0, 'b', '0000-00-00', 0, 0, '', 'b', 'dada', 'b', 0);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  ADD PRIMARY KEY (`id_pracownika`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
