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
INSERT INTO `department` VALUES (1,'Science','522 Main St, City 1','59422'),(2,'English','128 Main St, City 2','89471'),(3,'History','905 Main St, City 3','55535'),(4,'Physical Education','146 Main St, City 4','43004'),(5,'Art','322 Main St, City 5','36596'),(6,'Music','717 Main St, City 6','93248'),(7,'Social Studies','128 Main St, City 7','48213'),(8,'Computer Science','830 Main St, City 8','73285'),(9,'Foreign Languages','244 Main St, City 9','28919'),(10,'Philosophy','909 Main St, City 10','24872'),(11,'Psychology','439 Main St, City 11','91960'),(12,'Economics','43 Main St, City 12','29355'),(13,'Business Studies','520 Main St, City 13','95282'),(14,'Chemistry','856 Main St, City 14','65787'),(15,'Physics','247 Main St, City 15','31234'),(16,'Biology','813 Main St, City 16','64444'),(17,'Environmental Science','721 Main St, City 17','28104'),(18,'Librarian Services','424 Main St, City 18','95455'),(19,'Geography','871 Main St, City 19','18814'),(20,'Political Science','832 Main St, City 20','50099'),(21,'Engineering','882 Main St, City 21','50675'),(22,'Anthropology','410 Main St, City 22','97766'),(23,'Architecture','661 Main St, City 23','79341'),(24,'Culinary Arts','102 Main St, City 24','67557'),(25,'Journalism','929 Main St, City 25','40100');
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

-- Dump completed on 2024-11-09 17:00:05
