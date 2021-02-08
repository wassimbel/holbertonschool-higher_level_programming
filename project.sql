CREATE DATABASE IF NOT EXISTS mylist-users;
USE mylist-users;
CREATE TABLE IF NOT EXISTS user
(id INT UNIQUE NOT NULL AUTO_INCREMENT,
password VARCHAR(256),
name VARCHAR(256),
last-name VARCHAR(256),
email VARCHAR(256)
phone-number INT(30),
card-number INT(15),
expiry-carddate DATE,
cvv INT(3)) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `user` (`id`, `name`, `last-name`, `email`, `phone-number`, `card-number`, `expiry-carddate`, `cvv`) VALUES (1,
"John", "Jim", "jomjim@gmail.com", "258201201", "0123658978512364", "28/01/2000", 123)
INSERT INTO `user` (`id`, `name`, `last-name`, `email`, `phone-number`, `card-number`, `expiry-carddate`, `cvv`) VALUES ("sam", "paul", "sampaul7@gmail.com", "1234567890123456" , "20/01/2000", 456)

CREATE TABLE IF NOT EXISTS movies
(name VARCHAR(256),
release-date DATE,
genre VARCHAR(256)
rate INT NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `user` (`name`, `release-date`, `genre` ) VALUES ("titanic",
"29/01/2000", "drama",);
INSERT INTO `user` (`name`, `release-date`, `genre` ) VALUES ("never have i ever", "28/10/2001", "romantic");
INSERT INTO `movie` (`name`, `release-date`, `genre` ) VALUES ("what happened to monday", "06/12/1999", "action");
INSERT INTO `movie` (`name`, `release-date`, `genre` ) VALUES("the fault in our stars", "20/02/2005", "drama");
INSERT INTO `user` (`name`, `release-date`, `genre` ) VALUES("harry poter", "23/09/2003" , "sci_fi");
INSERT INTO  (`name`, `release-date`, `genre` ) VALUES ("shrek", "04/11/2001", "romantic")
INSERT INTO  (`name`, `release-date`, `genre` ) VALUES ("the trman show", "13/05/1998", "drama")
CREATE TABLE IF NOT EXISTS tvshows
(name VARCHAR(256),
release-date DATE,
genre VARCHAR(256)
rate INT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO (`name`, `release-date`, `genre` ) VALUES("how to get away with murder", "01/02/1999", "action")
("locked up", "04/12/1999", "action")
("you", "05/07/2000", "drama")
( "queens qambit", "09/12/1998", "drama")
("me before you", "08/11/1997", "romantic")
("the irishman" , "08/10/2000", "action")
CREATE TABLE IF NOT EXISTS animes
(name VARCHAR(256),
release-date DATE,
genre VARCHAR(256)
rate INT NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;



