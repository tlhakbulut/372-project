CREATE DATABASE  IF NOT EXISTS `proje_ara_rapor372` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `proje_ara_rapor372`;
-- MySQL dump 10.13  Distrib 8.0.38, for macos14 (arm64)
--
-- Host: localhost    Database: proje_ara_rapor372
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `Directions`
--

DROP TABLE IF EXISTS `Directions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Directions` (
  `direction_id` int NOT NULL,
  `direction` varchar(5000) DEFAULT NULL,
  `directions_recipe_id` int DEFAULT NULL,
  PRIMARY KEY (`direction_id`),
  KEY `recipe_id_idx` (`directions_recipe_id`),
  CONSTRAINT `directions_recipe_id` FOREIGN KEY (`directions_recipe_id`) REFERENCES `Recipe` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Directions`
--

LOCK TABLES `Directions` WRITE;
/*!40000 ALTER TABLE `Directions` DISABLE KEYS */;
INSERT INTO `Directions` VALUES (1,'Boil water and cook spaghetti.',1),(2,'Mix eggs with Parmesan and season.',1),(3,'Fry chicken until brown.',2),(4,'Add curry powder and simmer.',2),(5,'Sauté beef and mushrooms.',3),(6,'Stir-fry vegetables.',4),(7,'Prepare fish and taco shells.',5),(8,'Bake chocolate cake.',6),(9,'Grill lamb kebabs.',7),(10,'Cook tomato soup.',8);
/*!40000 ALTER TABLE `Directions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FavouriteRecipes`
--

DROP TABLE IF EXISTS `FavouriteRecipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FavouriteRecipes` (
  `favourite_id` int NOT NULL,
  `fav_user_id` int DEFAULT NULL,
  `fav_recipe_id` int DEFAULT NULL,
  PRIMARY KEY (`favourite_id`),
  KEY `fav_user_id_idx` (`fav_user_id`),
  KEY `fav_recipe_id_idx` (`fav_recipe_id`),
  CONSTRAINT `fav_recipe_id` FOREIGN KEY (`fav_recipe_id`) REFERENCES `Recipe` (`recipe_id`),
  CONSTRAINT `fav_user_id` FOREIGN KEY (`fav_user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FavouriteRecipes`
--

LOCK TABLES `FavouriteRecipes` WRITE;
/*!40000 ALTER TABLE `FavouriteRecipes` DISABLE KEYS */;
INSERT INTO `FavouriteRecipes` VALUES (1,1,10),(2,2,9),(3,3,8),(4,4,7),(5,5,6),(6,6,5),(7,7,4),(8,8,3),(9,9,2),(10,10,1);
/*!40000 ALTER TABLE `FavouriteRecipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Includes`
--

DROP TABLE IF EXISTS `Includes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Includes` (
  `include_recipe_id` int DEFAULT NULL,
  `ingredient_id` int DEFAULT NULL,
  KEY `ingrdient_id_idx` (`ingredient_id`),
  KEY `include_recipe_id_idx` (`include_recipe_id`),
  CONSTRAINT `include_recipe_id` FOREIGN KEY (`include_recipe_id`) REFERENCES `Recipe` (`recipe_id`),
  CONSTRAINT `ingrdient_id` FOREIGN KEY (`ingredient_id`) REFERENCES `Ingredients` (`ingredient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Includes`
--

LOCK TABLES `Includes` WRITE;
/*!40000 ALTER TABLE `Includes` DISABLE KEYS */;
INSERT INTO `Includes` VALUES (1,1),(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(4,9),(5,10);
/*!40000 ALTER TABLE `Includes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ingredients`
--

DROP TABLE IF EXISTS `Ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ingredients` (
  `ingredient_id` int NOT NULL,
  `ingredient` varchar(45) NOT NULL,
  PRIMARY KEY (`ingredient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ingredients`
--

LOCK TABLES `Ingredients` WRITE;
/*!40000 ALTER TABLE `Ingredients` DISABLE KEYS */;
INSERT INTO `Ingredients` VALUES (1,'Spaghetti'),(2,'Egg'),(3,'Parmesan Cheese'),(4,'Chicken'),(5,'Curry Powder'),(6,'Beef'),(7,'Mushrooms'),(8,'Carrot'),(9,'Cabbage'),(10,'Fish');
/*!40000 ALTER TABLE `Ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nutrition`
--

DROP TABLE IF EXISTS `Nutrition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nutrition` (
  `nutrition_id` int NOT NULL,
  `nutrition_recipe_id` int DEFAULT NULL,
  `nutrient` varchar(1000) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`nutrition_id`),
  KEY `recipe_id_idx` (`nutrition_recipe_id`),
  CONSTRAINT `nutrition_recipe_id` FOREIGN KEY (`nutrition_recipe_id`) REFERENCES `Recipe` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nutrition`
--

LOCK TABLES `Nutrition` WRITE;
/*!40000 ALTER TABLE `Nutrition` DISABLE KEYS */;
INSERT INTO `Nutrition` VALUES (1,1,'Calories',320),(2,2,'Calories',450),(3,3,'Calories',700),(4,4,'Calories',240),(5,5,'Calories',300),(6,6,'Calories',600),(7,7,'Calories',500),(8,8,'Calories',150),(9,9,'Calories',350),(10,10,'Calories',200);
/*!40000 ALTER TABLE `Nutrition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipe`
--

DROP TABLE IF EXISTS `Recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recipe` (
  `recipe_id` int NOT NULL,
  `recipe_name` varchar(45) NOT NULL,
  `cuisine_path` varchar(45) DEFAULT NULL,
  `servings` int DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`),
  CONSTRAINT `check_rating` CHECK ((`rating` between 0 and 10))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipe`
--

LOCK TABLES `Recipe` WRITE;
/*!40000 ALTER TABLE `Recipe` DISABLE KEYS */;
INSERT INTO `Recipe` VALUES (1,'Spaghetti Carbonara','Italian',4,4.5,'http://example.com/spaghetti'),(2,'Chicken Curry','Indian',4,4.2,'http://example.com/chicken-curry'),(3,'Beef Stroganoff','Russian',2,4.8,'http://example.com/beef-stroganoff'),(4,'Vegetable Stir Fry','Chinese',3,4.3,'http://example.com/vegetable-stir-fry'),(5,'Fish Tacos','Mexican',2,4,'http://example.com/fish-tacos'),(6,'Chocolate Cake','French',8,4.9,'http://example.com/chocolate-cake'),(7,'Lamb Kebab','Middle Eastern',2,4.6,'http://example.com/lamb-kebab'),(8,'Tomato Soup','American',5,4.1,'http://example.com/tomato-soup'),(9,'Sushi','Japanese',2,4.7,'http://example.com/sushi'),(10,'Pasta Salad','Italian',3,4,'http://example.com/pasta-salad');
/*!40000 ALTER TABLE `Recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Timing`
--

DROP TABLE IF EXISTS `Timing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Timing` (
  `timing_id` int NOT NULL,
  `timing_recipe_id` int DEFAULT NULL,
  `timing_type` varchar(45) DEFAULT NULL,
  `minute` int DEFAULT NULL,
  `hour` int DEFAULT NULL,
  PRIMARY KEY (`timing_id`),
  KEY `timing_recipe_id_idx` (`timing_recipe_id`),
  CONSTRAINT `timing_recipe_id` FOREIGN KEY (`timing_recipe_id`) REFERENCES `Recipe` (`recipe_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Timing`
--

LOCK TABLES `Timing` WRITE;
/*!40000 ALTER TABLE `Timing` DISABLE KEYS */;
INSERT INTO `Timing` VALUES (1,1,'Cook',20,0),(2,2,'Cook',30,0),(3,3,'Prep',15,0),(4,4,'Cook',10,0),(5,5,'Prep',25,0),(6,6,'Cook',45,0),(7,7,'Cook',30,0),(8,8,'Prep',10,0),(9,9,'Cook',0,1),(10,10,'Prep',15,0);
/*!40000 ALTER TABLE `Timing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `user_id` int NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'johnsmith','password123'),(2,'janedoe','securepass456'),(3,'mikebrown','mypassword789'),(4,'emilywhite','password101112'),(5,'davewilson','passphrase131415'),(6,'laurajones','mypwd161718'),(7,'chrisgreen','secretpassword1920'),(8,'sarahhall','password212223'),(9,'brianclark','pass242526'),(10,'lisawalker','password272829');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserRecipes`
--

DROP TABLE IF EXISTS `UserRecipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `UserRecipes` (
  `ur_user_id` int DEFAULT NULL,
  `ur_recipe_id` int DEFAULT NULL,
  `user_recipe_id` int NOT NULL,
  PRIMARY KEY (`user_recipe_id`),
  KEY `ur_user_id_idx` (`ur_user_id`),
  KEY `ur_recipe_id_idx` (`ur_recipe_id`),
  CONSTRAINT `ur_recipe_id` FOREIGN KEY (`ur_recipe_id`) REFERENCES `Recipe` (`recipe_id`),
  CONSTRAINT `ur_user_id` FOREIGN KEY (`ur_user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserRecipes`
--

LOCK TABLES `UserRecipes` WRITE;
/*!40000 ALTER TABLE `UserRecipes` DISABLE KEYS */;
INSERT INTO `UserRecipes` VALUES (1,2,1),(2,3,2),(3,4,3),(4,5,4),(5,6,5),(6,7,6),(7,8,7),(8,9,8),(9,10,9),(10,1,10);
/*!40000 ALTER TABLE `UserRecipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-07  0:31:14
