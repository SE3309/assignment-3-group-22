-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: 3309proj
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `departmentID` int NOT NULL,
  `departmentName` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `postalCode` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`departmentID`),
  UNIQUE KEY `departmentName` (`departmentName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Department_1','742 Main St, City 1','57368'),(2,'Department_2','834 Main St, City 2','53043'),(3,'Department_3','894 Main St, City 3','63483'),(4,'Department_4','725 Main St, City 4','28035'),(5,'Department_5','885 Main St, City 5','78726'),(6,'Department_6','518 Main St, City 6','10466'),(7,'Department_7','561 Main St, City 7','97626'),(8,'Department_8','797 Main St, City 8','97875'),(9,'Department_9','338 Main St, City 9','14017'),(10,'Department_10','253 Main St, City 10','48691'),(11,'Department_11','471 Main St, City 11','64838'),(12,'Department_12','395 Main St, City 12','32055'),(13,'Department_13','723 Main St, City 13','56242'),(14,'Department_14','104 Main St, City 14','60155'),(15,'Department_15','797 Main St, City 15','81196'),(16,'Department_16','805 Main St, City 16','31217'),(17,'Department_17','117 Main St, City 17','32165'),(18,'Department_18','946 Main St, City 18','33834'),(19,'Department_19','954 Main St, City 19','64503'),(20,'Department_20','552 Main St, City 20','67093'),(21,'Department_21','239 Main St, City 21','17139'),(22,'Department_22','46 Main St, City 22','68020'),(23,'Department_23','12 Main St, City 23','65737'),(24,'Department_24','523 Main St, City 24','78328'),(25,'Department_25','298 Main St, City 25','88427');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-09 15:48:14
