-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 07-09-2023 a las 11:35:55
-- Versión del servidor: 10.3.39-MariaDB-cll-lve
-- Versión de PHP: 8.1.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fgromano_webpersonal`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formacion`
--

CREATE TABLE `formacion` (
  `form_ind` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `centro` varchar(100) NOT NULL,
  `duracion` int(11) NOT NULL,
  `fecha_inicial` date NOT NULL,
  `fecha_final` date NOT NULL,
  `tipo` varchar(40) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `formacion`
--

INSERT INTO `formacion` (`form_ind`, `titulo`, `centro`, `duracion`, `fecha_inicial`, `fecha_final`, `tipo`) VALUES
(1, 'Licenciado en Biología', 'Universidad de Oviedo', 5, '2000-09-01', '2005-12-01', 'Carrera universitari'),
(2, 'Doctor en Biología', 'Universidad Complutense de Madrid', 4, '2010-09-01', '2015-06-30', 'Doctorado (PhD)'),
(3, 'Técnico superior en Diseño de Aplicaciones Web', 'CIFP Pau Casesnoves', 2, '2021-10-01', '2023-06-30', 'Ciclo Superior de FP');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `formacion`
--
ALTER TABLE `formacion`
  ADD PRIMARY KEY (`form_ind`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
