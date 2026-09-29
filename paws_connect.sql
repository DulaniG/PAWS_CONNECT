CREATE DATABASE  IF NOT EXISTS `paws_connect` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `paws_connect`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: paws_connect
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `accounts_notification`
--

DROP TABLE IF EXISTS `accounts_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification_type` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `target_url` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_notification_user_id_30e6cfc5_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `accounts_notification_user_id_30e6cfc5_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_notification`
--

LOCK TABLES `accounts_notification` WRITE;
/*!40000 ALTER TABLE `accounts_notification` DISABLE KEYS */;
INSERT INTO `accounts_notification` VALUES (1,'ACCOUNT_SAFETY_REPORT','New Account Safety Report','shelter_test_01 reported rescuer_test_01. Reason: Suspicious Behaviour.','/admin/accounts/userreport/',1,'2026-06-30 17:45:01.888361',1),(2,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Final priority: Medium.','/rescue/my-reports/4/',1,'2026-07-01 16:28:45.561151',2),(3,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-01 17:26:33.322327',4),(4,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-01 17:26:33.322327',5),(5,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Medium.','/rescue/shelter/reports/',1,'2026-07-03 13:52:01.821313',4),(6,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-03 13:52:01.826314',5),(7,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Final priority: Medium.','/rescue/my-reports/6/',1,'2026-07-03 13:55:34.656383',2),(8,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: Medium.','/rescue/rescuer/cases/6/',1,'2026-07-03 15:08:49.619201',3),(9,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/6/',1,'2026-07-03 15:08:49.669572',2),(10,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/6/',1,'2026-07-03 16:18:39.410837',2),(11,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/6/',1,'2026-07-03 16:18:39.428450',4),(12,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Rescued.','/rescue/my-reports/6/',1,'2026-07-03 16:36:38.906256',2),(13,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Rescued.','/rescue/shelter/reports/6/',1,'2026-07-03 16:36:38.908506',4),(14,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/6/',1,'2026-07-03 16:42:27.756058',2),(15,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/reports/6/',1,'2026-07-03 16:42:27.761786',4),(16,'TREATMENT_UPDATE','Treatment Status Updated','The treatment status for your reported animal has been updated to Under Treatment.','/rescue/my-reports/6/',1,'2026-07-03 17:00:06.394889',2),(17,'TREATMENT_UPDATE','Treatment Status Updated','The treatment status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/6/',1,'2026-07-03 17:10:23.130884',2),(18,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Test Dog -Tommy.','/rescue/shelter/adoption-requests/2/',1,'2026-07-03 17:14:32.126030',4),(19,'ADOPTION_DECISION','Adoption Request Approved','Your adoption request for Test Dog -Tommy has been approved. Please open the request details to view adoption handover information.','/rescue/my-adoption-requests/2/',1,'2026-07-03 17:26:17.207256',2),(20,'ACCOUNT_SAFETY_REPORT','New Account Safety Report','shelter_test_01 reported rescuer_test_01. Reason: Suspicious Behaviour.','/admin/accounts/userreport/',1,'2026-07-04 10:56:59.299267',1),(21,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: High.','/rescue/rescuer/cases/1/',1,'2026-07-05 18:09:06.915752',3),(22,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/1/',1,'2026-07-05 18:09:06.929803',2),(23,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/1/',1,'2026-07-05 18:11:09.115969',2),(24,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/1/',1,'2026-07-05 18:11:09.120124',4),(25,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Rescued.','/rescue/my-reports/1/',1,'2026-07-05 22:02:13.094526',2),(26,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Rescued.','/rescue/shelter/reports/1/',1,'2026-07-05 22:02:13.100477',4),(27,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Final priority: Low.','/rescue/my-reports/5/',1,'2026-07-06 11:28:38.102986',2),(28,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/1/',1,'2026-07-06 12:36:44.313922',2),(29,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/reports/1/',1,'2026-07-06 12:36:44.337650',4),(30,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: Medium.','/rescue/rescuer/cases/4/',1,'2026-07-06 12:42:40.164514',3),(31,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/4/',1,'2026-07-06 12:42:40.164514',2),(32,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-06 14:15:50.822140',4),(33,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-06 14:15:50.839881',5),(34,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Final priority: Low.','/rescue/my-reports/7/',1,'2026-07-06 14:32:11.498383',2),(35,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: Low.','/rescue/rescuer/cases/5/',1,'2026-07-06 15:13:10.953211',3),(36,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/5/',1,'2026-07-06 15:13:10.972585',2),(37,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: Low.','/rescue/rescuer/cases/5/',1,'2026-07-06 15:14:13.049348',3),(38,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/5/',1,'2026-07-06 15:14:13.049737',2),(39,'CASE_ASSIGNED','Rescue Case Reassigned','A rescue case has been reassigned to you by shelter_test_01. Priority: Low.','/rescue/rescuer/cases/5/',1,'2026-07-06 16:44:52.014652',7),(40,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Current rescue status: Not Started.','/rescue/my-reports/5/',1,'2026-07-06 16:44:52.019402',2),(41,'CASE_ASSIGNED','Rescue Case Reassigned','This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',1,'2026-07-06 17:42:03.173848',7),(42,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Priority: Low.','/rescue/rescuer/cases/5/',1,'2026-07-06 17:42:03.173848',3),(43,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Current rescue status: Not Started.','/rescue/my-reports/5/',1,'2026-07-06 17:42:03.187804',2),(44,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/5/',1,'2026-07-06 17:59:19.724080',2),(45,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/5/',1,'2026-07-06 17:59:19.724080',4),(46,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Rescued.','/rescue/my-reports/5/',1,'2026-07-06 18:02:48.041867',2),(47,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Rescued.','/rescue/shelter/reports/5/',1,'2026-07-06 18:02:48.049166',4),(48,'RESCUE_UPDATE','Rescue Status Updated','The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/5/',1,'2026-07-06 18:03:16.081114',2),(49,'RESCUE_UPDATE','Rescue Case Updated','Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/reports/5/',1,'2026-07-06 18:03:16.081114',4),(50,'TREATMENT_UPDATE','Treatment Status Updated','The treatment status for your reported animal has been updated to Under Treatment.','/rescue/my-reports/5/',1,'2026-07-07 11:35:12.278905',2),(51,'TREATMENT_UPDATE','Treatment Status Updated','The treatment status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/5/',1,'2026-07-07 18:01:35.553902',2),(52,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Puppy Test.','/rescue/shelter/adoption-requests/3/',1,'2026-07-07 18:46:25.310842',4),(53,'ADOPTION_DECISION','Adoption Request Approved','Your adoption request for Puppy Test has been approved. Please open the request details to view adoption handover information.','/rescue/my-adoption-requests/3/',1,'2026-07-08 06:32:59.639869',2),(54,'ACCOUNT_SAFETY_REPORT','New Account Safety Report','public_test_01 reported shelter_test_01. Reason: Suspicious Behaviour.','/admin/accounts/userreport/',1,'2026-07-08 07:14:47.783919',1),(55,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-08 16:02:46.777587',4),(56,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-08 16:02:46.826029',5),(57,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-08 16:02:46.844203',8),(58,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-08 17:12:13.328919',4),(59,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-08 17:12:13.331129',5),(60,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-08 17:12:13.346760',8),(61,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by Demo Shelter 02. Final priority: Low.','/rescue/my-reports/9/',1,'2026-07-08 17:34:39.936207',2),(62,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Medium.','/rescue/shelter/reports/',1,'2026-07-09 17:44:33.428041',4),(63,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-09 17:44:33.511348',5),(64,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-09 17:44:33.541458',8),(65,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Final priority: Medium.','/rescue/my-reports/10/',1,'2026-07-09 18:06:59.879342',2),(66,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Priority: Medium.','/rescue/rescuer/cases/10/',1,'2026-07-09 18:23:34.566139',3),(67,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Current rescue status: Not Started.','/rescue/my-reports/10/',1,'2026-07-09 18:23:34.599475',2),(68,'CASE_ASSIGNED','Rescue Case Reassigned','Report ID: #10. This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',1,'2026-07-10 13:35:54.302238',3),(69,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Report ID: #10. Priority: Medium.','/rescue/rescuer/cases/10/',1,'2026-07-10 13:35:54.306048',7),(70,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Report ID: #10. Current rescue status: Not Started.','/rescue/my-reports/10/',1,'2026-07-10 13:35:54.320879',2),(71,'CASE_ASSIGNED','Rescue Case Reassigned','Report ID: #10. This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',1,'2026-07-10 13:37:05.182744',7),(72,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Report ID: #10. Priority: Medium.','/rescue/rescuer/cases/10/',1,'2026-07-10 13:37:05.199716',3),(73,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Report ID: #10. Current rescue status: Not Started.','/rescue/my-reports/10/',1,'2026-07-10 13:37:05.199716',2),(74,'CASE_ASSIGNED','Rescue Case Reassigned','Report ID: #10. This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',1,'2026-07-10 13:44:07.502397',3),(75,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Report ID: #10. Priority: Medium.','/rescue/rescuer/cases/10/',1,'2026-07-10 13:44:07.503462',7),(76,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Report ID: #10. Current rescue status: Not Started.','/rescue/my-reports/10/',1,'2026-07-10 13:44:07.514343',2),(77,'CASE_ASSIGNED','Rescue Case Reassigned','Report ID: #10. This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',1,'2026-07-10 13:45:14.058395',7),(78,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Report ID: #10. Priority: Medium.','/rescue/rescuer/cases/10/',1,'2026-07-10 13:45:14.058395',3),(79,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Report ID: #10. Current rescue status: Not Started.','/rescue/my-reports/10/',1,'2026-07-10 13:45:14.077454',2),(80,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #10. The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/10/',1,'2026-07-10 17:25:17.255874',2),(81,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #10. Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/10/',1,'2026-07-10 17:25:17.271180',4),(82,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #10. The rescue status for your animal report was updated to Rescued.','/rescue/my-reports/10/',1,'2026-07-10 17:32:39.880984',2),(83,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #10. Rescuer Test User updated the rescue case status to Rescued.','/rescue/shelter/reports/10/',1,'2026-07-10 17:32:39.892972',4),(84,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #10. The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/10/',1,'2026-07-10 17:36:55.511564',2),(85,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #10. Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/treatment/10/',1,'2026-07-10 17:36:55.518563',4),(86,'TREATMENT_UPDATE','Treatment Status Updated','Report ID: #10. The treatment status for your reported animal has been updated to Under Treatment.','/rescue/my-reports/10/',1,'2026-07-11 15:45:16.285153',2),(87,'TREATMENT_UPDATE','Treatment Status Updated','Report ID: #10. The treatment status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/10/',1,'2026-07-11 16:27:32.464965',2),(88,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Brownie.Report ID: #10.','/rescue/shelter/adoption-requests/4/',1,'2026-07-11 16:59:31.155612',4),(89,'ADOPTION_DECISION','Adoption Request Approved','Your adoption request for Brownie has been approved. Report ID: #10. Please open the request details to view adoption handover information.','/rescue/my-adoption-requests/4/',1,'2026-07-11 18:01:21.370813',2),(90,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #11. Suggested priority: Medium.','/rescue/shelter/reports/',1,'2026-07-14 17:16:20.771882',4),(91,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #11. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-14 17:16:20.791249',5),(92,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #11. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-14 17:16:20.791838',8),(93,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #11. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-14 17:16:20.791838',10),(94,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #11. Suggested priority: Medium.','/rescue/shelter/reports/',0,'2026-07-14 17:16:20.806761',12),(95,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Report ID: #11. Verification status: Animal Not Found / Moved. Final priority: Low.','/rescue/my-reports/11/',1,'2026-07-14 17:49:48.368318',2),(96,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #12. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-15 16:57:35.639055',4),(97,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #12. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 16:57:35.642141',5),(98,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #12. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 16:57:35.642141',8),(99,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #12. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 16:57:35.660662',10),(100,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #12. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 16:57:35.660662',12),(101,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Report ID: #12. Verification status: Animal Not Found. Final priority: Low.','/rescue/my-reports/12/',1,'2026-07-15 17:00:38.987316',2),(102,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #4. The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/4/',1,'2026-07-15 19:45:05.882719',2),(103,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #4. Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/4/',1,'2026-07-15 19:45:05.900262',4),(104,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #13. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-15 20:54:01.311434',4),(105,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #13. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 20:54:01.311434',5),(106,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #13. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 20:54:01.327143',8),(107,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #13. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 20:54:01.328203',10),(108,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #13. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-15 20:54:01.328203',12),(109,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Report ID: #13. Verification status: Already Rescued. Final priority: Low.','/rescue/my-reports/13/',1,'2026-07-15 20:59:09.463948',2),(110,'TREATMENT_UPDATE','Animal Care Status Updated','Report ID: #1. The animal care status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/1/',1,'2026-07-16 03:13:48.725257',2),(111,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Bobby.Report ID: #1.','/rescue/shelter/adoption-requests/5/',1,'2026-07-16 03:17:29.522075',4),(112,'ADOPTION_DECISION','Adoption Request Rejected','Your adoption request for Bobby has been rejected by the shelter. Report ID: #1.','/rescue/my-adoption-requests/5/',1,'2026-07-16 04:15:34.694589',2),(113,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Report ID: #7. Priority: Low.','/rescue/rescuer/cases/7/',0,'2026-07-17 06:16:14.685514',9),(114,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Report ID: #7. Current rescue status: Not Started.','/rescue/my-reports/7/',1,'2026-07-17 06:16:14.724690',2),(115,'ACCOUNT_SAFETY_REPORT','New Account Safety Report','shelter_test_01 reported rescuer_approval_demo_01. Reason: Not Actually Linked to Selected Shelter.','/admin/accounts/userreport/',1,'2026-07-17 06:17:44.214036',1),(116,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #14. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-18 13:17:41.024905',4),(117,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #14. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 13:17:41.064757',5),(118,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #14. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 13:17:41.071426',8),(119,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #14. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 13:17:41.076425',10),(120,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #14. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 13:17:41.086667',12),(121,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #15. Suggested priority: Low.','/rescue/shelter/reports/',1,'2026-07-18 15:57:16.435088',4),(122,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #15. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 15:57:16.454714',5),(123,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #15. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 15:57:16.458709',8),(124,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #15. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 15:57:16.463710',10),(125,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #15. Suggested priority: Low.','/rescue/shelter/reports/',0,'2026-07-18 15:57:16.470022',12),(126,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Report ID: #14. Verification status: Confirmed Still There. Final priority: Low.','/rescue/my-reports/14/',1,'2026-07-18 17:32:29.157659',2),(127,'CASE_ASSIGNED','New Rescue Case Assigned','A new rescue case has been assigned to you by shelter_test_01. Report ID: #14. Priority: Low.','/rescue/rescuer/cases/14/',1,'2026-07-18 17:36:23.069151',3),(128,'CASE_ASSIGNED','Rescue Case Assigned','Your animal report has been assigned to a rescuer. Report ID: #14. Current rescue status: Not Started.','/rescue/my-reports/14/',1,'2026-07-18 17:36:23.080922',2),(129,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #14. The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/14/',1,'2026-07-18 17:46:33.384573',2),(130,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #14. Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/14/',1,'2026-07-18 17:46:33.400129',4),(131,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #14. The rescue status for your animal report was updated to Rescued.','/rescue/my-reports/14/',1,'2026-07-18 17:48:53.266370',2),(132,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #14. Rescuer Test User updated the rescue case status to Rescued.','/rescue/shelter/reports/14/',1,'2026-07-18 17:48:53.272375',4),(133,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #14. The rescue status for your animal report was updated to On the Way.','/rescue/my-reports/14/',1,'2026-07-18 17:51:56.170785',2),(134,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #14. Rescuer Test User updated the rescue case status to On the Way.','/rescue/shelter/reports/14/',1,'2026-07-18 17:51:56.170785',4),(135,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #14. The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/14/',1,'2026-07-18 17:52:45.002961',2),(136,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #14. Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/reports/14/',1,'2026-07-18 17:52:45.018360',4),(137,'TREATMENT_UPDATE','Animal Care Status Updated','Report ID: #14. The animal care status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/14/',1,'2026-07-18 18:03:30.394983',2),(138,'ADOPTION_REQUEST','New Adoption Request','Rescuer Test User submitted an adoption request for Puppy russel.Report ID: #14.','/rescue/shelter/adoption-requests/6/',1,'2026-07-18 18:14:26.216053',4),(139,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Puppy russel.Report ID: #14.','/rescue/shelter/adoption-requests/7/',1,'2026-07-18 18:18:50.079014',4),(140,'ADOPTION_DECISION','Adoption Request Rejected','Your adoption request for Puppy russel was rejected because another request was approved. Report ID: #14.','/rescue/my-adoption-requests/7/',1,'2026-07-18 18:38:20.524079',2),(141,'ADOPTION_DECISION','Adoption Request Approved','Your adoption request for Puppy russel has been approved. Report ID: #14. Please open the request details to view adoption handover information.','/rescue/my-adoption-requests/6/',1,'2026-07-18 18:38:20.540700',3),(142,'CASE_ASSIGNED','Rescue Case Reassigned','Report ID: #7. This rescue case has been reassigned and removed from your active cases.','/rescue/rescuer/cases/',0,'2026-07-19 06:34:00.104007',9),(143,'CASE_ASSIGNED','Rescue Case Assigned','A rescue case has been assigned to you by shelter_test_01. Report ID: #7. Priority: Low.','/rescue/rescuer/cases/7/',0,'2026-07-19 06:34:00.126377',11),(144,'CASE_ASSIGNED','Rescue Case Reassigned','Your animal rescue case has been reassigned to another rescuer. Report ID: #7. Current rescue status: Not Started.','/rescue/my-reports/7/',1,'2026-07-19 06:34:00.137559',2),(145,'REPORT_REVIEWED','Animal Report Reviewed','Your animal report has been reviewed by shelter_test_01. Report ID: #15. Verification status: Confirmed Still There. Final priority: Low.','/rescue/my-reports/15/',1,'2026-07-19 06:34:39.186789',2),(146,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #16. Suggested priority: High.','/rescue/shelter/reports/',1,'2026-07-21 08:56:06.861986',4),(147,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #16. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 08:56:06.901557',5),(148,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #16. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 08:56:06.916703',8),(149,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #16. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 08:56:06.921698',10),(150,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #16. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 08:56:06.928663',12),(151,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #17. Suggested priority: High.','/rescue/shelter/reports/',1,'2026-07-21 09:06:03.963223',4),(152,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #17. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 09:06:03.967300',5),(153,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #17. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 09:06:03.985467',8),(154,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #17. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 09:06:04.001758',10),(155,'REPORT_REVIEWED','New Animal Report Submitted','A new animal report has been submitted by Public Test User. Report ID: #17. Suggested priority: High.','/rescue/shelter/reports/',0,'2026-07-21 09:06:04.007756',12),(156,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Bobby.Report ID: #1.','/rescue/shelter/adoption-requests/8/',1,'2026-07-21 11:07:52.892824',4),(157,'ADOPTION_DECISION','Adoption Request Rejected','Your adoption request for Bobby has been rejected by the shelter. Report ID: #1.','/rescue/my-adoption-requests/8/',1,'2026-07-21 11:10:32.394448',2),(158,'ADOPTION_REQUEST','New Adoption Request','Public Test User submitted an adoption request for Bobby.Report ID: #1.','/rescue/shelter/adoption-requests/9/',1,'2026-07-21 11:12:04.223143',4),(159,'RESCUE_UPDATE','Rescue Status Updated','Report ID: #4. The rescue status for your animal report was updated to Handed Over to Shelter.','/rescue/my-reports/4/',1,'2026-07-28 18:49:42.511820',2),(160,'RESCUE_UPDATE','Rescue Case Updated','Report ID: #4. Rescuer Test User updated the rescue case status to Handed Over to Shelter.','/rescue/shelter/reports/4/',1,'2026-07-28 18:49:42.524505',4),(161,'TREATMENT_UPDATE','Animal Care Status Updated','Report ID: #4. The animal care status for your reported animal has been updated to Ready for Adoption.','/rescue/my-reports/4/',1,'2026-07-28 18:51:27.454238',2);
/*!40000 ALTER TABLE `accounts_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `full_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `account_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `service_area` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `linked_shelter_id` bigint DEFAULT NULL,
  `shelter_address` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `shelter_map_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `accounts_user_linked_shelter_id_be68f2d8_fk_accounts_user_id` (`linked_shelter_id`),
  CONSTRAINT `accounts_user_linked_shelter_id_be68f2d8_fk_accounts_user_id` FOREIGN KEY (`linked_shelter_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (1,'pbkdf2_sha256$1000000$kTU9PLZQIKCl5If2Z1HaJB$evQBDvC4JEnjQsUIxXGoYuN6QF2SNYlliGQLU7jEcRU=','2026-07-29 07:01:41.269501',1,'admin','','',1,1,'2026-06-16 14:46:47.538702','','dulanigelanigamage@gmail.com','','ADMIN','APPROVED','',NULL,'',''),(2,'pbkdf2_sha256$1000000$bgvFVKVj5LEr41meaccYIU$DwnQ9mN6JPjniLkfhnplvSIdEfA1RhwX00PTCNMLgXQ=','2026-07-31 19:48:00.356670',0,'public_test_01','','',0,1,'2026-06-17 11:35:13.882405','Public Test User','public.test01@test.com','0712345678','PUBLIC','APPROVED','',NULL,'',''),(3,'pbkdf2_sha256$1000000$HYNAsA2Nbc98O7l69wmpG6$Zi6OYkB9vnzE0XvtkzHR0xfCzXjO75dXDHhEgTrVYwg=','2026-07-28 19:40:16.163482',0,'rescuer_test_01','','',0,1,'2026-06-17 11:46:46.000000','Rescuer Test User','rescuer.test01@test.com','0771234567','RESCUER','APPROVED','',4,'',''),(4,'pbkdf2_sha256$1000000$TKUGwhsicbLEQHv5yIQYVt$E4YORIznXUAwrXzfs10xIZbggiOgfBMBpWYR+I3heUA=','2026-07-31 19:54:30.685722',0,'shelter_test_01','','',0,1,'2026-06-17 15:53:20.000000','shelter_test_01','shelter.validation@test.com','0777771234','SHELTER','APPROVED','Makumbura / Kottawa / Maharagama',NULL,'No. 25, Main Road, Maharagama','https://maps.app.goo.gl/LkvrPt8yo9zTubDL9'),(5,'pbkdf2_sha256$1000000$4rvtph2x7FGoobBQke5fTe$noWJdDsC3ECYls5A7tscScFvADc1kUfiuq04RjHu5S4=',NULL,0,'shelter_demo_01','','',0,1,'2026-06-21 19:58:56.326314','Demo Shelter','shelterdemo01@example.com','0112345678','SHELTER','APPROVED','Nugegoda / Maharagama',NULL,'No. 10, Demo Road, Maharagama','https://maps.google.com/?q=Maharagama'),(6,'pbkdf2_sha256$1000000$pu4H9H86NSF0XqJCsfbROW$e75qvk0xCoEY4Svwhm6hpECR3UyhLZdsd8W7U1XQcdw=',NULL,0,'rescuer_demo_01','','',0,1,'2026-06-21 20:09:22.812120','Demo Rescuer','rescuerdemo01@example.com','0771111111','RESCUER','APPROVED','',5,'',''),(7,'pbkdf2_sha256$1000000$qAzOSmVcfZols3Px134tRG$t5pfIh5nW8DWPTH19oS6eemFJvyyFK2039zTt7YSB20=','2026-07-12 08:16:50.517236',0,'rescuer_test_02','','',0,1,'2026-07-06 16:00:34.000000','rescuer_test_02','RescuerTest02@gmail.com','0789012345','RESCUER','APPROVED','',4,'',''),(8,'pbkdf2_sha256$1000000$yVhI722DiYfR728GrDinGE$mA2YX9/NflUG1nB0ib4vJPUPBX8C+H6MHFcfWtjnShA=','2026-07-08 18:46:52.168222',0,'shelter_demo_02','','',0,1,'2026-07-08 15:49:50.000000','Demo Shelter 02','ShelterDemo02@gmail.com','0798756234','SHELTER','APPROVED','Jaffna / Nallur / Chunnakam',NULL,'160 Hospital Rd, Jaffna','https://maps.app.goo.gl/oULTfC2U491Jewu56'),(9,'pbkdf2_sha256$1000000$OLyllBJ0BL5Itu9wmN3hzG$9c5RnzaloDYz40NX5BPFKFYzFPCVJk87rVj7nvFJXxk=','2026-07-17 09:45:00.000000',0,'rescuer_approval_demo_01','','',0,1,'2026-07-12 07:50:22.000000','Rescuer Approval Demo','rescuer.approval.demo@test.com','0761112222','RESCUER','APPROVED','',4,'',''),(10,'pbkdf2_sha256$1000000$Gb5BDbCoOGTF9LBwT3AhFS$poUyRWnWtY1KYgwQ3uvMKUi4g6309xmL/VflXliqTDA=','2026-07-13 22:16:45.477085',0,'shelter_approval_demo_01','','',0,1,'2026-07-12 12:02:12.000000','Shelter Approval Demo','shelter.approval.demo@test.com','0772223333','SHELTER','APPROVED','Kadawatha / Kiribathgoda / Kelaniya',NULL,'Shelter Approval Demo, High Level Road, Kadawatha , Sri Lanka','https://maps.app.goo.gl/DRafKEdVtipqCnLg8'),(11,'pbkdf2_sha256$1000000$VPYkNBJpLbndlvTQ9cQeol$ayrFgoiBr8oFjUhpCMEiXnXHv9boW9M0W9xvDaEZdhs=',NULL,0,'rescuer_email_demo_01','','',0,1,'2026-07-13 11:24:09.000000','rescuer_email_demo_01','rescuer_email_demo_01@gmail.com','0723777777','RESCUER','APPROVED','',4,'',''),(12,'pbkdf2_sha256$1000000$GWrHuOSidJabdnvDShBj2t$CDgDm3fFOskniExWPYZkogxpkaEI6JR6GJu+hmf6kqM=',NULL,0,'shelter_email_demo_01','','',0,1,'2026-07-13 11:30:26.000000','shelter_email_demo_01','shelter_email_demo_01@gmail.com','0777771111','SHELTER','APPROVED','Nugegoda / Maharagama',NULL,'No. 25, Main Road, Nugegoda','https://maps.app.goo.gl/dLGTKEb7a7o3SiGc6'),(13,'pbkdf2_sha256$1000000$zIQAM3Sug99Osewe4FtC2I$QqE2rsuiNueXs0DBbukZnylci6CXSI8xXIqW5Dlt27w=','2026-07-17 03:01:50.103525',0,'rescuer_test_03','','',0,1,'2026-07-17 02:46:48.000000','rescuer_test_03','rescuer_test_03@gmail.com','0777711223','RESCUER','APPROVED','',8,'','');
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_groups`
--

DROP TABLE IF EXISTS `accounts_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`),
  CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_groups`
--

LOCK TABLES `accounts_user_groups` WRITE;
/*!40000 ALTER TABLE `accounts_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_user_permissions`
--

DROP TABLE IF EXISTS `accounts_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`),
  CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_user_permissions`
--

LOCK TABLES `accounts_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_userreport`
--

DROP TABLE IF EXISTS `accounts_userreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_userreport` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `reason` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `related_page` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `admin_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `reviewed_at` datetime(6) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `reported_by_id` bigint NOT NULL,
  `reported_user_id` bigint NOT NULL,
  `reviewed_by_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_userreport_reported_by_id_54e5f272_fk_accounts_user_id` (`reported_by_id`),
  KEY `accounts_userreport_reported_user_id_434b5e7c_fk_accounts_` (`reported_user_id`),
  KEY `accounts_userreport_reviewed_by_id_998f64d8_fk_accounts_user_id` (`reviewed_by_id`),
  CONSTRAINT `accounts_userreport_reported_by_id_54e5f272_fk_accounts_user_id` FOREIGN KEY (`reported_by_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `accounts_userreport_reported_user_id_434b5e7c_fk_accounts_` FOREIGN KEY (`reported_user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `accounts_userreport_reviewed_by_id_998f64d8_fk_accounts_user_id` FOREIGN KEY (`reviewed_by_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_userreport`
--

LOCK TABLES `accounts_userreport` WRITE;
/*!40000 ALTER TABLE `accounts_userreport` DISABLE KEYS */;
INSERT INTO `accounts_userreport` VALUES (1,'NOT_LINKED_TO_SHELTER','This is a test safety report to show that the shelter can report a suspicious rescuer account to the administrator for review.','/rescue/shelter/reports/3/','REVIEWED','Initial investigation completed as part of dissertation system testing. Report has been reviewed and requires no immediate enforcement action.',NULL,'2026-06-28 16:31:29.010351','2026-07-17 05:05:30.330421',4,3,NULL),(2,'SUSPICIOUS_BEHAVIOUR','This is a test notification report to check whether the administrator receives a system notification after a suspicious account report is submitted.','/rescue/shelter/reports/3/','PENDING','',NULL,'2026-06-30 17:45:01.855710','2026-06-30 17:45:01.855710',4,3,NULL),(3,'SUSPICIOUS_BEHAVIOUR','This is a test account safety report from the completed case detail page to confirm that the administrator receives a notification after the completed case layout update.','/rescue/shelter/reports/6/','PENDING','',NULL,'2026-07-04 10:56:59.239660','2026-07-04 10:56:59.239660',4,3,NULL),(4,'SUSPICIOUS_BEHAVIOUR','This is a test account safety report for dissertation testing. The shelter account is being reported to confirm that suspicious account reporting and admin notification work correctly.','/rescue/my-adoption-requests/3/','PENDING','',NULL,'2026-07-08 07:14:47.639243','2026-07-08 07:14:47.639243',2,4,NULL),(5,'NOT_LINKED_TO_SHELTER','The Rescuer is not linked to our shelter, Please remove this rescuer from our account.','/rescue/shelter/reports/7/','REVIEWED','Investigation completed during final administrator audit. Report reviewed and recorded successfully.','2026-07-17 06:25:55.824698','2026-07-17 06:17:44.198036','2026-07-17 06:25:55.824698',4,9,1);
/*!40000 ALTER TABLE `accounts_userreport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add user',1,'add_user'),(2,'Can change user',1,'change_user'),(3,'Can delete user',1,'delete_user'),(4,'Can view user',1,'view_user'),(5,'Can add log entry',2,'add_logentry'),(6,'Can change log entry',2,'change_logentry'),(7,'Can delete log entry',2,'delete_logentry'),(8,'Can view log entry',2,'view_logentry'),(9,'Can add permission',3,'add_permission'),(10,'Can change permission',3,'change_permission'),(11,'Can delete permission',3,'delete_permission'),(12,'Can view permission',3,'view_permission'),(13,'Can add group',4,'add_group'),(14,'Can change group',4,'change_group'),(15,'Can delete group',4,'delete_group'),(16,'Can view group',4,'view_group'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add report',7,'add_report'),(26,'Can change report',7,'change_report'),(27,'Can delete report',7,'delete_report'),(28,'Can view report',7,'view_report'),(29,'Can add rescue update',8,'add_rescueupdate'),(30,'Can change rescue update',8,'change_rescueupdate'),(31,'Can delete rescue update',8,'delete_rescueupdate'),(32,'Can view rescue update',8,'view_rescueupdate'),(33,'Can add animal',9,'add_animal'),(34,'Can change animal',9,'change_animal'),(35,'Can delete animal',9,'delete_animal'),(36,'Can view animal',9,'view_animal'),(37,'Can add adoption request',10,'add_adoptionrequest'),(38,'Can change adoption request',10,'change_adoptionrequest'),(39,'Can delete adoption request',10,'delete_adoptionrequest'),(40,'Can view adoption request',10,'view_adoptionrequest'),(41,'Can add User Safety Report',11,'add_userreport'),(42,'Can change User Safety Report',11,'change_userreport'),(43,'Can delete User Safety Report',11,'delete_userreport'),(44,'Can view User Safety Report',11,'view_userreport'),(45,'Can add Notification',12,'add_notification'),(46,'Can change Notification',12,'change_notification'),(47,'Can delete Notification',12,'delete_notification'),(48,'Can view Notification',12,'view_notification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-06-18 03:20:59.293327','3','Rescuer Test User - RESCUER',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(2,'2026-06-18 04:08:21.251673','4','Shelter Validation Test - SHELTER',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(3,'2026-06-18 17:39:40.059729','2','Cat report by public_test_01',3,'',7,1),(4,'2026-06-21 18:03:22.934172','4','shelter_test_01 - SHELTER',2,'[{\"changed\": {\"fields\": [\"Username\", \"Service area\", \"Shelter address\", \"Shelter map link\"]}}]',1,1),(5,'2026-06-21 18:04:20.808422','3','Rescuer Test User - RESCUER',2,'[{\"changed\": {\"fields\": [\"Linked Shelter\"]}}]',1,1),(6,'2026-06-21 20:01:37.483212','5','Demo Shelter - SHELTER',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(7,'2026-06-21 20:12:07.138180','6','Demo Rescuer - RESCUER',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(8,'2026-06-25 16:09:54.380166','4','shelter_test_01 - SHELTER',2,'[{\"changed\": {\"fields\": [\"Phone number\"]}}]',1,1),(9,'2026-07-06 16:07:11.877500','7','rescuer_test_02 (rescuer_test_02)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(10,'2026-07-08 15:52:52.387255','8','Demo Shelter 02 (shelter_demo_02)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(11,'2026-07-08 16:07:44.998102','8','Dog report by public_test_01',3,'',7,1),(12,'2026-07-09 17:34:26.123279','9','Dog report by public_test_01',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(13,'2026-07-12 11:39:42.428950','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(14,'2026-07-12 12:10:35.007251','10','Shelter Approval Demo (shelter_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(15,'2026-07-13 11:25:21.532403','11','rescuer_email_demo_01 (rescuer_email_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(16,'2026-07-13 11:34:10.110592','12','shelter_email_demo_01 (shelter_email_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(17,'2026-07-14 17:25:57.079093','11','Other report by public_test_01',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(18,'2026-07-14 17:26:20.193727','11','Other report by public_test_01',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(19,'2026-07-17 02:59:58.660547','13','rescuer_test_03 (rescuer_test_03)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(20,'2026-07-17 05:05:30.397098','1','Report against rescuer_test_01 by shelter_test_01',2,'[{\"changed\": {\"fields\": [\"Status\", \"Admin notes\"]}}]',11,1),(21,'2026-07-17 06:25:55.874631','5','Report against rescuer_approval_demo_01 by shelter_test_01',2,'[{\"changed\": {\"fields\": [\"Status\", \"Admin notes\"]}}]',11,1),(22,'2026-07-17 06:56:21.074222','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(23,'2026-07-17 07:18:02.096168','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(24,'2026-07-17 09:19:02.939005','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(25,'2026-07-17 09:22:09.210166','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(26,'2026-07-17 09:35:21.005150','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(27,'2026-07-17 09:35:51.506930','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(28,'2026-07-17 09:36:30.737625','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(29,'2026-07-17 09:39:20.895342','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(30,'2026-07-17 09:41:47.888609','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(31,'2026-07-17 09:42:01.820796','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(32,'2026-07-17 09:44:24.895896','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(33,'2026-07-17 09:45:58.561835','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(34,'2026-07-17 09:50:49.898267','9','Rescuer Approval Demo (rescuer_approval_demo_01)',2,'[{\"changed\": {\"fields\": [\"Account status\"]}}]',1,1),(35,'2026-07-18 14:03:49.786099','14','Dog report by public_test_01',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',7,1),(36,'2026-07-18 15:58:13.450571','15','Cat report by public_test_01',2,'[{\"changed\": {\"fields\": [\"Animal type\"]}}]',7,1),(37,'2026-07-21 09:04:46.414009','16','Cat report by public_test_01',3,'',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (12,'accounts','notification'),(1,'accounts','user'),(11,'accounts','userreport'),(2,'admin','logentry'),(4,'auth','group'),(3,'auth','permission'),(5,'contenttypes','contenttype'),(10,'rescue','adoptionrequest'),(9,'rescue','animal'),(7,'rescue','report'),(8,'rescue','rescueupdate'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-06-16 14:01:10.594595'),(2,'contenttypes','0002_remove_content_type_name','2026-06-16 14:01:10.798077'),(3,'auth','0001_initial','2026-06-16 14:01:11.381565'),(4,'auth','0002_alter_permission_name_max_length','2026-06-16 14:01:11.483744'),(5,'auth','0003_alter_user_email_max_length','2026-06-16 14:01:11.509064'),(6,'auth','0004_alter_user_username_opts','2026-06-16 14:01:11.522442'),(7,'auth','0005_alter_user_last_login_null','2026-06-16 14:01:11.549709'),(8,'auth','0006_require_contenttypes_0002','2026-06-16 14:01:11.562707'),(9,'auth','0007_alter_validators_add_error_messages','2026-06-16 14:01:11.590686'),(10,'auth','0008_alter_user_username_max_length','2026-06-16 14:01:11.659454'),(11,'auth','0009_alter_user_last_name_max_length','2026-06-16 14:01:11.684515'),(12,'auth','0010_alter_group_name_max_length','2026-06-16 14:01:11.728073'),(13,'auth','0011_update_proxy_permissions','2026-06-16 14:01:11.757134'),(14,'auth','0012_alter_user_first_name_max_length','2026-06-16 14:01:11.792687'),(15,'accounts','0001_initial','2026-06-16 14:01:12.583979'),(16,'admin','0001_initial','2026-06-16 14:01:12.867616'),(17,'admin','0002_logentry_remove_auto_add','2026-06-16 14:01:12.884372'),(18,'admin','0003_logentry_add_action_flag_choices','2026-06-16 14:01:12.909530'),(19,'sessions','0001_initial','2026-06-16 14:01:12.982350'),(20,'rescue','0001_initial','2026-06-18 05:49:14.263390'),(21,'rescue','0002_report_reporter_contact_phone_and_more','2026-06-18 17:08:33.035852'),(22,'rescue','0003_report_assigned_at_report_assigned_rescuer_and_more','2026-06-19 10:26:54.794973'),(23,'rescue','0004_report_current_rescue_status_rescueupdate','2026-06-20 17:58:44.380837'),(24,'accounts','0002_user_linked_shelter_user_shelter_address_and_more','2026-06-21 17:56:24.683652'),(25,'rescue','0005_alter_report_assignment_notes_and_more','2026-06-21 17:56:24.774304'),(26,'rescue','0006_animal','2026-06-22 13:26:11.856682'),(27,'rescue','0007_adoptionrequest','2026-06-24 18:06:55.566428'),(28,'accounts','0003_alter_user_account_status_alter_user_full_name_and_more','2026-06-27 17:50:07.923640'),(29,'accounts','0004_notification','2026-06-30 17:00:32.330074');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1lsjeurkt5vtb5ln7b633us3bhhj891j','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wltLT:itQ9AoV0NKh2gLqK4u2xRaPOW9H-QpYZX1xMQM62N8A','2026-08-03 19:08:07.792475'),('27z1y2del3q8ts4ne7ugtjcelputu6wa','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlt89:MkTbyETF7JRR5LANho3AMh8vamTOXMErVjL7Zo0UkgA','2026-08-03 18:54:21.549276'),('2jwlrw8xu8urcpc4qx9dwprfg6ny9iji','.eJxVjDsOwjAQBe_iGlmx409MSc8Zol3vLg4gR4qTCnF3iJQC2jcz76VG2NYybo2XcSJ1Vk6dfjeE_OC6A7pDvc06z3VdJtS7og_a9HUmfl4O9--gQCvfGi3KEHxnrQTpnaQYeuOYGF2MPXuGISVKYjoGEnaYDUoXvGEvNguo9wfwyTjS:1wptJO:E27cWFcs1n51iocuKaPtJgymS8f1kEofvyrVipQXnus','2026-08-14 19:54:30.699844'),('3wvci5upizki7oxfjbb18epg49zh9q3c','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm6GU:S7827c_i1J7tgeF97nrNrrOPHF8Gxz7VbRVKpXtiF5c','2026-08-04 08:55:50.441503'),('46sbd94biyltbnoqlxulbuwkr6k4pvkt','.eJxVjM0OwiAQhN-FsyEs5Wf16L3PQHYBpWogKe3J-O62SQ96m8z3zbxFoHUpYe15DlMSFwHi9NsxxWeuO0gPqvcmY6vLPLHcFXnQLseW8ut6uH8HhXrZ1oO1HFXMA6GyyvszOAXW4Y0ZNG7ZgFHaabIOkIxnRwqRgQ06Swji8wWl3DYJ:1woyIP:vUPA3cCgfbkW0iqL4s2J6RSTw67mLMiPglQ_FQA9ApY','2026-08-12 07:01:41.285125'),('4oif4nku0kljq5g53wf291es3kpakzhz','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wltUT:Feg4TPG4EaapHMmejPFfwXnsPTT5P0TFLaykROyzRj0','2026-08-03 19:17:25.391013'),('6shmuu7cnxa2r7n8gmszp69ft52hpp9h','.eJxVjEEOwiAQRe_C2pBCp8C4dO8ZCAODVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-TuIsRnH63SjEB9cdpHuotyZjq-syk9wVedAury3x83K4fwcl9PKtg00IhBzdZFEZdCY6RA1sATLYkBHBUiaExMYoHLLKo9aMihxONIj3B9RVN1U:1wlLnY:DSUdPd0YF5aMdqCI4ozBg1ZlwSUDvblQVeGJpFfF5c0','2026-08-02 07:18:52.574096'),('7gkq3qkik8ztdwv1t4hake8ze0zc4m0a','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm5CM:x3v_9LbArkvvnyHDhLAbgvqTGRC2poBwtb1t1Jg9NHA','2026-08-04 07:47:30.405672'),('9gtywll2lbua9p9lgi2wjxaye6zivsar','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm6Cb:750KRLes2vGosIDGYwfDK-7nBuzZM7EKn4ncgo-RvMU','2026-08-04 08:51:49.991031'),('bgz1e9gqrw1m9q50icszg9dcaqizlffi','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm8O2:AkidyD2oY3-VodsTSRcctzLEL7FjEOdE8sEzR1q7tCU','2026-08-04 11:11:46.864701'),('c29ugjprzg7esv85i6xzmnzmgh9w4kpx','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlse5:t3KJLWtvV7xYiKhJ-BwZWMnztw3TiR-XxjliBZJHtiA','2026-08-03 18:23:17.872983'),('ebrxibs8zxo3uw1antyzsonm9lsrqams','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlHhL:kmpKpBDzIs-G5tlJCqOU5E63h7tRfV7hVsqMYgssD3Y','2026-08-02 02:56:11.500250'),('gl6kx5kbr8iiubftvl6f4887mk6g1u1o','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm6Q7:bAV3exNurUfGcpttNFAO_40EhBax11jjLRPwaWmkstY','2026-08-04 09:05:47.924764'),('gp264z5z98uetsdv8v9nxy6tce5os6u3','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wltHX:gbDW1hqduO781Fa4AvAB0SzcSPVVUkcoJmyZ5fLAkNU','2026-08-03 19:04:03.506301'),('gswa4llykpptatyae9x1z6lflmbc50xe','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm8Jz:tOrUkWJw6wWZV8V9fhhnNcOWjZ8k6FPXSXEmZeAXXoY','2026-08-04 11:07:35.626634'),('hy09jdqrtwyfi0zq7p3dm5dzf5dvwzw6','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm5Br:569y1P7ZHvsRdFvDvxcGAvIqBEOlEiwqT_CaSBrHJkQ','2026-08-04 07:46:59.505068'),('ii6beb4pj0yl8a2brqy5eqdx5oakso6z','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlI9l:yDNYQmbCxAVx7HZRzLhbkc0GMM5-M1oakxfUqPkroHs','2026-08-02 03:25:33.036347'),('kb3jxltdfyqbe1g3x7q9ioo787t92p70','.eJxVjDsOwjAQBe_iGlmx409MSc8Zol3vLg4gR4qTCnF3iJQC2jcz76VG2NYybo2XcSJ1Vk6dfjeE_OC6A7pDvc06z3VdJtS7og_a9HUmfl4O9--gQCvfGi3KEHxnrQTpnaQYeuOYGF2MPXuGISVKYjoGEnaYDUoXvGEvNguo9wfwyTjS:1wh81Y:VHNCA9VrYy6t3ksWA_SEpWVr66aI1iMrKwOJdrfH4H8','2026-07-21 15:47:52.218995'),('kbbnejarvuste2sw62bct6y7jp6mniat','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wltPp:GcnzZN3n8ZQDvM8xW2pYSnxRGR60Sn8Uief4qNl_6Cs','2026-08-03 19:12:37.448605'),('ku64qzq14v4s6d5zlz0v7x61ct19xbqo','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlJ3z:SiJq0nvv-4ur-SEhdvtQ-NHMLX7gxrBnTWjjPDxxcvE','2026-08-02 04:23:39.658478'),('l1upl4vmh90cub4ch1x0iu2pysbpf7ah','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wltGh:0Nr-snoz-Y5e_mjOiOt4RpVNFLOex_uZy-nyWrMf0eM','2026-08-03 19:03:11.904645'),('m1re30g3k7jbijlrrz6h1ynvzeooqswq','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlsuq:Qp6uxE0KIWQQABVOLOiqB8dC6NxaYNSLqdH2uGZUbzo','2026-08-03 18:40:36.868551'),('mbw7ezdfxh9hys0bafg5ec5hk5g5wup6','.eJxVjEEOwiAQRe_C2pBCp8C4dO8ZCAODVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-TuIsRnH63SjEB9cdpHuotyZjq-syk9wVedAury3x83K4fwcl9PKtg00IhBzdZFEZdCY6RA1sATLYkBHBUiaExMYoHLLKo9aMihxONIj3B9RVN1U:1wh5jG:mjJibVm527u_5NekU6HNkAf7C_1_3yzeqMx0PYyQ3rY','2026-07-21 13:20:50.779294'),('r7nzqz6ymbzrgyz07oababayfngr9763','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm7ui:bFZq2IJ24jotQGbVhs06ssAC05entxJrd5HvILz79FI','2026-08-04 10:41:28.448623'),('rsz673ikcfzwqm9hc31n6jtich4oyr9k','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm69Z:Rb574ta1e6cp8T00VU3bf0RYvoLKkPelwsP5PUik-A8','2026-08-04 08:48:41.448505'),('suf6s6njlwkl01ofisvpbj7b2zonlh6x','.eJxVjDsOwjAQBe_iGlmx409MSc8Zol3vLg4gR4qTCnF3iJQC2jcz76VG2NYybo2XcSJ1Vk6dfjeE_OC6A7pDvc06z3VdJtS7og_a9HUmfl4O9--gQCvfGi3KEHxnrQTpnaQYeuOYGF2MPXuGISVKYjoGEnaYDUoXvGEvNguo9wfwyTjS:1wb0Mw:ru6NePycBUZNxCN7KnGrfMBVRHH2XoAxFQ6vpCVCLcA','2026-07-04 18:24:38.467023'),('ul27haktkalucwl16kx3ni6jdrmtdwto','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlt3d:iXh9mMjIGf3v1uijA2bszncnLjd8xYfvp65Rtzm7z8w','2026-08-03 18:49:41.675734'),('uogvnqil72ez18e20n2g2wdc9tv0vrg6','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wm5zN:DOt4_tQAGtZy3RVCOeCnz4c_xtf5LMwJkseLjlmSDLg','2026-08-04 08:38:09.871117'),('xpeaofhktrp9purta32ais7st84nkhuj','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlILK:dI4ZsCL_a0FsYy_sSwrI3knRW9nI5TeqQUR3bincSek','2026-08-02 03:37:30.358438'),('y99pyvflk5j1ohyp0btrtv12klxasdr5','.eJxVjDkOwjAQAP_iGlm-1gclfd5grS8cQLYUJxXi78hSCmhnRvMmHo-9-mPkza-JXIkgl18WMD5zmyI9sN07jb3t2xroTOhpB116yq_b2f4NKo46t9qCAaEsKEgBErOFaaudRo6SuSKRFRGBS16EdiXIJIPmYKxBriwC-XwBqoo2ig:1wlGA2:wLVT1-grKSMYhX4s96FSrrB0j_DctdLbPWXf_gEmvkk','2026-08-02 01:17:42.785337');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rescue_adoptionrequest`
--

DROP TABLE IF EXISTS `rescue_adoptionrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rescue_adoptionrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `decision_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `processed_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) NOT NULL,
  `animal_id` bigint NOT NULL,
  `processed_by_id` bigint DEFAULT NULL,
  `requester_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rescue_adoptionrequest_animal_id_ecdf144c_fk_rescue_animal_id` (`animal_id`),
  KEY `rescue_adoptionreque_processed_by_id_3526d136_fk_accounts_` (`processed_by_id`),
  KEY `rescue_adoptionrequest_requester_id_65abdd99_fk_accounts_user_id` (`requester_id`),
  CONSTRAINT `rescue_adoptionreque_processed_by_id_3526d136_fk_accounts_` FOREIGN KEY (`processed_by_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `rescue_adoptionrequest_animal_id_ecdf144c_fk_rescue_animal_id` FOREIGN KEY (`animal_id`) REFERENCES `rescue_animal` (`id`),
  CONSTRAINT `rescue_adoptionrequest_requester_id_65abdd99_fk_accounts_user_id` FOREIGN KEY (`requester_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rescue_adoptionrequest`
--

LOCK TABLES `rescue_adoptionrequest` WRITE;
/*!40000 ALTER TABLE `rescue_adoptionrequest` DISABLE KEYS */;
INSERT INTO `rescue_adoptionrequest` VALUES (1,'I would like to adopt this animal because I can provide a safe home, regular food, care, and attention. I understand the responsibility of looking after a rescued animal.','APPROVED','Adoption request approved. The requester has provided a suitable reason and appears ready to care for the rescued animal.','2026-06-25 08:49:23.620781','2026-06-25 10:20:17.192066','2026-06-25 10:20:17.210424',1,4,2),(2,'I would like to adopt this animal and provide a safe home. This is a test adoption request for notification testing.','APPROVED','Adoption request approved for notification testing.','2026-07-03 17:14:32.120761','2026-07-03 17:26:17.165953','2026-07-03 17:26:17.165953',2,4,2),(3,'I would like to adopt Puppy Test and provide a safe, caring home. I can provide food, shelter, regular care, and attention. I understand the responsibility of adopting an animal and will make sure the puppy is looked after properly.','APPROVED','Adoption request approved. The requester can contact the shelter to arrange the final handover.','2026-07-07 18:46:25.244145','2026-07-08 06:32:59.572421','2026-07-08 06:32:59.572421',3,4,2),(4,'I would like to adopt this dog and provide a safe home, regular food, and proper care. I understand the animal was rescued and treated by the shelter, and I am ready to take responsibility for its wellbeing.','APPROVED','Approved. The requester has provided a clear adoption message and the animal is ready for adoption after shelter care.','2026-07-11 16:59:31.105545','2026-07-11 18:01:21.203116','2026-07-11 18:01:21.205135',4,4,2),(5,'I would like to adopt bobby and provide a safe home, proper veterinary care, nutritious food, and daily attention. I understand the responsibilities of pet ownership and will ensure he receives lifelong care.','REJECTED','The adoption request has been carefully reviewed. After considering the animal\'s current needs and the current adoption process, the shelter is unable to approve this application at this time. You are welcome to apply for another suitable animal in the future.','2026-07-16 03:17:29.464033','2026-07-16 04:15:34.536829','2026-07-16 04:15:34.536829',5,4,2),(6,'I would like to adopt Puppy Russel because I can provide a safe, loving, and permanent home. I have experience caring for dogs and will ensure regular veterinary care, proper nutrition, exercise, and plenty of affection.','APPROVED','The adoption request has been reviewed and approved. We wish you and Puppy Russel a happy future together.','2026-07-18 18:14:26.182015','2026-07-18 18:38:20.392257','2026-07-18 18:38:20.392257',6,4,3),(7,'I would like to adopt Puppy Russel because I can provide a safe, loving, and permanent home, regular veterinary care, proper nutrition, exercise, and plenty of affection. Love to welcome baby russel into our family.','REJECTED','This request was rejected because another adoption request was approved.','2026-07-18 18:18:50.079014','2026-07-18 18:38:20.507604','2026-07-18 18:38:20.507604',6,4,2),(8,'I would like to adopt Bobby and provide him with a safe home, regular veterinary care, nutritious food, daily exercise, and lifelong love and attention.','REJECTED','','2026-07-21 11:07:52.831630','2026-07-21 11:10:32.355437','2026-07-21 11:10:32.355437',5,4,2),(9,'I would like to adopt Bobby and provide him with a safe home, regular veterinary care, nutritious food, daily exercise, and lifelong love and attention.','PENDING','','2026-07-21 11:12:04.183535',NULL,'2026-07-21 11:12:04.183535',5,NULL,2);
/*!40000 ALTER TABLE `rescue_adoptionrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rescue_animal`
--

DROP TABLE IF EXISTS `rescue_animal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rescue_animal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `animal_image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `health_status` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `treatment_status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `treatment_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `vet_info` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `arrival_date` date DEFAULT NULL,
  `adoption_ready_date` date DEFAULT NULL,
  `outcome_date` date DEFAULT NULL,
  `outcome_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `assigned_rescuer_id` bigint DEFAULT NULL,
  `report_id` bigint NOT NULL,
  `shelter_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `report_id` (`report_id`),
  KEY `rescue_animal_assigned_rescuer_id_3d9bacb5_fk_accounts_user_id` (`assigned_rescuer_id`),
  KEY `rescue_animal_shelter_id_26b3f57f_fk_accounts_user_id` (`shelter_id`),
  CONSTRAINT `rescue_animal_assigned_rescuer_id_3d9bacb5_fk_accounts_user_id` FOREIGN KEY (`assigned_rescuer_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `rescue_animal_report_id_09d4ae41_fk_rescue_report_id` FOREIGN KEY (`report_id`) REFERENCES `rescue_report` (`id`),
  CONSTRAINT `rescue_animal_shelter_id_26b3f57f_fk_accounts_user_id` FOREIGN KEY (`shelter_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rescue_animal`
--

LOCK TABLES `rescue_animal` WRITE;
/*!40000 ALTER TABLE `rescue_animal` DISABLE KEYS */;
INSERT INTO `rescue_animal` VALUES (1,'Kitty','Adult','MALE','animal_images/images_2.jfif','The animal has recovered and is healthy enough to be considered for adoption.','ADOPTED','Treatment completed successfully. The animal is active, eating well, and ready for adoption review.','City Vet Clinic, Maharagama','2026-06-21','2026-06-23','2026-06-25','Adoption request approved. The requester has provided a suitable reason and appears ready to care for the rescued animal.','2026-06-22 18:08:31.792459','2026-06-25 10:20:17.340968',3,3,4),(2,'Test Dog -Tommy','Adult','MALE','animal_images/f3e27a1a-5bdc-48d9-be51-fb980f1df96e-768x1024.webp','Minor injury observed. Animal is stable.','ADOPTED','Animal has recovered and is now ready for adoption testing.','Test clinic','2026-07-03','2026-07-03','2026-07-03','Adoption request approved for notification testing.','2026-07-03 17:00:06.365142','2026-07-03 17:26:17.194254',3,6,4),(3,'Puppy Test','Puppy','FEMALE','animal_images/met-this-cute-puppy-in-vietnam-he-chased-me-down-the-street-v0-ncrivemr74x11.webp','Puppy is healthy, active, and ready for adoption.','ADOPTED','Puppy has completed initial shelter care and is suitable for adoption.','Shelter basic care check','2026-07-06','2026-07-07','2026-07-08','Adoption request approved. The requester can contact the shelter to arrange the final handover.','2026-07-07 11:35:12.198299','2026-07-08 06:32:59.622515',3,5,4),(4,'Brownie','6-8 months','MALE','animal_images/images_11.jfif','The dog is now stable and healthy after basic care and observation. The minor injury has improved, and the animal is suitable for adoption.','ADOPTED','Shelter care and monitoring have been completed. The animal is now ready to be shown in the adoption section for public users.','Shelter basic care unit','2026-07-10','2026-07-11','2026-07-11','Approved. The requester has provided a clear adoption message and the animal is ready for adoption after shelter care.','2026-07-11 15:45:16.176869','2026-07-11 18:01:21.319096',3,10,4),(5,'Bobby','Adult','MALE','animal_images/images_14.jfif','Bobby was treated for 2 months by Kottawa Animal Care Hospital and now the animal is fully recovered.','READY_FOR_ADOPTION','Bobby was treated for 2 months by Kottawa Animal Care Hospital and now the animal is fully recovered and ready to find a loving and caring home.','Kottawa Animal Care Hospital','2026-07-06','2026-07-16',NULL,'','2026-07-16 03:13:48.681444','2026-07-16 03:13:48.681444',3,1,4),(6,'Puppy russel','Puppy','FEMALE','animal_images/images_15.jfif','Puppy is healthy, active, and ready for adoption.','ADOPTED','Puppy has completed initial shelter care and is suitable for adoption.','Shelter basic care check','2026-07-18','2026-07-18','2026-07-19','The adoption request has been reviewed and approved. We wish you and Puppy Russel a happy future together.','2026-07-18 18:03:30.370183','2026-07-18 18:38:20.491971',3,14,4),(7,'Tommy','Adult','FEMALE','','Test','READY_FOR_ADOPTION','Test','Shelter basic care check','2026-07-29','2026-07-29',NULL,'','2026-07-28 18:51:27.442715','2026-07-28 18:51:27.442715',3,4,4);
/*!40000 ALTER TABLE `rescue_animal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rescue_report`
--

DROP TABLE IF EXISTS `rescue_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rescue_report` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `animal_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `other_animal_type` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `condition` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `latitude` decimal(9,6) DEFAULT NULL,
  `longitude` decimal(9,6) DEFAULT NULL,
  `location_description` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `map_link` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `suggested_priority` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `priority` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `report_status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `reported_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `assigned_shelter_id` bigint DEFAULT NULL,
  `reporter_id` bigint NOT NULL,
  `reporter_contact_phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `verification_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `verification_status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `verified_at` datetime(6) DEFAULT NULL,
  `assigned_at` datetime(6) DEFAULT NULL,
  `assigned_rescuer_id` bigint DEFAULT NULL,
  `assignment_notes` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `current_rescue_status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rescue_report_assigned_shelter_id_8f3547a6_fk_accounts_user_id` (`assigned_shelter_id`),
  KEY `rescue_report_reporter_id_98bb8cd2_fk_accounts_user_id` (`reporter_id`),
  KEY `rescue_report_assigned_rescuer_id_73630cc8_fk_accounts_user_id` (`assigned_rescuer_id`),
  CONSTRAINT `rescue_report_assigned_rescuer_id_73630cc8_fk_accounts_user_id` FOREIGN KEY (`assigned_rescuer_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `rescue_report_assigned_shelter_id_8f3547a6_fk_accounts_user_id` FOREIGN KEY (`assigned_shelter_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `rescue_report_reporter_id_98bb8cd2_fk_accounts_user_id` FOREIGN KEY (`reporter_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rescue_report`
--

LOCK TABLES `rescue_report` WRITE;
/*!40000 ALTER TABLE `rescue_report` DISABLE KEYS */;
INSERT INTO `rescue_report` VALUES (1,'DOG','','ROAD_ACCIDENT','Dog near road, unable to move properly.','report_images/images.jfif',6.844234,79.959640,'Near kottawa people\'s bank, old road kottawa','https://maps.app.goo.gl/vvK82gxP6RfrC7uj9','HIGH','HIGH','CLOSED','2026-06-18 06:47:41.352682','2026-07-06 12:36:44.295214',4,2,'','Called reporter, Animal is still at the location.','CONFIRMED_STILL_THERE','2026-06-19 10:34:06.285254','2026-07-05 18:09:06.891324',3,'Animal is near kottawa people\'s bank, old road kottawa. Unable to move properly due to a road accident, Please rescue and bring back to the shelter.','HANDED_OVER_TO_SHELTER'),(3,'CAT','','SICK','Older cat looks sick, doesn\'t eat food','report_images/images_1.jfif',NULL,NULL,'Side of Makumbura Highway bus & train station, behind the pizza hut','https://maps.app.goo.gl/Fk86LKPVBJyWYsCH8','MEDIUM','MEDIUM','CLOSED','2026-06-18 17:43:28.872504','2026-06-21 18:07:34.205406',4,2,'0712345678','Called reporter. Animal is still near the reported location.','CONFIRMED_STILL_THERE','2026-06-18 18:12:03.652653','2026-06-19 10:30:41.575000',3,'Animal is near Makumbura Highway bus and train station, behind Pizza Hut.','HANDED_OVER_TO_SHELTER'),(4,'DOG','','MINOR_INJURY','Test report for checking notification workflow.','',NULL,NULL,'Kottawa test location','','MEDIUM','MEDIUM','CLOSED','2026-07-01 16:27:03.859012','2026-07-28 18:49:42.507619',4,2,'0712345678','','PENDING_VERIFICATION',NULL,'2026-07-06 12:42:40.152213',3,'Animal is at Kottawa test location for checking notification workflow.','HANDED_OVER_TO_SHELTER'),(5,'DOG','','OTHER','Healthy puppy to test notification feature','report_images/images_3.jfif',NULL,NULL,'Near Maharagama cool planet','','LOW','LOW','CLOSED','2026-07-01 17:26:33.290299','2026-07-06 18:03:16.064171',4,2,'0712345678','Called reporter. Animal is still at the reported location.','CONFIRMED_STILL_THERE','2026-07-06 11:28:37.969092','2026-07-06 17:42:03.159797',3,'','HANDED_OVER_TO_SHELTER'),(6,'DOG','','MINOR_INJURY','Notification testing report. This is a new test report to check the full notification workflow.','report_images/images_4.jfif',6.844223,79.959623,'Kottawa test location','','MEDIUM','MEDIUM','CLOSED','2026-07-03 13:52:01.781414','2026-07-03 16:42:27.731648',4,2,'0771234567','Test review completed for notification testing.','CONFIRMED_STILL_THERE','2026-07-03 13:55:34.622618','2026-07-03 15:08:49.519798',3,'Please rescue the animal from the provided location and hand it over to the shelter.','HANDED_OVER_TO_SHELTER'),(7,'CAT','','ABANDONED','A group of small kittens are staying near the roadside. They look very young and may be unsafe because vehicles pass nearby. They appear to need shelter or rescue support.','report_images/images_7.jfif',6.844199,79.959693,'Near AWB roller doors, old road kottawa','https://maps.app.goo.gl/3FiJDjZJaZevJCWx9','LOW','LOW','ASSIGNED','2026-07-06 14:15:50.808877','2026-07-19 06:33:59.977507',4,2,'0712345678','Called reporter. Kittens are still at the reported location.','CONFIRMED_STILL_THERE','2026-07-06 14:32:11.481739','2026-07-19 06:33:59.973508',11,'','NOT_STARTED'),(9,'DOG','','LOST','A dog wearing a collar appears lost and is wandering near the roadside. The animal looks scared but not injured. This is a test lost animal case for PAWS CONNECT workflow testing.','',NULL,NULL,'Near Jaffna Bus Stand, Hospital Rd, Jaffna','https://maps.app.goo.gl/NntEhUTyTFwjCrHC8','LOW','LOW','REVIEWED','2026-07-08 17:12:13.266008','2026-07-09 17:34:26.123279',8,2,'073456789','Lost dog case reviewed. The animal appears to be wearing a collar and may be a lost pet.','CONFIRMED_STILL_THERE','2026-07-08 17:34:39.928844',NULL,NULL,'','NOT_STARTED'),(10,'DOG','','MINOR_INJURY','A dog is staying near the roadside and appears weak with a minor injury. The animal is calm but needs rescue support. This is a final workflow test report for PAWS CONNECT.','report_images/sri-lankan-puppy-village-western-province-224986978.webp',NULL,NULL,'Near Kottawa Bus Stand, High Level Road, Kottawa','https://maps.app.goo.gl/g43baYyg2U98cc5d9','MEDIUM','MEDIUM','CLOSED','2026-07-09 17:44:32.664415','2026-07-10 17:36:55.494563',4,2,'0712345678','Verification Notes: Called the reporter. The dog is still near Kottawa Bus Stand and needs rescue support.','CONFIRMED_STILL_THERE','2026-07-09 18:06:59.829798','2026-07-10 13:45:14.041333',3,'Reassigning this rescue case to another available rescuer for final workflow testing. Please rescue the dog from near Kottawa Bus Stand and hand it over to the shelter.','HANDED_OVER_TO_SHELTER'),(11,'OTHER','Rabbit','MINOR_INJURY','A small rabbit was seen near the roadside and may need shelter support. This is an alternative workflow test for the Other Animal report option.','report_images/images_13.jfif',NULL,NULL,'Near Kadawatha Junction, Kadawatha','https://maps.google.com/?q=Kadawatha+Sri+Lanka','MEDIUM','LOW','CLOSED','2026-07-14 17:16:20.682863','2026-07-14 17:49:48.245355',4,2,'0712345678','Shelter could not confirm the animal at the reported location. The animal may have moved before rescue coordination.','ANIMAL_NOT_FOUND','2026-07-14 17:49:48.245355',NULL,NULL,'','NOT_STARTED'),(12,'DOG','','LOST','The Animal found roaming on the roadside with a collar, seems to be lost.','report_images/348s.jpg',6.844477,79.959665,'Kottawa test location','','LOW','LOW','CLOSED','2026-07-15 16:57:35.617967','2026-07-15 17:00:38.953992',4,2,'0771234567','Called the Reporter and found out that the Animal is not at the location now.','ANIMAL_NOT_FOUND','2026-07-15 17:00:38.953992',NULL,NULL,'','NOT_STARTED'),(13,'DOG','','LOST','Alternative workflow testing. The animal was reported, but the shelter later confirmed that it had already been rescued before rescue assignment.','',6.844411,79.959700,'Near Kottawa Bus Stand','','LOW','LOW','CLOSED','2026-07-15 20:54:01.262529','2026-07-15 20:59:09.435530',4,2,'0771234567','The shelter confirmed that the reported animal had already been rescued before rescue coordination began. No additional rescue assignment was required.','ALREADY_RESCUED','2026-07-15 20:59:09.435530',NULL,NULL,'','NOT_STARTED'),(14,'DOG','','OTHER','Friendly puppy sitting near the roadside. Appears scared but not injured.','report_images/images1.jfif',6.844220,79.959568,'Near Sahara constructions, old road, kottawa.','','LOW','LOW','CLOSED','2026-07-18 13:17:40.841475','2026-07-18 17:52:44.986338',4,2,'0771234567','The report details were verified. The animal was confirmed to still be at the reported location and is suitable for rescue assignment.','CONFIRMED_STILL_THERE','2026-07-18 17:32:29.105715','2026-07-18 17:36:23.058120',3,'Please attend this rescue case and safely transport the animal to the assigned shelter.','HANDED_OVER_TO_SHELTER'),(15,'CAT','','OTHER','test','report_images/images_6.jfif',6.844260,79.959627,'test','','LOW','LOW','REVIEWED','2026-07-18 15:57:16.303880','2026-07-19 06:34:39.166639',4,2,'0771234567','Test verification','CONFIRMED_STILL_THERE','2026-07-19 06:34:39.166639',NULL,NULL,'','NOT_STARTED'),(17,'CAT','','ROAD_ACCIDENT','Friendly puppy waiting near the bus stop. Appears healthy but alone.','report_images/puppy_test_KBsV014.jfif',6.841200,79.965400,'Near Kottawa Bus Stand','https://maps.google.com','HIGH','','SUBMITTED','2026-07-21 09:06:03.897636','2026-07-21 09:06:03.897636',NULL,2,'0771234567','','PENDING_VERIFICATION',NULL,NULL,NULL,'','NOT_STARTED');
/*!40000 ALTER TABLE `rescue_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rescue_rescueupdate`
--

DROP TABLE IF EXISTS `rescue_rescueupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rescue_rescueupdate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `update_text` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `photo` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `report_id` bigint NOT NULL,
  `rescuer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `rescue_rescueupdate_report_id_8ecf38b1_fk_rescue_report_id` (`report_id`),
  KEY `rescue_rescueupdate_rescuer_id_f823b092_fk_accounts_user_id` (`rescuer_id`),
  CONSTRAINT `rescue_rescueupdate_report_id_8ecf38b1_fk_rescue_report_id` FOREIGN KEY (`report_id`) REFERENCES `rescue_report` (`id`),
  CONSTRAINT `rescue_rescueupdate_rescuer_id_f823b092_fk_accounts_user_id` FOREIGN KEY (`rescuer_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rescue_rescueupdate`
--

LOCK TABLES `rescue_rescueupdate` WRITE;
/*!40000 ALTER TABLE `rescue_rescueupdate` DISABLE KEYS */;
INSERT INTO `rescue_rescueupdate` VALUES (1,'ON_THE_WAY','I am on the way to the reported location.','','2026-06-20 18:02:23.264046',3,3),(2,'RESCUED','The cat was safely rescued and will be handed over to the shelter for treatment.','rescue_update_photos/download.jfif','2026-06-20 18:10:27.846977',3,3),(3,'HANDED_OVER_TO_SHELTER','The cat was handed over to the shelter handover location for treatment.','','2026-06-21 18:07:34.188538',3,3),(4,'ON_THE_WAY','Rescuer is on the way to the animal location for notification testing.','','2026-07-03 16:18:39.361045',6,3),(5,'RESCUED','Animal has been rescued from the reported location for notification testing.','rescue_update_photos/360_F_2047686587_2g7JK4KbrClmP4FHgioZCEANZiS0XpD5.jpg','2026-07-03 16:36:38.860358',6,3),(6,'HANDED_OVER_TO_SHELTER','Animal has been handed over to the shelter for treatment tracking.','','2026-07-03 16:42:27.714062',6,3),(7,'ON_THE_WAY','On the way to rescue the animal, currently near homagama police station.','','2026-07-05 18:11:09.102955',1,3),(8,'RESCUED','The Animal was successfully rescued and will be handed over to the shelter.','','2026-07-05 22:02:13.056616',1,3),(9,'HANDED_OVER_TO_SHELTER','the animal has been handed over to the shelter_test_01, No. 25, Main Road, Maharagama.','rescue_update_photos/images_5.jfif','2026-07-06 12:36:44.281753',1,3),(10,'ON_THE_WAY','I am on the way to the reported location.','','2026-07-06 17:59:19.707706',5,3),(11,'RESCUED','The puppy has been rescued from the reported location.','rescue_update_photos/images_10.jfif','2026-07-06 18:02:48.013624',5,3),(12,'HANDED_OVER_TO_SHELTER','The puppy has been handed over to the shelter for treatment and care.','','2026-07-06 18:03:16.064171',5,3),(13,'ON_THE_WAY','I am on the way to the reported location near Kottawa Bus Stand to check and rescue the dog.','','2026-07-10 17:25:17.089294',10,3),(14,'RESCUED','The dog has been found at the reported location and safely rescued. Preparing to hand the animal over to the shelter.','','2026-07-10 17:32:39.825615',10,3),(15,'HANDED_OVER_TO_SHELTER','The rescued dog has been handed over to the assigned shelter for treatment and care.','rescue_update_photos/lost_pup2.jfif','2026-07-10 17:36:55.478457',10,3),(16,'ON_THE_WAY','On the Way to rescue the animal.','','2026-07-15 19:45:05.815846',4,3),(17,'ON_THE_WAY','The rescuer is travelling to the reported location to safely collect the animal.','','2026-07-18 17:46:33.367060',14,3),(18,'RESCUED','The animal has been safely rescued and is being transported to the assigned shelter.','','2026-07-18 17:48:53.239531',14,3),(19,'ON_THE_WAY','The animal has been safely handed over to the assigned shelter for treatment and further care.','rescue_update_photos/download_1.jfif','2026-07-18 17:51:56.151384',14,3),(20,'HANDED_OVER_TO_SHELTER','The animal has been safely handed over to the assigned shelter for treatment and further care.','rescue_update_photos/download_1_1iikNQW.jfif','2026-07-18 17:52:44.968027',14,3),(21,'HANDED_OVER_TO_SHELTER','Handed over the animal to shelter address.','','2026-07-28 18:49:42.492833',4,3);
/*!40000 ALTER TABLE `rescue_rescueupdate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-01 15:39:24
