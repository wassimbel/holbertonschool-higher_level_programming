DROP DATABASE mylist_users;
CREATE DATABASE IF NOT EXISTS mylist_users;
USE mylist_users;
CREATE TABLE IF NOT EXISTS user
(id INT UNIQUE NOT NULL AUTO_INCREMENT,
password VARCHAR(256),
name VARCHAR(256),
last_name VARCHAR(256),
email VARCHAR(256),
phone_number INT,
card_number VARCHAR(256),
expiry_card DATE,
cvv INT NOT NULL);

INSERT INTO `user` (`id`, `name`, `last_name`, `email`, `phone_number`, `card_number`, `expiry_card`, `cvv`) VALUES (17,
"John", "Jim", "jomjim@gmail.com", "258201201", "01236589785", "2000-05-21", 123);
INSERT INTO `user` (`id`, `name`, `last_name`, `email`, `phone_number`, `card_number`, `expiry_card`, `cvv`) VALUES (18,
"sam", "paul", "sampaul7@gmail.com", "25645454" , "0013543543" , "2000-06-01", 456);

CREATE TABLE IF NOT EXISTS movies
(name VARCHAR(256),
release_date DATE,
genre VARCHAR(256));

INSERT INTO `movies` (`name`, `release_date`, `genre` ) VALUES ("titanic",
"2000-04-04", "drama");
INSERT INTO `movies` (`name`, `release_date`, `genre` ) VALUES ("never have i ever", "2001-05-05", "romantic");
INSERT INTO `movies` (`name`, `release_date`, `genre` ) VALUES ("what happened to monday", "2005-04-02", "action");
INSERT INTO `movies` (`name`, `release_date`, `genre` ) VALUES ("the fault in our stars", "2001-02-08", "drama");
INSERT INTO `movies` (`name`, `release_date`, `genre` ) VALUES ("harry poter", "2005-02-01" , "sci_fi");
INSERT INTO  `movies` (`name`, `release_date`, `genre` ) VALUES ("shrek", "2010-09-09", "romantic");
INSERT INTO  `movies` (`name`, `release_date`, `genre` ) VALUES ("the truman show", "1998-02-02", "drama");

CREATE TABLE IF NOT EXISTS tvshows
(name VARCHAR(256),
release_date DATE,
genre VARCHAR(256));

INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ("how to get away with murder", "1999-01-01", "action");
INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ("locked up", "1997-02-02", "action");
INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ("you", "2007-07-07", "drama");
INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ( "queens qambit", "1998-09-08", "drama");
INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ("me before you", "1991-05-05", "romantic");
INSERT INTO `tvshows` (`name`, `release_date`, `genre` ) VALUES ("the irishman" , "2000-10-10", "action");

CREATE TABLE IF NOT EXISTS animes
(name VARCHAR(256),
release_date DATE,
genre VARCHAR(256));

INSERT INTO `animes` (`name`, `release_date`, `genre` ) VALUES ("the simpsons", "1998-01-01", "comdey");
INSERT INTO `animes` (`name`, `release_date`, `genre` ) VALUES ("rick and morty", "2015-05-01", "sci-fi");


