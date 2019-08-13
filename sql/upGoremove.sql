-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: 2019-08-12 16:15:29
-- 服务器版本： 5.7.26-log
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `upGoremove`
--

-- --------------------------------------------------------

--
-- 表的结构 `UG_KEYBOX`
--

CREATE TABLE `UG_KEYBOX` (
  `id` int(12) NOT NULL,
  `Rkey` varchar(32) NOT NULL,
  `num` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- --------------------------------------------------------

--
-- 表的结构 `UG_KEYOFMAC`
--

CREATE TABLE `UG_KEYOFMAC` (
  `id` int(12) NOT NULL,
  `keyId` int(12) NOT NULL,
  `macId` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `UG_MACBOX`
--

CREATE TABLE `UG_MACBOX` (
  `id` int(12) NOT NULL,
  `userMac` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `UG_MACBOX`
--

INSERT INTO `UG_MACBOX` (`id`, `userMac`) VALUES
(1, '2c:60:0c:9c:d5:2e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `UG_KEYBOX`
--
ALTER TABLE `UG_KEYBOX`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `UG_KEYOFMAC`
--
ALTER TABLE `UG_KEYOFMAC`
  ADD PRIMARY KEY (`id`),
  ADD KEY `KEYOFMAC_KEY` (`keyId`),
  ADD KEY `KEYOFMAC_MAC` (`macId`);

--
-- Indexes for table `UG_MACBOX`
--
ALTER TABLE `UG_MACBOX`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `UG_KEYBOX`
--
ALTER TABLE `UG_KEYBOX`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- 使用表AUTO_INCREMENT `UG_KEYOFMAC`
--
ALTER TABLE `UG_KEYOFMAC`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `UG_MACBOX`
--
ALTER TABLE `UG_MACBOX`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 限制导出的表
--

--
-- 限制表 `UG_KEYOFMAC`
--
ALTER TABLE `UG_KEYOFMAC`
  ADD CONSTRAINT `KEYOFMAC_KEY` FOREIGN KEY (`keyId`) REFERENCES `UG_KEYBOX` (`id`),
  ADD CONSTRAINT `KEYOFMAC_MAC` FOREIGN KEY (`macId`) REFERENCES `UG_MACBOX` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
