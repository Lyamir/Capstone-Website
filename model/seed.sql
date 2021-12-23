CREATE DATABASE IF NOT EXISTS capstone_blogsite;
USE capstone_blogsite;

CREATE TABLE IF NOT EXISTS `posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` text,
  `content` longtext,
  `date` datetime DEFAULT NULL,
  `author_username` varchar(45) NOT NULL,
  `views` int DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE IF NOT EXISTS `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `postID` int NOT NULL,
  `content` longtext,
  `date` datetime DEFAULT NULL,
  `author_username` varchar(45) NOT NULL,
  PRIMARY KEY (`id`, `postID`),
  FOREIGN KEY (`postID`) REFERENCES `posts`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE IF NOT EXISTS `reports` (
  `postID` int NOT NULL,
  `views` int DEFAULT 0,
  `numComments` int DEFAULT 0,
  PRIMARY KEY (`postID`),
  FOREIGN KEY (`postID`) REFERENCES `posts`(`id`)
  ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

INSERT INTO `posts` (id, title, content, date, author_username) 
SELECT * FROM (SELECT 1,'Goodbye World','This is an updated post','2021-10-27 00:00:00','admin') AS tmp
WHERE NOT EXISTS (
  SELECT id FROM `posts` WHERE id = 1
) LIMIT 1;

INSERT INTO `reports` (postID) 
SELECT * FROM (SELECT 1) AS tmp
WHERE NOT EXISTS (
  SELECT postID FROM `reports` WHERE postID = 1
) LIMIT 1;

INSERT INTO `posts` (id, title, content, date, author_username) 
SELECT * FROM (SELECT 2,'Test Post','This is a test post','2021-10-27 22:26:02','john') AS tmp
WHERE NOT EXISTS (
  SELECT id FROM `posts` WHERE id = 2
) LIMIT 1;

INSERT INTO `reports` (postID) 
SELECT * FROM (SELECT 2) AS tmp
WHERE NOT EXISTS (
  SELECT postID FROM `reports` WHERE postID = 2
) LIMIT 1;

INSERT INTO `posts` (id, title, content, date, author_username) 
SELECT * FROM (SELECT 3,'Test Post 2','This is another test post','2021-10-27 22:28:45','admin') AS tmp
WHERE NOT EXISTS (
  SELECT id FROM `posts` WHERE id = 3
) LIMIT 1;

INSERT INTO `reports` (postID) 
SELECT * FROM (SELECT 3) AS tmp
WHERE NOT EXISTS (
  SELECT postID FROM `reports` WHERE postID = 3
) LIMIT 1;

