-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: stream-hackathon.cxcymd5kllyc.us-east-1.rds.amazonaws.com    Database: stream-hackathon
-- ------------------------------------------------------
-- Server version	8.0.35

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `brand_a_campaigns`
--

DROP TABLE IF EXISTS `brand_a_campaigns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand_a_campaigns` (
  `campaign_id` varchar(45) NOT NULL,
  `portfolio_id` varchar(45) DEFAULT NULL,
  `state` text,
  `name` text,
  `ad_type` text,
  `report_type` varchar(45) DEFAULT NULL,
  `cost_type` text,
  `target_type` text,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `budget` float DEFAULT NULL,
  `tos_modifier` float DEFAULT NULL,
  `pp_modifier` float DEFAULT NULL,
  `ros_modifier` float DEFAULT NULL,
  `tag_1` text,
  `tag_2` text,
  `tag_3` text,
  `tag_4` text,
  `tag_5` text,
  `tag_6` text,
  `tag_7` text,
  `tag_8` text,
  `tag_9` text,
  `tag_10` text,
  `tag_11` text,
  `tag_12` text,
  `origin` text,
  `last_updated_in_db` datetime DEFAULT NULL,
  PRIMARY KEY (`campaign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand_a_campaigns`
--

LOCK TABLES `brand_a_campaigns` WRITE;
/*!40000 ALTER TABLE `brand_a_campaigns` DISABLE KEYS */;
INSERT INTO `brand_a_campaigns` VALUES ('144185387033434285','252626367868910','ENABLED','Probiotics | Womens Probiotics | SB | Nexus | 1.0 P | $BTR | NEXUS','SB','campaigns','CPC',NULL,'2020-08-25',NULL,471.86,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:49:24'),('180432605785118','153835778404287','ENABLED','Prenatal | Prenatal Vitamins | B005JAT3TU | SP | B | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2020-11-21',NULL,31.2,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('182017324249446','133165741479386','ENABLED','Ashwagandha | B07G7XZT5K | SP | KR | 1.1 P | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2022-05-30',NULL,10,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-25 14:22:14'),('190968188059827','84075567514339','ENABLED','Vitamins | Mens Multi Vitamin | SP | Nexus | 1.4 P | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2020-08-18',NULL,422.5,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('202129081943787','182142745107975','ENABLED','Herbal | Turmeric | B07G2LBQ1G | SP | A-SG | CAT | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2022-05-26',NULL,110.5,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('203895691201075','149635200217941','ENABLED','Meal/Protein | Organic Vegan Vanilla Protein Powder | SP | Nexus KW | 3.19 P | B0031JK96C | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2023-06-14',NULL,78,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('23538048283352','68461407566273','ENABLED','Herbal - Other | mykind Organics Oregano Oil Drops | SP | Nexus KW | 3.5 E | B07G7MRZT6 | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2023-06-14',NULL,13,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('255804355714626','84075567514339','ENABLED','Vitamins | Womens Multi Vitamin | SP | Nexus | 2.3 B | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2020-08-17',NULL,130,0,0,0,'Awareness','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09'),('275082917844423','149635200217941','ENABLED','Meal or Protein | Protein Powder | SP | Nexus | 1.6 P | $BTR | NEXUS','SP','campaigns',NULL,'MANUAL','2020-08-18',NULL,104,0,0,0,'Ranking','Non-Branded','Efficiency',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'Amazon Ads API','2024-05-28 16:47:09');
/*!40000 ALTER TABLE `brand_a_campaigns` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-04  8:37:13
