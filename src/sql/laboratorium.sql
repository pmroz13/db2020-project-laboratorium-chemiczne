-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 14 Cze 2020, 15:32
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
(1, 'H2O', 'woda', 'ciecz', 'taka fajna woda2020-06-11 18:25:24.745717uwaga2', 2, 78, 0, 'jakies napewno', 100, 30, 2),
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

--
-- Zrzut danych tabeli `odbior_odpadow`
--

INSERT INTO `odbior_odpadow` (`data_zgloszenia`, `cena_za_wiaderko`, `ilosc_zadeklarowanych_wiaderek`, `id_odbioru`) VALUES
('2019-10-04', 13, 8, 10),
('2019-11-04', 57, 4, 11),
('2020-05-05', 93, 3, 12),
('2020-05-26', 86, 5, 13),
('2020-03-27', 54, 3, 14),
('2020-03-20', 80, 2, 15),
('2019-08-24', 90, 7, 16),
('2019-09-03', 29, 7, 17),
('2019-07-28', 29, 4, 18),
('2020-01-14', 72, 2, 19);

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
(1, 'Nicole', 'Harris', 3255168848, 2023, 'Gjoçaj', '2020-04-01', 6, 14, 'Recruiter', 'nharris0', 'MYMYkgwCTs', 'nharris0@php.net', 0),
(2, 'Freeland', 'Arlow', 6287827440, 3035, 'San Esteban', '2019-10-22', 9, 18, 'Structural Engineer', 'farlow1', 'qHSPJnk4T', 'farlow1@japanpost.jp', 0),
(3, 'Adminek', 'Admiński', 41241241, 12345, 'Kraków', '2020-06-12', 11, 18, 'admin', 'admin', 'admin', 'Admin@agh.edu.pl', 1),
(11, 'Rolando', 'Balderson', 2289134457, 3630, 'Xirikxiy', '2020-04-29', 10, 14, 'Web Developer III', 'rbalderson0', '1yAW2bhfw6e', 'rbalderson0@time.com', 0),
(12, 'Yanaton', 'Castaner', 1171826001, 4473, 'Randuagung', '2019-07-19', 10, 15, 'Database Administrator IV', 'ycastaner1', 'lGCfbV', 'ycastaner1@google.pl', 0),
(13, 'Tilda', 'Pasby', 3988110809, 1524, 'Tipaz', '2019-12-07', 8, 15, 'Research Nurse', 'tpasby2', 'JpsxaeAREza3', 'tpasby2@meetup.com', 0),
(14, 'Con', 'Ravenshear', 6823264829, 2547, 'Liangshuijing', '2020-05-25', 6, 16, 'Research Associate', 'cravenshear3', 'czXM5X1', 'cravenshear3@moonfruit.com', 0),
(15, 'Rozanna', 'Netley', 5437160887, 4437, 'Filimonovo', '2020-02-02', 8, 16, 'Web Designer II', 'rnetley4', 'R9mhZ6unE', 'rnetley4@google.ru', 0),
(16, 'Tripp', 'Stockdale', 5937499018, 1381, 'Skała', '2020-01-23', 7, 18, 'Accounting Assistant IV', 'tstockdale5', 'o55amfpqY', 'tstockdale5@illinois.edu', 0),
(17, 'Faulkner', 'McGrowther', 7547511031, 3999, 'Tulihe', '2020-05-19', 10, 18, 'Programmer I', 'fmcgrowther6', 'JboEd5CR3HY', 'fmcgrowther6@freewebs.com', 0),
(18, 'Henka', 'Mounfield', 6046171814, 3061, '‘Arab ar Rashāydah', '2019-12-18', 10, 16, 'Biostatistician I', 'hmounfield7', 'J9BT2aSoUtb', 'hmounfield7@liveinternet.ru', 0),
(19, 'Kenna', 'Tointon', 4008305769, 549, 'Mambusao', '2019-09-17', 9, 16, 'Product Engineer', 'ktointon8', 'wV8Xy8L35i', 'ktointon8@sbwire.com', 0),
(20, 'Charlene', 'Diment', 2749688590, 4778, 'San Sebastián', '2020-03-02', 7, 15, 'Biostatistician I', 'cdiment9', '46r2VsogIK6r', 'cdiment9@friendfeed.com', 0),
(21, 'Othella', 'Duprey', 6802701103, 4402, 'Desa Baregbeg', '2019-09-05', 6, 17, 'Food Chemist', 'odupreya', 'clRq7rpxQQ', 'odupreya@com.com', 0),
(22, 'Karlens', 'Mosedale', 9737136160, 4473, 'Ijero-Ekiti', '2020-06-12', 8, 14, 'Staff Scientist', 'kmosedaleb', 'DTbB45eBieI', 'kmosedaleb@goodreads.com', 0),
(23, 'Saidee', 'Olivia', 2963300204, 113, 'Cocieri', '2020-01-18', 9, 16, 'Social Worker', 'soliviac', '31kEUw2', 'soliviac@wikia.com', 0),
(24, 'Ben', 'Logan', 4035573531, 2145, 'Fuqiang', '2020-04-30', 9, 17, 'Professor', 'blogand', '5368Xdd', 'blogand@simplemachines.org', 0),
(25, 'Rudiger', 'Keers', 7529773070, 1045, 'Punta Hermosa', '2020-02-24', 10, 16, 'Financial Analyst', 'rkeerse', 't10YJI18rx6', 'rkeerse@geocities.jp', 0),
(26, 'Sanderson', 'Currm', 2090219432, 4009, 'Fuvahmulah', '2019-12-01', 8, 15, 'Structural Analysis Engineer', 'scurrmf', 'PQifKbcYVqt', 'scurrmf@odnoklassniki.ru', 0),
(27, 'Matthew', 'Hallin', 3022869630, 1213, 'Trudobelikovskiy', '2020-03-02', 10, 17, 'VP Quality Control', 'mhalling', 'nPjQUA5fXi', 'mhalling@about.me', 0),
(28, 'Ainsley', 'Aries', 8572833455, 3198, 'Juancheng', '2020-05-21', 9, 17, 'Electrical Engineer', 'aariesh', 'rBu6582H', 'aariesh@imdb.com', 0),
(29, 'Gualterio', 'Skelding', 6408813089, 1228, 'Chamical', '2019-09-15', 10, 17, 'Compensation Analyst', 'gskeldingi', 'q9bg4yyU', 'gskeldingi@marketwatch.com', 0),
(30, 'Iain', 'Dougher', 2593680644, 1777, 'El Pino', '2019-09-29', 6, 17, 'Programmer III', 'idougherj', '241W4JWufLia', 'idougherj@smh.com.au', 0),
(31, 'Naomi', 'Dellit', 9312311182, 4856, 'Itbayat', '2020-05-13', 9, 17, 'Senior Editor', 'ndellitk', 'ftTs4LS', 'ndellitk@uol.com.br', 0),
(32, 'Jobina', 'Jumel', 6663864572, 3309, 'Celso Ramos', '2019-06-21', 8, 17, 'Chemical Engineer', 'jjumell', 'DEvDd2MLZ', 'jjumell@woothemes.com', 0),
(33, 'Kamila', 'Rowth', 1222463849, 754, 'Paquera', '2020-03-11', 10, 14, 'Research Assistant III', 'krowthm', '7DjnSJJXsnx', 'krowthm@t.co', 0),
(34, 'Zarla', 'O\'Neary', 6279332624, 2973, 'Bayan-Ovoo', '2019-07-07', 7, 14, 'Paralegal', 'zonearyn', 'QulXOy8EzIA', 'zonearyn@redcross.org', 0),
(35, 'Cordy', 'Adamovitch', 4372071264, 244, 'Tubigan', '2019-12-03', 9, 14, 'Research Assistant III', 'cadamovitcho', '6EioZYRrBAb0', 'cadamovitcho@oracle.com', 0),
(36, 'aaa', 'aaa', 123, 0, 'aaa', '2020-06-14', 0, 0, '', 'aaa', 'aaa', 'aaa', 0);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rezerwacje_lab`
--

CREATE TABLE `rezerwacje_lab` (
  `id_rezerwacji` int(11) NOT NULL,
  `id_pracownika` int(11) NOT NULL,
  `termin` datetime NOT NULL
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
  `id_zakupu` int(11) DEFAULT NULL,
  `id_pracownika` int(11) DEFAULT NULL,
  `id_odbioru` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `wydatki`
--

INSERT INTO `wydatki` (`id_wydatku`, `typ_wydatku`, `cena`, `data`, `id_zakupu`, `id_pracownika`, `id_odbioru`) VALUES
(58, 'odpady', 104, '2019-10-04', NULL, NULL, 10),
(59, 'odpady', 228, '2019-11-04', NULL, NULL, 11),
(60, 'odpady', 279, '2020-05-05', NULL, NULL, 12),
(61, 'odpady', 430, '2020-05-26', NULL, NULL, 13),
(62, 'odpady', 162, '2020-03-27', NULL, NULL, 14),
(63, 'odpady', 160, '2020-03-20', NULL, NULL, 15),
(64, 'odpady', 630, '2019-08-24', NULL, NULL, 16),
(65, 'odpady', 203, '2019-09-03', NULL, NULL, 17),
(66, 'odpady', 116, '2019-07-28', NULL, NULL, 18),
(67, 'odpady', 144, '2020-01-14', NULL, NULL, 19),
(73, 'pensja', 2023, '2020-06-14', NULL, 1, NULL),
(74, 'pensja', 3035, '2020-06-14', NULL, 2, NULL),
(75, 'pensja', 12345, '2020-06-14', NULL, 3, NULL),
(76, 'pensja', 3630, '2020-06-14', NULL, 11, NULL),
(77, 'pensja', 4473, '2020-06-14', NULL, 12, NULL),
(78, 'pensja', 1524, '2020-06-14', NULL, 13, NULL),
(79, 'pensja', 2547, '2020-06-14', NULL, 14, NULL),
(80, 'pensja', 4437, '2020-06-14', NULL, 15, NULL),
(81, 'pensja', 1381, '2020-06-14', NULL, 16, NULL),
(82, 'pensja', 3999, '2020-06-14', NULL, 17, NULL),
(83, 'pensja', 3061, '2020-06-14', NULL, 18, NULL),
(84, 'pensja', 549, '2020-06-14', NULL, 19, NULL),
(85, 'pensja', 4778, '2020-06-14', NULL, 20, NULL),
(86, 'pensja', 4402, '2020-06-14', NULL, 21, NULL),
(87, 'pensja', 4473, '2020-06-14', NULL, 22, NULL),
(88, 'pensja', 113, '2020-06-14', NULL, 23, NULL),
(89, 'pensja', 2145, '2020-06-14', NULL, 24, NULL),
(90, 'pensja', 1045, '2020-06-14', NULL, 25, NULL),
(91, 'pensja', 4009, '2020-06-14', NULL, 26, NULL),
(92, 'pensja', 1213, '2020-06-14', NULL, 27, NULL),
(93, 'pensja', 3198, '2020-06-14', NULL, 28, NULL),
(94, 'pensja', 1228, '2020-06-14', NULL, 29, NULL),
(95, 'pensja', 1777, '2020-06-14', NULL, 30, NULL),
(96, 'pensja', 4856, '2020-06-14', NULL, 31, NULL),
(97, 'pensja', 3309, '2020-06-14', NULL, 32, NULL),
(98, 'pensja', 754, '2020-06-14', NULL, 33, NULL),
(99, 'pensja', 2973, '2020-06-14', NULL, 34, NULL),
(100, 'pensja', 244, '2020-06-14', NULL, 35, NULL);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `zakupy`
--

CREATE TABLE `zakupy` (
  `id_zakupu` int(11) NOT NULL,
  `id_zwiazku` int(11) DEFAULT NULL,
  `id_sprzetu` int(11) DEFAULT NULL,
  `data_zakupu` date NOT NULL,
  `ilosc` int(11) NOT NULL,
  `cena` float NOT NULL,
  `stan_zamowienia` text CHARACTER SET utf8 COLLATE utf8_polish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;

--
-- Zrzut danych tabeli `zakupy`
--

INSERT INTO `zakupy` (`id_zakupu`, `id_zwiazku`, `id_sprzetu`, `data_zakupu`, `ilosc`, `cena`, `stan_zamowienia`) VALUES
(22, 1, NULL, '2020-06-04', 4, 86, '0'),
(23, 2, NULL, '2020-03-13', 57, 272, '0'),
(24, 2, NULL, '2020-01-04', 97, 20, '0'),
(25, 2, NULL, '2019-09-11', 21, 34, '0'),
(26, 1, NULL, '2019-06-20', 41, 280, '0'),
(27, 1, NULL, '2019-06-16', 53, 200, '0'),
(28, 2, NULL, '2019-08-12', 33, 6, '0'),
(29, 2, NULL, '2019-08-12', 10, 238, '0'),
(30, 1, NULL, '2020-05-05', 61, 176, '0'),
(31, 1, NULL, '2020-05-06', 30, 73, '0'),
(32, 1, NULL, '2019-11-14', 80, 267, '0'),
(33, 1, NULL, '2019-06-23', 1, 84, '0'),
(34, 2, NULL, '2020-06-11', 34, 282, '0'),
(35, 1, NULL, '2020-01-09', 48, 280, '0'),
(36, 1, NULL, '2020-06-02', 96, 27, '0'),
(37, 1, NULL, '2019-10-21', 80, 47, '0'),
(38, 2, NULL, '2019-10-12', 22, 154, '0'),
(39, 1, NULL, '2019-09-29', 1, 276, '0'),
(40, 1, NULL, '2020-01-14', 84, 185, '0'),
(41, 1, NULL, '2019-07-21', 46, 290, '0'),
(42, NULL, 2, '2019-09-25', 13, 285, '0'),
(43, NULL, 2, '2020-06-01', 72, 40, '0'),
(44, NULL, 2, '2020-01-22', 43, 259, '0'),
(45, NULL, 1, '2020-04-30', 99, 268, '0'),
(46, NULL, 2, '2020-03-24', 55, 134, '0'),
(47, NULL, 1, '2020-04-20', 10, 244, '0'),
(48, NULL, 1, '2019-11-29', 25, 187, '0'),
(49, NULL, 1, '2019-11-17', 63, 295, '0'),
(50, NULL, 2, '2020-01-18', 40, 240, '0'),
(51, NULL, 2, '2019-12-19', 26, 199, '0'),
(52, NULL, 2, '2020-01-26', 83, 3, '0'),
(53, NULL, 3, '2020-04-08', 95, 7, '0'),
(54, NULL, 2, '2019-11-19', 36, 73, '0'),
(55, NULL, 2, '2019-11-18', 38, 23, '0'),
(56, NULL, 1, '2020-01-17', 54, 141, '0'),
(57, NULL, 1, '2019-11-08', 3, 171, '0'),
(58, NULL, 3, '2019-08-09', 15, 254, '0'),
(59, NULL, 2, '2019-07-18', 68, 9, '0'),
(60, NULL, 1, '2019-06-21', 61, 228, '0'),
(61, NULL, 2, '2019-11-16', 78, 130, '0');

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
(26, 2, '2020-03-14', 10),
(32, 1, '2019-10-05', 6),
(25, 2, '2019-07-18', 3),
(25, 2, '2020-05-28', 9),
(15, 1, '2020-03-18', 8),
(16, 1, '2020-01-07', 5),
(31, 2, '2019-06-30', 5),
(23, 2, '2020-01-14', 10),
(31, 1, '2020-02-21', 10),
(18, 2, '2020-03-02', 6),
(11, 1, '2019-07-05', 1),
(17, 2, '2020-01-11', 6),
(17, 2, '2019-10-02', 8),
(27, 1, '2020-02-11', 3),
(12, 2, '2019-06-25', 5),
(17, 1, '2020-05-14', 5),
(23, 2, '2019-11-19', 8),
(17, 2, '2019-12-12', 8),
(32, 1, '2020-05-19', 10),
(28, 2, '2019-06-27', 2),
(36, 1, '2020-06-14', 11),
(36, 1, '2020-06-14', 1);

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
  ADD PRIMARY KEY (`id_rezerwacji`),
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
-- AUTO_INCREMENT dla tabeli `odbior_odpadow`
--
ALTER TABLE `odbior_odpadow`
  MODIFY `id_odbioru` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT dla tabeli `rezerwacje_lab`
--
ALTER TABLE `rezerwacje_lab`
  MODIFY `id_rezerwacji` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `sprzet_lab`
--
ALTER TABLE `sprzet_lab`
  MODIFY `id_sprzetu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT dla tabeli `wydatki`
--
ALTER TABLE `wydatki`
  MODIFY `id_wydatku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT dla tabeli `zakupy`
--
ALTER TABLE `zakupy`
  MODIFY `id_zakupu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `rezerwacje_lab`
--
ALTER TABLE `rezerwacje_lab`
  ADD CONSTRAINT `rezerwacje_lab_ibfk_1` FOREIGN KEY (`id_pracownika`) REFERENCES `pracownicy` (`id_pracownika`);

--
-- Ograniczenia dla tabeli `zakupy`
--
ALTER TABLE `zakupy`
  ADD CONSTRAINT `zakupy_ibfk_1` FOREIGN KEY (`id_sprzetu`) REFERENCES `sprzet_lab` (`id_sprzetu`),
  ADD CONSTRAINT `zakupy_ibfk_2` FOREIGN KEY (`id_zwiazku`) REFERENCES `info_o_zwiazku` (`id_zwiazku`);

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
