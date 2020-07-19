-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 
-- 伺服器版本： 10.4.8-MariaDB
-- PHP 版本： 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `2020-04-05`
--

-- --------------------------------------------------------

--
-- 資料表結構 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `source` varchar(200) NOT NULL,
  `create_date` date NOT NULL,
  `description` text NOT NULL,
  `look` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `news`
--

INSERT INTO `news` (`id`, `title`, `source`, `create_date`, `description`, `look`) VALUES
(1, 'AI應用人才遍地開花TibaMe與勞動部合作開班', '經濟日報', '2018-09-22', '緯育TibaMe團隊進一步獲得勞動部勞動力發展署桃竹苗分署肯定，107年建置「AI人工智慧產業專才發展基地」的專業AI人才培訓單位，將於十月底到 ...', NULL),
(2, 'TibaMe【2019培才趨勢雙週論壇】全力推動『數位轉型x跨域人才』', '鉅亨網', '2019-03-04', '緯育TibaMe「提拔我」是全台「數位跨域人才培育加速器」，不僅服務超過14 萬會員，與超過800 家企業合作徵才，更協助超過500 家企業進行數位轉型 ...', NULL),
(3, '緯育TibaMe盛大舉辦首屆『培才趨勢年會』聚集專家及企業共同', '鏡週刊', '2018-10-08', 'TibaMe學習網從2015年正式成立，聚焦於泛資通訊領域的人才培訓，至今已經透過數位學習服務超過13萬會員，並與600家企業合作，輔導超過上千 ...', NULL);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
