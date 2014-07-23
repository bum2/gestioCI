CREATE DATABASE  IF NOT EXISTS `gestioCI` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `gestioCI`;
-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gestioCI
-- ------------------------------------------------------
-- Server version	5.5.35-0+wheezy1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `General_address_type`
--

DROP TABLE IF EXISTS `General_address_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_address_type` (
  `space_type_id` int(11) NOT NULL,
  PRIMARY KEY (`space_type_id`),
  CONSTRAINT `space_type_id_refs_typ_id_9112582a` FOREIGN KEY (`space_type_id`) REFERENCES `General_space_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_address_type`
--

LOCK TABLES `General_address_type` WRITE;
/*!40000 ALTER TABLE `General_address_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_address_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_region`
--

DROP TABLE IF EXISTS `General_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `space_type_id` int(11) DEFAULT NULL,
  `comment` longtext,
  `longitude` int(11) DEFAULT NULL,
  `latitude` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `General_region_d2c3a6a8` (`space_type_id`),
  KEY `General_region_410d0aac` (`parent_id`),
  KEY `General_region_329f6fb3` (`lft`),
  KEY `General_region_e763210f` (`rght`),
  KEY `General_region_ba470c4a` (`tree_id`),
  KEY `General_region_20e079f4` (`level`),
  CONSTRAINT `parent_id_refs_id_d0933889` FOREIGN KEY (`parent_id`) REFERENCES `General_region` (`id`),
  CONSTRAINT `space_type_id_refs_typ_id_d76c1cd0` FOREIGN KEY (`space_type_id`) REFERENCES `General_space_type` (`typ_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_region`
--

LOCK TABLES `General_region` WRITE;
/*!40000 ALTER TABLE `General_region` DISABLE KEYS */;
INSERT INTO `General_region` VALUES (1,'Països Catalans',NULL,'',NULL,NULL,NULL,1,6,1,0),(2,'Catalunya',11,'',NULL,NULL,1,2,5,1,1),(3,'Barcelonès',38,'',NULL,NULL,2,3,4,1,2);
/*!40000 ALTER TABLE `General_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_project`
--

DROP TABLE IF EXISTS `General_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_project` (
  `human_id` int(11) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `socialweb` varchar(30) NOT NULL,
  `email2` varchar(75) NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`human_id`),
  KEY `General_project_410d0aac` (`parent_id`),
  KEY `General_project_329f6fb3` (`lft`),
  KEY `General_project_e763210f` (`rght`),
  KEY `General_project_ba470c4a` (`tree_id`),
  KEY `General_project_20e079f4` (`level`),
  CONSTRAINT `human_id_refs_id_c0052093` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`),
  CONSTRAINT `parent_id_refs_human_id_cb4b7459` FOREIGN KEY (`parent_id`) REFERENCES `General_project` (`human_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_project`
--

LOCK TABLES `General_project` WRITE;
/*!40000 ALTER TABLE `General_project` DISABLE KEYS */;
INSERT INTO `General_project` VALUES (1,NULL,'','',1,4,1,0),(2,1,'','',2,3,1,1);
/*!40000 ALTER TABLE `General_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_project_ref_members`
--

DROP TABLE IF EXISTS `General_project_ref_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_project_ref_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_id` (`project_id`,`person_id`),
  KEY `General_project_ref_members_37952554` (`project_id`),
  KEY `General_project_ref_members_16f39487` (`person_id`),
  CONSTRAINT `person_id_refs_human_id_574b5d42` FOREIGN KEY (`person_id`) REFERENCES `General_person` (`human_id`),
  CONSTRAINT `project_id_refs_human_id_ebecb464` FOREIGN KEY (`project_id`) REFERENCES `General_project` (`human_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_project_ref_members`
--

LOCK TABLES `General_project_ref_members` WRITE;
/*!40000 ALTER TABLE `General_project_ref_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_project_ref_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_space_type`
--

DROP TABLE IF EXISTS `General_space_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_space_type` (
  `typ_id` int(11) NOT NULL,
  PRIMARY KEY (`typ_id`),
  CONSTRAINT `typ_id_refs_concept_id_5dcfea05` FOREIGN KEY (`typ_id`) REFERENCES `General_type` (`concept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_space_type`
--

LOCK TABLES `General_space_type` WRITE;
/*!40000 ALTER TABLE `General_space_type` DISABLE KEYS */;
INSERT INTO `General_space_type` VALUES (11),(12),(36),(37),(38);
/*!40000 ALTER TABLE `General_space_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_material_type`
--

DROP TABLE IF EXISTS `General_material_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_material_type` (
  `artwork_type_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_type_id`),
  CONSTRAINT `artwork_type_id_refs_typ_id_416409e2` FOREIGN KEY (`artwork_type_id`) REFERENCES `General_artwork_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_material_type`
--

LOCK TABLES `General_material_type` WRITE;
/*!40000 ALTER TABLE `General_material_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_material_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_accountbank`
--

DROP TABLE IF EXISTS `General_accountbank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_accountbank` (
  `record_id` int(11) NOT NULL,
  `human_id` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `number` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`record_id`),
  KEY `General_accountbank_6922ec88` (`human_id`),
  KEY `General_accountbank_0316dde1` (`company_id`),
  KEY `General_accountbank_b9dcc52b` (`unit_id`),
  CONSTRAINT `company_id_refs_human_id_466f5e8e` FOREIGN KEY (`company_id`) REFERENCES `General_company` (`human_id`),
  CONSTRAINT `human_id_refs_id_d6164342` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`),
  CONSTRAINT `record_id_refs_id_a20996dc` FOREIGN KEY (`record_id`) REFERENCES `General_record` (`id`),
  CONSTRAINT `unit_id_refs_id_e5728480` FOREIGN KEY (`unit_id`) REFERENCES `General_unit` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_accountbank`
--

LOCK TABLES `General_accountbank` WRITE;
/*!40000 ALTER TABLE `General_accountbank` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_accountbank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_record_type`
--

DROP TABLE IF EXISTS `General_record_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_record_type` (
  `artwork_type_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_type_id`),
  CONSTRAINT `artwork_type_id_refs_typ_id_18d309fa` FOREIGN KEY (`artwork_type_id`) REFERENCES `General_artwork_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_record_type`
--

LOCK TABLES `General_record_type` WRITE;
/*!40000 ALTER TABLE `General_record_type` DISABLE KEYS */;
INSERT INTO `General_record_type` VALUES (39),(40),(41),(43),(44);
/*!40000 ALTER TABLE `General_record_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_relation`
--

DROP TABLE IF EXISTS `General_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_relation` (
  `art_id` int(11) NOT NULL,
  `clas` varchar(30) NOT NULL,
  PRIMARY KEY (`art_id`),
  CONSTRAINT `art_id_refs_id_46450b3e` FOREIGN KEY (`art_id`) REFERENCES `General_art` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_relation`
--

LOCK TABLES `General_relation` WRITE;
/*!40000 ALTER TABLE `General_relation` DISABLE KEYS */;
INSERT INTO `General_relation` VALUES (3,'Membership');
/*!40000 ALTER TABLE `General_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_person`
--

DROP TABLE IF EXISTS `General_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_person` (
  `human_id` int(11) NOT NULL,
  `surnames` varchar(40) NOT NULL,
  `id_card` varchar(9) NOT NULL,
  `email2` varchar(75) NOT NULL,
  `nickname2` varchar(20) NOT NULL,
  PRIMARY KEY (`human_id`),
  CONSTRAINT `human_id_refs_id_ce327b3b` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_person`
--

LOCK TABLES `General_person` WRITE;
/*!40000 ALTER TABLE `General_person` DISABLE KEYS */;
INSERT INTO `General_person` VALUES (3,'','','','');
/*!40000 ALTER TABLE `General_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_company_type`
--

DROP TABLE IF EXISTS `General_company_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_company_type` (
  `being_type_id` int(11) NOT NULL,
  PRIMARY KEY (`being_type_id`),
  CONSTRAINT `being_type_id_refs_typ_id_f04123a9` FOREIGN KEY (`being_type_id`) REFERENCES `General_being_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_company_type`
--

LOCK TABLES `General_company_type` WRITE;
/*!40000 ALTER TABLE `General_company_type` DISABLE KEYS */;
INSERT INTO `General_company_type` VALUES (35),(45);
/*!40000 ALTER TABLE `General_company_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_unit_type`
--

DROP TABLE IF EXISTS `General_unit_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_unit_type` (
  `artwork_type_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_type_id`),
  CONSTRAINT `artwork_type_id_refs_typ_id_0b70a72e` FOREIGN KEY (`artwork_type_id`) REFERENCES `General_artwork_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_unit_type`
--

LOCK TABLES `General_unit_type` WRITE;
/*!40000 ALTER TABLE `General_unit_type` DISABLE KEYS */;
INSERT INTO `General_unit_type` VALUES (14),(17),(18),(19);
/*!40000 ALTER TABLE `General_unit_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_person_projects`
--

DROP TABLE IF EXISTS `General_person_projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_person_projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`,`project_id`),
  KEY `General_person_projects_16f39487` (`person_id`),
  KEY `General_person_projects_37952554` (`project_id`),
  CONSTRAINT `person_id_refs_human_id_58cf10c0` FOREIGN KEY (`person_id`) REFERENCES `General_person` (`human_id`),
  CONSTRAINT `project_id_refs_human_id_8bb63966` FOREIGN KEY (`project_id`) REFERENCES `General_project` (`human_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_person_projects`
--

LOCK TABLES `General_person_projects` WRITE;
/*!40000 ALTER TABLE `General_person_projects` DISABLE KEYS */;
INSERT INTO `General_person_projects` VALUES (1,3,2);
/*!40000 ALTER TABLE `General_person_projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_human`
--

DROP TABLE IF EXISTS `General_human`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_human` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `being_type_id` int(11) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `dead_date` date DEFAULT NULL,
  `nickname` varchar(20) NOT NULL,
  `email` varchar(40) NOT NULL,
  `telephone` varchar(20) NOT NULL,
  `website` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `General_human_9b04ef5e` (`being_type_id`),
  CONSTRAINT `being_type_id_refs_typ_id_5427e9c4` FOREIGN KEY (`being_type_id`) REFERENCES `General_being_type` (`typ_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_human`
--

LOCK TABLES `General_human` WRITE;
/*!40000 ALTER TABLE `General_human` DISABLE KEYS */;
INSERT INTO `General_human` VALUES (1,'Xarxa de Cooperatives Integrals',7,NULL,NULL,'XCI','','',''),(2,'Cooperativa Integral Catalana',8,'2010-07-21',NULL,'CIC','','',''),(3,'Sebas',NULL,'1972-09-29',NULL,'bumbum','','','');
/*!40000 ALTER TABLE `General_human` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_nonmaterial`
--

DROP TABLE IF EXISTS `General_nonmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_nonmaterial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `nonmaterial_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `General_nonmaterial_d40a8f00` (`nonmaterial_type_id`),
  CONSTRAINT `nonmaterial_type_id_refs_artwork_type_id_185071f1` FOREIGN KEY (`nonmaterial_type_id`) REFERENCES `General_nonmaterial_type` (`artwork_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_nonmaterial`
--

LOCK TABLES `General_nonmaterial` WRITE;
/*!40000 ALTER TABLE `General_nonmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_nonmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_unitratio`
--

DROP TABLE IF EXISTS `General_unitratio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_unitratio` (
  `record_id` int(11) NOT NULL,
  `in_unit_id` int(11) NOT NULL,
  `rate` decimal(6,3) NOT NULL,
  `out_unit_id` int(11) NOT NULL,
  PRIMARY KEY (`record_id`),
  KEY `General_unitratio_49ac93b0` (`in_unit_id`),
  KEY `General_unitratio_17576a54` (`out_unit_id`),
  CONSTRAINT `out_unit_id_refs_id_e045a3a5` FOREIGN KEY (`out_unit_id`) REFERENCES `General_unit` (`id`),
  CONSTRAINT `in_unit_id_refs_id_e045a3a5` FOREIGN KEY (`in_unit_id`) REFERENCES `General_unit` (`id`),
  CONSTRAINT `record_id_refs_id_e333dd70` FOREIGN KEY (`record_id`) REFERENCES `General_record` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_unitratio`
--

LOCK TABLES `General_unitratio` WRITE;
/*!40000 ALTER TABLE `General_unitratio` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_unitratio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_company_ref_members`
--

DROP TABLE IF EXISTS `General_company_ref_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_company_ref_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `company_id` (`company_id`,`person_id`),
  KEY `General_company_ref_members_0316dde1` (`company_id`),
  KEY `General_company_ref_members_16f39487` (`person_id`),
  CONSTRAINT `company_id_refs_human_id_3fddb5c6` FOREIGN KEY (`company_id`) REFERENCES `General_company` (`human_id`),
  CONSTRAINT `person_id_refs_human_id_9272530d` FOREIGN KEY (`person_id`) REFERENCES `General_person` (`human_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_company_ref_members`
--

LOCK TABLES `General_company_ref_members` WRITE;
/*!40000 ALTER TABLE `General_company_ref_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_company_ref_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_region_type`
--

DROP TABLE IF EXISTS `General_region_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_region_type` (
  `space_type_id` int(11) NOT NULL,
  PRIMARY KEY (`space_type_id`),
  CONSTRAINT `space_type_id_refs_typ_id_723b7251` FOREIGN KEY (`space_type_id`) REFERENCES `General_space_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_region_type`
--

LOCK TABLES `General_region_type` WRITE;
/*!40000 ALTER TABLE `General_region_type` DISABLE KEYS */;
INSERT INTO `General_region_type` VALUES (36),(37),(38);
/*!40000 ALTER TABLE `General_region_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_accountces`
--

DROP TABLE IF EXISTS `General_accountces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_accountces` (
  `record_id` int(11) NOT NULL,
  `human_id` int(11) NOT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `unit_id` int(11) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `number` varchar(4) DEFAULT NULL,
  PRIMARY KEY (`record_id`),
  KEY `General_accountces_6922ec88` (`human_id`),
  KEY `General_accountces_c096cf48` (`entity_id`),
  KEY `General_accountces_b9dcc52b` (`unit_id`),
  CONSTRAINT `entity_id_refs_human_id_935d5d48` FOREIGN KEY (`entity_id`) REFERENCES `General_project` (`human_id`),
  CONSTRAINT `human_id_refs_id_da305fb3` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`),
  CONSTRAINT `record_id_refs_id_2286902b` FOREIGN KEY (`record_id`) REFERENCES `General_record` (`id`),
  CONSTRAINT `unit_id_refs_id_07a72ac8` FOREIGN KEY (`unit_id`) REFERENCES `General_unit` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_accountces`
--

LOCK TABLES `General_accountces` WRITE;
/*!40000 ALTER TABLE `General_accountces` DISABLE KEYS */;
INSERT INTO `General_accountces` VALUES (3,3,2,1,'COOP','0111');
/*!40000 ALTER TABLE `General_accountces` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_being_type`
--

DROP TABLE IF EXISTS `General_being_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_being_type` (
  `typ_id` int(11) NOT NULL,
  PRIMARY KEY (`typ_id`),
  CONSTRAINT `typ_id_refs_concept_id_8745a66c` FOREIGN KEY (`typ_id`) REFERENCES `General_type` (`concept_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_being_type`
--

LOCK TABLES `General_being_type` WRITE;
/*!40000 ALTER TABLE `General_being_type` DISABLE KEYS */;
INSERT INTO `General_being_type` VALUES (5),(6),(7),(8),(9),(10),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(34),(35),(45),(46);
/*!40000 ALTER TABLE `General_being_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_job`
--

DROP TABLE IF EXISTS `General_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_job` (
  `art_id` int(11) NOT NULL,
  `clas` varchar(30) NOT NULL,
  PRIMARY KEY (`art_id`),
  CONSTRAINT `art_id_refs_id_c23db58e` FOREIGN KEY (`art_id`) REFERENCES `General_art` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_job`
--

LOCK TABLES `General_job` WRITE;
/*!40000 ALTER TABLE `General_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_nonmaterial_type`
--

DROP TABLE IF EXISTS `General_nonmaterial_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_nonmaterial_type` (
  `artwork_type_id` int(11) NOT NULL,
  PRIMARY KEY (`artwork_type_id`),
  CONSTRAINT `artwork_type_id_refs_typ_id_5702be87` FOREIGN KEY (`artwork_type_id`) REFERENCES `General_artwork_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_nonmaterial_type`
--

LOCK TABLES `General_nonmaterial_type` WRITE;
/*!40000 ALTER TABLE `General_nonmaterial_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_nonmaterial_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_human_addresses`
--

DROP TABLE IF EXISTS `General_human_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_human_addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `human_id` int(11) NOT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `human_id` (`human_id`,`address_id`),
  KEY `General_human_addresses_6922ec88` (`human_id`),
  KEY `General_human_addresses_3ac8a70a` (`address_id`),
  CONSTRAINT `address_id_refs_id_63816851` FOREIGN KEY (`address_id`) REFERENCES `General_address` (`id`),
  CONSTRAINT `human_id_refs_id_7dd94b0f` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_human_addresses`
--

LOCK TABLES `General_human_addresses` WRITE;
/*!40000 ALTER TABLE `General_human_addresses` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_human_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_address`
--

DROP TABLE IF EXISTS `General_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `space_type_id` int(11) DEFAULT NULL,
  `comment` longtext,
  `longitude` int(11) DEFAULT NULL,
  `latitude` int(11) DEFAULT NULL,
  `p_address` varchar(50) NOT NULL,
  `town` varchar(40) NOT NULL,
  `postalcode` varchar(5) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `m2` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `General_address_d2c3a6a8` (`space_type_id`),
  KEY `General_address_55a4ce96` (`region_id`),
  CONSTRAINT `region_id_refs_id_c1ad246c` FOREIGN KEY (`region_id`) REFERENCES `General_region` (`id`),
  CONSTRAINT `space_type_id_refs_typ_id_7916783a` FOREIGN KEY (`space_type_id`) REFERENCES `General_space_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_address`
--

LOCK TABLES `General_address` WRITE;
/*!40000 ALTER TABLE `General_address` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_material`
--

DROP TABLE IF EXISTS `General_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `material_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `General_material_6965c408` (`material_type_id`),
  CONSTRAINT `material_type_id_refs_artwork_type_id_c95cd6a1` FOREIGN KEY (`material_type_id`) REFERENCES `General_material_type` (`artwork_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_material`
--

LOCK TABLES `General_material` WRITE;
/*!40000 ALTER TABLE `General_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_unit`
--

DROP TABLE IF EXISTS `General_unit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_unit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `unit_type_id` int(11) DEFAULT NULL,
  `code` varchar(4) DEFAULT NULL,
  `rel_region_id` int(11) DEFAULT NULL,
  `rel_human_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `General_unit_0f371b60` (`unit_type_id`),
  KEY `General_unit_0db5aa19` (`rel_region_id`),
  KEY `General_unit_68c93ee4` (`rel_human_id`),
  CONSTRAINT `unit_type_id_refs_artwork_type_id_5cc88dc7` FOREIGN KEY (`unit_type_id`) REFERENCES `General_unit_type` (`artwork_type_id`),
  CONSTRAINT `rel_human_id_refs_id_5eaaaa15` FOREIGN KEY (`rel_human_id`) REFERENCES `General_human` (`id`),
  CONSTRAINT `rel_region_id_refs_id_c4f5f71c` FOREIGN KEY (`rel_region_id`) REFERENCES `General_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_unit`
--

LOCK TABLES `General_unit` WRITE;
/*!40000 ALTER TABLE `General_unit` DISABLE KEYS */;
INSERT INTO `General_unit` VALUES (1,'EcoCoop',17,'eco',2,2),(2,'Euro',18,'€',NULL,NULL);
/*!40000 ALTER TABLE `General_unit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_human_jobs`
--

DROP TABLE IF EXISTS `General_human_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_human_jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `human_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `human_id` (`human_id`,`job_id`),
  KEY `General_human_jobs_6922ec88` (`human_id`),
  KEY `General_human_jobs_218f3960` (`job_id`),
  CONSTRAINT `human_id_refs_id_3c4470a7` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`),
  CONSTRAINT `job_id_refs_art_id_36244d85` FOREIGN KEY (`job_id`) REFERENCES `General_job` (`art_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_human_jobs`
--

LOCK TABLES `General_human_jobs` WRITE;
/*!40000 ALTER TABLE `General_human_jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_human_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_record`
--

DROP TABLE IF EXISTS `General_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `record_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `General_record_ac580b38` (`record_type_id`),
  CONSTRAINT `record_type_id_refs_artwork_type_id_bf922724` FOREIGN KEY (`record_type_id`) REFERENCES `General_record_type` (`artwork_type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_record`
--

LOCK TABLES `General_record` WRITE;
/*!40000 ALTER TABLE `General_record` DISABLE KEYS */;
INSERT INTO `General_record` VALUES (1,'COOP0111',39),(2,'Ecocoop -> Euro',41),(3,'COOP0111',39);
/*!40000 ALTER TABLE `General_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_company`
--

DROP TABLE IF EXISTS `General_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_company` (
  `human_id` int(11) NOT NULL,
  `legal_name` varchar(40) DEFAULT NULL,
  `vat_number` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`human_id`),
  CONSTRAINT `human_id_refs_id_ae2f98d3` FOREIGN KEY (`human_id`) REFERENCES `General_human` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_company`
--

LOCK TABLES `General_company` WRITE;
/*!40000 ALTER TABLE `General_company` DISABLE KEYS */;
/*!40000 ALTER TABLE `General_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_project_type`
--

DROP TABLE IF EXISTS `General_project_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_project_type` (
  `being_type_id` int(11) NOT NULL,
  PRIMARY KEY (`being_type_id`),
  CONSTRAINT `being_type_id_refs_typ_id_a90a2e07` FOREIGN KEY (`being_type_id`) REFERENCES `General_being_type` (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_project_type`
--

LOCK TABLES `General_project_type` WRITE;
/*!40000 ALTER TABLE `General_project_type` DISABLE KEYS */;
INSERT INTO `General_project_type` VALUES (8),(9),(10),(24),(25),(26),(27),(28),(29),(30),(31),(32),(33),(46);
/*!40000 ALTER TABLE `General_project_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_concept`
--

DROP TABLE IF EXISTS `General_concept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_concept` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` longtext NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `General_concept_410d0aac` (`parent_id`),
  KEY `General_concept_329f6fb3` (`lft`),
  KEY `General_concept_e763210f` (`rght`),
  KEY `General_concept_ba470c4a` (`tree_id`),
  KEY `General_concept_20e079f4` (`level`),
  CONSTRAINT `parent_id_refs_id_9ec027ea` FOREIGN KEY (`parent_id`) REFERENCES `General_concept` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_concept`
--

LOCK TABLES `General_concept` WRITE;
/*!40000 ALTER TABLE `General_concept` DISABLE KEYS */;
INSERT INTO `General_concept` VALUES (1,'Tipus','',NULL,1,84,1,0),(2,'Entitat','',1,2,43,1,1),(3,'Espai','',1,44,55,1,1),(4,'Obra','',1,56,83,1,1),(5,'Humà','',2,3,42,1,2),(6,'Persona','',5,4,5,1,3),(7,'Projecte','',5,6,35,1,3),(8,'Cooperativa Integral','',28,25,26,1,6),(9,'Ecoxarxa','',28,23,24,1,6),(10,'Nucli d\'Autogestió Local','',28,21,22,1,6),(11,'Regió','',3,45,52,1,2),(12,'Adreça','',3,53,54,1,2),(13,'Registre','',4,57,68,1,2),(14,'Moneda','',42,74,81,1,3),(15,'Material','',4,69,70,1,2),(16,'Inmaterial','',4,71,72,1,2),(17,'Moneda Social','',14,75,76,1,4),(18,'Moneda Fiat','',14,77,78,1,4),(19,'Criptomoneda','',14,79,80,1,4),(24,'Autoocupat','',46,8,9,1,5),(25,'Autoocupat Firaire','',46,10,11,1,5),(26,'PAIC amb facturació','',46,12,13,1,5),(27,'Projecte de Serveis','',46,14,15,1,5),(28,'Públic','',46,16,27,1,5),(29,'Cooperatiu Col·lectiu','',46,28,29,1,5),(30,'Grup de Consum','',46,30,31,1,5),(31,'Servei Comú','',28,17,18,1,6),(32,'Productiu Public','',28,19,20,1,6),(33,'PAIC sense facturació','',46,32,33,1,5),(34,'Empresa','',5,36,41,1,3),(35,'Bancaria','',34,37,38,1,4),(36,'Continent','',11,46,47,1,3),(37,'Bioregió','',11,48,49,1,3),(38,'Comarca','',11,50,51,1,3),(39,'Compte iCES','',43,61,62,1,4),(40,'Compte Bancari','',43,63,64,1,4),(41,'Equivalencia d\'Unitats','',13,58,59,1,3),(42,'Unitat','',4,73,82,1,2),(43,'Compte monetari','',13,60,67,1,3),(44,'Compte CES','',43,65,66,1,4),(45,'Cooperativa','',34,39,40,1,4),(46,'projecte CIC','',7,7,34,1,4);
/*!40000 ALTER TABLE `General_concept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_artwork_type`
--

DROP TABLE IF EXISTS `General_artwork_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_artwork_type` (
  `typ_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`typ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_artwork_type`
--

LOCK TABLES `General_artwork_type` WRITE;
/*!40000 ALTER TABLE `General_artwork_type` DISABLE KEYS */;
INSERT INTO `General_artwork_type` VALUES (13),(14),(15),(16),(17),(18),(19),(39),(40),(41),(42),(43),(44);
/*!40000 ALTER TABLE `General_artwork_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_type`
--

DROP TABLE IF EXISTS `General_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_type` (
  `concept_id` int(11) NOT NULL,
  `clas` varchar(30) NOT NULL,
  PRIMARY KEY (`concept_id`),
  CONSTRAINT `concept_id_refs_id_3c7307d7` FOREIGN KEY (`concept_id`) REFERENCES `General_concept` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_type`
--

LOCK TABLES `General_type` WRITE;
/*!40000 ALTER TABLE `General_type` DISABLE KEYS */;
INSERT INTO `General_type` VALUES (2,'Being'),(3,'Space'),(4,'Artwork'),(5,'Human'),(6,'Person'),(7,'Project'),(8,''),(9,''),(10,''),(11,'Region'),(12,'Address'),(13,'Record'),(14,''),(15,'Material'),(16,'Nonmaterial'),(17,''),(18,''),(19,''),(24,'Self-employed'),(25,''),(26,''),(27,''),(28,''),(29,''),(30,''),(31,''),(32,''),(33,''),(34,'Company'),(35,''),(36,''),(37,''),(38,''),(39,'AccountCes'),(40,'AccountBank'),(41,'UnitRatio'),(42,'Unit'),(43,''),(44,'AccountCes'),(45,''),(46,'');
/*!40000 ALTER TABLE `General_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `General_art`
--

DROP TABLE IF EXISTS `General_art`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `General_art` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `verb` varchar(30) NOT NULL,
  `gerund` varchar(30) NOT NULL,
  `description` longtext NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `General_art_410d0aac` (`parent_id`),
  KEY `General_art_329f6fb3` (`lft`),
  KEY `General_art_e763210f` (`rght`),
  KEY `General_art_ba470c4a` (`tree_id`),
  KEY `General_art_20e079f4` (`level`),
  CONSTRAINT `parent_id_refs_id_efcf9409` FOREIGN KEY (`parent_id`) REFERENCES `General_art` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `General_art`
--

LOCK TABLES `General_art` WRITE;
/*!40000 ALTER TABLE `General_art` DISABLE KEYS */;
INSERT INTO `General_art` VALUES (1,'Relació','relacionar','relacionant','',NULL,1,4,1,0),(2,'Ofici','fer','fent','',NULL,1,2,2,0),(3,'Membresia','formar part','formant part','',1,2,3,1,1);
/*!40000 ALTER TABLE `General_art` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-07-23 10:15:41
