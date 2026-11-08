/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.0.67-community-nt : Database - wedding
*********************************************************************
Server version : 5.0.67-community-nt
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `wedding`;

USE `wedding`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `email` varchar(50) default NULL,
  `password` varchar(50) default NULL,
  PRIMARY KEY  (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `admin` */

insert  into `admin`(`username`,`email`,`password`) values ('admin','admin@gmail.com','admin');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(20) NOT NULL auto_increment,
  `user_email` varchar(50) default NULL,
  `venue` varchar(50) default NULL,
  `catering` varchar(50) default NULL,
  `decoration` varchar(50) default NULL,
  `numPeople` int(50) default NULL,
  `extraDays` int(30) default NULL,
  `total_cost` int(50) default NULL,
  `wedding_date` varchar(20) default NULL,
  `payment_status` varchar(20) default 'pending',
  `booking_status` varchar(20) default 'pending',
  PRIMARY KEY  (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`user_email`,`venue`,`catering`,`decoration`,`numPeople`,`extraDays`,`total_cost`,`wedding_date`,`payment_status`,`booking_status`) values (1,'sai@gmail.com','The Ritz-Carlton','Blue Plate Catering ','The Vintage Rental Company',34,0,127490,'2024-05-29','Confirmed','Confirmed');

/*Table structure for table `catering` */

DROP TABLE IF EXISTS `catering`;

CREATE TABLE `catering` (
  `cat_id` int(20) NOT NULL auto_increment,
  `cat_type` varchar(50) default NULL,
  `cat_name` varchar(50) default NULL,
  `cat_price` int(50) default NULL,
  PRIMARY KEY  (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `catering` */

insert  into `catering`(`cat_id`,`cat_type`,`cat_name`,`cat_price`) values (1,'Full-Service Catering','Gourmet Caterers',300),(2,'Full-Service Catering','Culinary Capers Catering',400),(3,'Full-Service Catering','Patina Catering ',500),(4,'Buffet Style Catering','Catering by Seasons',150),(5,'Buffet Style Catering','Blue Plate Catering ',300),(6,'Buffet Style Catering','Famous Dave\'s BBQ ',400),(7,'Food Trucks','Kogi BBQ ',150),(8,'Food Trucks','The Grilled Cheese Truck',750),(9,'Food Trucks','Cousins Maine Lobster',250),(10,' Family Style Catering','Giordano\'s Catering',400),(11,' Family Style Catering','Maggiano\'s Little Italy',250),(12,' Family Style Catering','Lucille\'s Smokehouse BBQ ',150),(13,' Cocktail Reception','Truffleberry Market',400),(14,' Cocktail Reception','Puff \'n Stuff Catering ',250),(15,' Cocktail Reception','Creative Edge Parties',400),(16,'Food Trucks','SS trucks food',478);

/*Table structure for table `decoration` */

DROP TABLE IF EXISTS `decoration`;

CREATE TABLE `decoration` (
  `dec_id` int(50) NOT NULL auto_increment,
  `dec_type` varchar(50) default NULL,
  `dec_name` varchar(50) default NULL,
  `dec_price` int(50) default NULL,
  PRIMARY KEY  (`dec_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `decoration` */

insert  into `decoration`(`dec_id`,`dec_type`,`dec_name`,`dec_price`) values (1,'Floral Decorations','Floral Artistry',10000),(2,'Floral Decorations','Bella Flora',12000),(3,'Floral Decorations','The Wild Orchid',22000),(4,'Rustic Decorations','Rustic Chic Events',13000),(5,'Rustic Decorations','Barnwood Events',10000),(6,'Rustic Decorations','Vintage Charm Rentals',5000),(7,'Modern Minimalist Decorations','Minimalist Decor Co',7000),(8,'Modern Minimalist Decorations','Urban Chic Events',49000),(9,'Modern Minimalist Decorations','Clean Slate Events',25000),(10,'Vintage Decorations','Vintage Ambiance',15000),(11,'Vintage Decorations','The Vintage Rental Company',24000),(12,'Vintage Decorations','Retro Revival Events',30000),(14,'Theme-based Decorations','Enchanted Forest Events',12900),(15,'Theme-based Decorations','Tropical Paradise Decor',13400),(16,'Theme-based Decorations','Masquerade Ball Events',14000),(18,'Vintage Decorations','RR decorations',25000);

/*Table structure for table `packages` */

DROP TABLE IF EXISTS `packages`;

CREATE TABLE `packages` (
  `p_id` int(100) NOT NULL auto_increment,
  `package_type` varchar(50) default NULL,
  `venue` varchar(50) default NULL,
  `catering` varchar(50) default NULL,
  `decoration` varchar(50) default NULL,
  `venue_price` int(20) default NULL,
  `catering_price` int(20) default NULL,
  `decoration_price` int(20) default NULL,
  PRIMARY KEY  (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `packages` */

insert  into `packages`(`p_id`,`package_type`,`venue`,`catering`,`decoration`,`venue_price`,`catering_price`,`decoration_price`) values (1,'traditional','saimanikanta gardens','laxmi caterings','ashok decorations',100000,350,15000),(2,'destination','kilimanjaro hills','deva caterings','star decorations',299999,500,30000),(3,'Design','hotel taj','paradise biryanis','alpha designs',300000,450,50000);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone` varchar(15) default NULL,
  `password` varchar(50) default NULL,
  `address` varchar(50) default NULL,
  `city` varchar(50) default NULL,
  `state` varchar(50) default NULL,
  PRIMARY KEY  (`email`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`name`,`email`,`phone`,`password`,`address`,`city`,`state`) values (1,'saikrishna','sai@gmail.com','9999888333','sai','hyd','sircilla','ts');

/*Table structure for table `venue` */

DROP TABLE IF EXISTS `venue`;

CREATE TABLE `venue` (
  `venue_id` int(100) NOT NULL auto_increment,
  `venue_type` varchar(50) default NULL,
  `venue_name` varchar(50) default NULL,
  `venue_price` int(20) default NULL,
  PRIMARY KEY  (`venue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `venue` */

insert  into `venue`(`venue_id`,`venue_type`,`venue_name`,`venue_price`) values (1,'Hotel Ballrooms','Marriott Hotel Grand Ballroom',100000),(2,'Hotel Ballrooms','Hilton Chicago',125000),(3,'Hotel Ballrooms','The Ritz-Carlton',100000),(4,'Hotel Ballrooms','Fairmont San Francisco ',75000),(5,'Hotel Ballrooms','JW Marriott Austin',150000),(6,'Historic Mansions','The Breakers',100000),(7,'Historic Mansions','Biltmore Estate',125000),(8,'Historic Mansions','Vizcaya Museum and Gardens',200000),(9,'Historic Mansions','The Branford House',100000),(10,'Historic Mansions','Lyndhurst Castle',125000),(11,'Outdoor Gardens','Brooklyn Botanic Garden',200000),(12,'Outdoor Gardens','Descanso Gardens',150000),(13,'Outdoor Gardens','Longwood Gardens',135000),(14,'Beach Resorts','Four Seasons Resort Maui at Wailea',150000),(15,'Beach Resorts','The Ritz-Carlton, Laguna Niguel',170000),(16,'Beach Resorts','Sandals Grande Antigua ',155000),(17,'Vineyard or Winery','Napa Valley Vineyard',250000),(18,'Vineyard or Winery','Sonoma Valley Vineyard',190000),(19,'Vineyard or Winery','Chateau St. Jean Winery',350000),(20,'Beach Resorts','Grand Velas Riviera Maya',159000),(21,'Hotel Ballrooms','taj banjara hotel',500000);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
