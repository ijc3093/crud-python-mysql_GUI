DROP DATABASE IF EXISTS employees;

CREATE DATABASE IF NOT EXISTS employees;

SHOW DATABASES;

USE employees;


CREATE TABLE IF NOT EXISTS `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `email` varchar(50),
  `age` int(11) NOT NULL,
  `designation` varchar(255) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=19;

INSERT INTO `Employees` (`id`, `name`, `email`, `age`, `designation`, `created`) VALUES 
(1, 'Sean Doe', 'sean@gmail.com', 32, 'Data Scientist', '2011-06-01 02:13:30'),
(2, 'David Wenye', 'david.mraz1996@yahoo.com', 29, 'Computer Science', '2015-06-03 01:10:10'),
(3, 'John Lopez', 'johnr5@gmail.com', 36, 'Accountant', '2013-09-20 03:10:25'),
(4, 'Rosa Marion', 'rosa@yahoo.com', 34, 'Manager', '2018-04-21 03:11:22'),
(5, 'Matthew Zack', 'matthew@gmail.com', 48, 'Chief Sustainability Officer', '2021-01-14 05:30:30'),
(6, 'Tylor John', 'tylor34@hotmail.com', 37, 'Chemical Technician', '2020-01-10 07:40:10'),
(7, 'Joy Lopez', 'joy.maye@yahoo.com', 40, 'Transportation Planner', '2019-05-02 02:10:30'),
(8, 'Kira Ji', 'kira@yahoo.com', 50, 'Wind Energy Engineer', '2018-01-04 07:17:35'),
(9, 'Andrew Cha', 'andrew@hotmail.com', 41, 'Geneticist', '2019-01-02 01:20:30'),
(10, 'Justin Ogle', 'justin@hotmail.com', 35, 'Space Sciences Teacher', '2020-04-03 06:12:50');
