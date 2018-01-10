CREATE DATABASE  IF NOT EXISTS `rhm_database` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `rhm_database`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: rhm_database
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Temporary view structure for view `examination_view`
--

DROP TABLE IF EXISTS `examination_view`;
/*!50001 DROP VIEW IF EXISTS `examination_view`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `examination_view` AS SELECT 
 1 AS `Name`,
 1 AS `Surname`,
 1 AS `PESEL`,
 1 AS `Examination Date`,
 1 AS `Examination Name`,
 1 AS `Systolic Pressure`,
 1 AS `Diastolic Pressure`,
 1 AS `Body Height`,
 1 AS `Body Weight`,
 1 AS `BMI`,
 1 AS `Heart Rate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `patientdata`
--

DROP TABLE IF EXISTS `patientdata`;
/*!50001 DROP VIEW IF EXISTS `patientdata`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `patientdata` AS SELECT 
 1 AS `Name`,
 1 AS `Surname`,
 1 AS `Date Of Birth`,
 1 AS `Gender`,
 1 AS `Country`,
 1 AS `City`,
 1 AS `Postal Code`,
 1 AS `Phone Number`,
 1 AS `PESEL`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `patientexamination`
--

DROP TABLE IF EXISTS `patientexamination`;
/*!50001 DROP VIEW IF EXISTS `patientexamination`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `patientexamination` AS SELECT 
 1 AS `Name`,
 1 AS `Surname`,
 1 AS `Examination Date`,
 1 AS `Systolic Pressure`,
 1 AS `Diastolic Pressure`,
 1 AS `Heart Rate`,
 1 AS `Patient Height`,
 1 AS `Patient Weight`,
 1 AS `BMI`,
 1 AS `Patient Feedback`,
 1 AS `Parameter Warning`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `examination_view`
--

/*!50001 DROP VIEW IF EXISTS `examination_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `examination_view` AS select `patientcredentials`.`Name` AS `Name`,`patientcredentials`.`SurName` AS `Surname`,`patientcredentials`.`PESEL` AS `PESEL`,`ex_catalogue`.`ExaminationDate` AS `Examination Date`,`ex_catalogue`.`ExaminationName` AS `Examination Name`,`ex_bloodpressure`.`SystolicPressure` AS `Systolic Pressure`,`ex_bloodpressure`.`DiastolicPressure` AS `Diastolic Pressure`,`ex_wellnessparameters`.`BodyHeight` AS `Body Height`,`ex_wellnessparameters`.`BodyWeight` AS `Body Weight`,`ex_wellnessparameters`.`BMI` AS `BMI`,`ex_heartrate`.`HeartRate` AS `Heart Rate` from ((((`ex_catalogue` left join `patientcredentials` on((`patientcredentials`.`ID_Patient` = `ex_catalogue`.`PatientID`))) left join `ex_bloodpressure` on((`ex_catalogue`.`ExaminationID` = `ex_bloodpressure`.`ExaminationID`))) left join `ex_wellnessparameters` on((`ex_catalogue`.`ExaminationID` = `ex_wellnessparameters`.`ExaminationID`))) left join `ex_heartrate` on((`ex_catalogue`.`ExaminationID` = `ex_heartrate`.`ExaminationID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `patientdata`
--

/*!50001 DROP VIEW IF EXISTS `patientdata`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `patientdata` AS select `patientcredentials`.`Name` AS `Name`,`patientcredentials`.`SurName` AS `Surname`,`patientcredentials`.`DateOfBirth` AS `Date Of Birth`,`patientcredentials`.`Gender` AS `Gender`,`patientcredentials`.`Country` AS `Country`,`patientcredentials`.`City` AS `City`,`patientcredentials`.`PostalCode` AS `Postal Code`,`patientcredentials`.`PhoneNumber` AS `Phone Number`,`patientcredentials`.`PESEL` AS `PESEL` from `patientcredentials` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `patientexamination`
--

/*!50001 DROP VIEW IF EXISTS `patientexamination`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `patientexamination` AS select `patientcredentials`.`Name` AS `Name`,`patientcredentials`.`SurName` AS `Surname`,`examination`.`ExaminationDate` AS `Examination Date`,`examination`.`SystolicPressure` AS `Systolic Pressure`,`examination`.`DiastolicPressure` AS `Diastolic Pressure`,`examination`.`HeartRate` AS `Heart Rate`,`examination`.`PatientHeight` AS `Patient Height`,`examination`.`PatientWeight` AS `Patient Weight`,`examination`.`BMI` AS `BMI`,`examination`.`PatientFeedback` AS `Patient Feedback`,`examination`.`ParameterWarning` AS `Parameter Warning` from (`patientcredentials` join `examination` on((`patientcredentials`.`ID_Patient` = `examination`.`FID_Examination`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping events for database 'rhm_database'
--

--
-- Dumping routines for database 'rhm_database'
--
/*!50003 DROP PROCEDURE IF EXISTS `DataVisualization_int` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DataVisualization_int`(in parameter varchar(45), in  operator varchar(1), in parameter_value int)
BEGIN

CREATE TEMPORARY TABLE IF NOT EXISTS examination_results SELECT * FROM rhm_database.examination_view;
CREATE TEMPORARY TABLE examination_results_copy SELECT * FROM rhm_database.examination_results;


IF operator = '>' THEN

	DROP table examination_results;
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` > ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;

ELSEIF operator = '<' THEN

	DROP table examination_results;
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` < ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;

ELSEIF operator = '=' THEN

	DROP table examination_results;
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` = ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;
    
ELSEIF operator = 'Text Like' THEN

	DROP table examination_results_copy;   
    
    
END IF;

DROP table examination_results_copy;
DEALLOCATE PREPARE stmt;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DataVisualization_reset` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DataVisualization_reset`()
BEGIN

select * from examination_view;
DROP table IF EXISTS examination_results;
DROP table IF EXISTS examination_results_copy;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DataVisualization_str` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DataVisualization_str`(in parameter varchar(45), in parameter_value varchar(45))
BEGIN

CREATE TEMPORARY TABLE IF NOT EXISTS examination_results SELECT * FROM rhm_database.examination_view;
CREATE TEMPORARY TABLE examination_results_copy SELECT * FROM rhm_database.examination_results;

DROP table examination_results;

set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` LIKE "', parameter_value,'"');
PREPARE stmt FROM @k;
EXECUTE stmt;

SELECT * FROM examination_results;
DROP table examination_results_copy;

DEALLOCATE PREPARE stmt;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Data_bulk_insert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Data_bulk_insert`(in incoming_data text)
BEGIN

SET @ExaminationType := (SELECT SUBSTRING_INDEX(incoming_data, '___', 1));
SET @PatientID := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 2), '___', -1));
SET @ExaminationDate := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 3), '___', -1));

##########################################################
# Based on type of examination string is divided into    #
# respective categories Were the additional examination  #
# type to be added a database administrator is to create #
# an additional table to store its results plus write    #
# the condition in THIS stored procedure                 #
##########################################################

############################## WELLNESS PARAMETERS
if @ExaminationType = 1 THEN
SET @BodyHeight := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));
SET @BodyWeight := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 5), '___', -1));

INSERT INTO ex_wellness_parameters VALUES (@PatientID, @ExaminationDate, @BodyHeight, @BodyWeight, 0);

############################## HEART RATE
ELSEIF @ExaminationType = 2 THEN
SET @HeartRate := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));

INSERT INTO ex_heart_rate VALUES (@PatientID, @ExaminationDate, @HeartRate);

############################## BLOOD PRESSURE
ELSEIF @ExaminationType = 3 THEN
SET @SystolicPressure := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));
SET @DiastolicPressure := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 5), '___', -1));

INSERT INTO ex_blood_pressure VALUES (@PatientID, @ExaminationDate, @SystolicPressure, @DiastolicPressure);

END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Data_insert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Data_insert`(in ex_type int, in patient_id int, in  ex_datetime datetime(1),
 in parameter_int1 int, in parameter_int2 int, in parameter_int3 int, in parameter_int4 int, in parameter_int5 int,
 in parameter_str1 varchar(45), in parameter_str2 varchar(45), in parameter_str3 varchar(45),
 in parameter_blob1 blob, in parameter_blob2 mediumblob, in parameter_blob3 longblob)
BEGIN

# welness_parameters
IF ex_type = 1 THEN

	insert into ex_wellness_parameters(`PatientID`, `ExaminationDate`, `BodyHeight`, `BodyWeight`) values (patient_id, ex_datetime, parameter_int1, parameter_int2);

# heart_rate
ELSEIF ex_type = 2 THEN

	insert into ex_heart_rate(`PatientID`, `ExaminationDate`, `HeartRate`) values (patient_id, ex_datetime, parameter_int1);

# blood_pressure
ELSEIF ex_type = 3 THEN

	insert into ex_blood_pressure(`PatientID`, `ExaminationDate`, `SystolicPressure`, `DiastolicPressure`) values (patient_id, ex_datetime, parameter_int1, parameter_int2);    
    
END IF;


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Examination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Examination`(in parameter varchar(45), in  operator varchar(1), in parameter_value int)
BEGIN

set @parameter = parameter;
set @operator = operator;

IF operator = '>' THEN

	#set @k = CONCAT('SELECT `', parameter,'` FROM rhm_database.patientexamination WHERE `', parameter,'` < ', parameter_value);
	set @k = CONCAT('SELECT * FROM rhm_database.patientexamination WHERE `', parameter,'` > ', parameter_value);
	PREPARE stmt FROM @k;
	EXECUTE stmt;

ELSEIF operator = '<' THEN

	set @k = CONCAT('SELECT * FROM rhm_database.patientexamination WHERE `', parameter,'` < ', parameter_value);
	PREPARE stmt FROM @k;
	EXECUTE stmt;

ELSEIF operator = '=' THEN

	set @k = CONCAT('SELECT * FROM rhm_database.patientexamination WHERE `', parameter,'` = ', parameter_value);
	PREPARE stmt FROM @k;
	EXECUTE stmt;
    
    
END IF;

DEALLOCATE PREPARE stmt;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Examination_data_insert` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Examination_data_insert`(in incoming_data text)
BEGIN

SET FOREIGN_KEY_CHECKS = 0;

SET @ExaminationType := (SELECT SUBSTRING_INDEX(incoming_data, '___', 1));
SET @PatientID := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 2), '___', -1));
SET @ExaminationDate := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 3), '___', -1));

##########################################################
# Based on type of examination string is divided into    #
# respective categories Were the additional examination  #
# type to be added a database administrator is to create #
# an additional table to store its results plus write    #
# the condition in THIS stored procedure                 #
##########################################################

############################## WELLNESS PARAMETERS ######################################
if @ExaminationType = 1 THEN
SET @BodyHeight := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));
SET @BodyWeight := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 5), '___', -1));
SET @ExaminationName = 'Wellness';

INSERT INTO ex_catalogue(`PatientID`, `ExaminationDate`, `ExaminationName`)
			VALUES (@PatientID, @ExaminationDate, @ExaminationName);

SET @ExaminationID = last_insert_id();

INSERT INTO ex_wellnessparameters(`ExaminationID`,`BodyHeight`, `BodyWeight`, `BMI`) VALUES (@ExaminationID, @BodyHeight, @BodyWeight, 0);

############################## HEART RATE ######################################
ELSEIF @ExaminationType = 2 THEN
SET @HeartRate := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));
SET @ExaminationName = 'Heart Rate';

INSERT INTO ex_catalogue(`PatientID`, `ExaminationDate`, `ExaminationName`)
			VALUES (@PatientID, @ExaminationDate, @ExaminationName);
            
SET @ExaminationID = last_insert_id();

INSERT INTO ex_heartrate (`ExaminationID`,`HeartRate`) VALUES (@ExaminationID, @HeartRate);

############################## BLOOD PRESSURE ######################################
ELSEIF @ExaminationType = 3 THEN
SET @SystolicPressure := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 4), '___', -1));
SET @DiastolicPressure := (SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(incoming_data, '___', 5), '___', -1));
SET @ExaminationName = 'BloodPressure';

INSERT INTO ex_catalogue(`PatientID`, `ExaminationDate`, `ExaminationName`)
			VALUES (@PatientID, @ExaminationDate, @ExaminationName);
        
SET @ExaminationID = last_insert_id();

INSERT INTO ex_bloodpressure (`ExaminationID`, `SystolicPressure`, `DiastolicPressure`) VALUES (@ExaminationID, @SystolicPressure, @DiastolicPressure);

END IF;

SET FOREIGN_KEY_CHECKS = 1;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Examination_int` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Examination_int`(in parameter varchar(45), in  operator varchar(1), in parameter_value int)
BEGIN

#DROP TEMPORARY TABLE IF EXISTS examination_results;

#CREATE TEMPORARY TABLE IF NOT EXISTS examination_results SELECT * FROM rhm_database.patientexamination;
CREATE TEMPORARY TABLE IF NOT EXISTS examination_results SELECT * FROM rhm_database.examination_view;
CREATE TEMPORARY TABLE examination_results_copy SELECT * FROM rhm_database.examination_results;


IF operator = '>' THEN

	#set @k = CONCAT('SELECT `', parameter,'` FROM rhm_database.patientexamination WHERE `', parameter,'` < ', parameter_value);
	DROP table examination_results;
    #set @k = CONCAT('INSERT INTO examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` > ', parameter_value);
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` > ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;
	DROP table examination_results_copy;


ELSEIF operator = '<' THEN

	DROP table examination_results;
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` < ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;
	DROP table examination_results_copy;


ELSEIF operator = '=' THEN

	DROP table examination_results;
    set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` = ', parameter_value);
    PREPARE stmt FROM @k;
    EXECUTE stmt;
    SELECT * FROM examination_results;
	DROP table examination_results_copy;
    
   	
ELSEIF operator = 'Text Like' THEN

	DROP table examination_results_copy;   
    
    
END IF;

DEALLOCATE PREPARE stmt;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Examination_reset` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Examination_reset`()
BEGIN

DROP table examination_results;
DROP table examination_results_copy;
SELECT * FROM examination_view;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Examination_str` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `Examination_str`(in parameter varchar(45), in parameter_value varchar(45))
BEGIN

CREATE TEMPORARY TABLE IF NOT EXISTS examination_results SELECT * FROM rhm_database.patientexamination;
CREATE TEMPORARY TABLE examination_results_copy SELECT * FROM rhm_database.examination_results;

DROP table examination_results;

set @k = CONCAT('CREATE TEMPORARY TABLE examination_results SELECT * FROM rhm_database.examination_results_copy WHERE `', parameter,'` LIKE "', parameter_value,'"');
PREPARE stmt FROM @k;
EXECUTE stmt;

SELECT * FROM examination_results;
DROP table examination_results_copy;

DEALLOCATE PREPARE stmt;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `FindPatient_AND` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `FindPatient_AND`(in InputName varchar(45), 
in InputSurname varchar(45), in InputDateOfBirth varchar(45), in InputGender varchar(1),
 in InputCountry varchar(45), in InputCity varchar(45), in InputPostalCode varchar(15),
 in InputPhoneNumber varchar(20), in InputPESEL varchar(20))
BEGIN

SELECT * from rhm_database.patientdata where
`Name` like InputName 
AND `Surname` like InputSurname
AND `Gender` like InputGender
AND `Date Of Birth` like InputDateOfBirth
AND `Country` like InputCountry
AND `City` like InputCity
AND `Postal Code` like InputPostalCode
AND `Phone Number` like InputPhoneNumber
AND `PESEL` like InputPESEL;
 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `FindPatient_OR` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `FindPatient_OR`(in InputName varchar(45), 
in InputSurname varchar(45), in InputDateOfBirth varchar(45), in InputGender varchar(1),
 in InputCountry varchar(45), in InputCity varchar(45), in InputPostalCode varchar(15),
 in InputPhoneNumber varchar(20), in InputPESEL varchar(20))
BEGIN

SELECT * from rhm_database.patientdata where
`Name` like InputName 
OR `Surname` like InputSurname
OR `Date Of Birth` like InputDateOfBirth
OR `Gender` like InputGender
OR `Country` like InputCountry
OR `City` like InputCity
OR `Postal Code` like InputPostalCode
OR `Phone Number` like InputPhoneNumber
OR `PESEL` like InputPESEL;
 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-01-06 17:04:39
