#Шаг 1: Создание базы данных tradein.
CREATE DATABASE tradein;
USE tradein;

#Шаг 2: Создание общей таблицы ‘OrdLog’ для последующей выгрузки данных по всем заявкам.
CREATE TABLE
IF
	NOT EXISTS OrdLog (
	NO INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	seccode TEXT NOT NULL,
	buysell VARCHAR ( 1 ) NOT NULL,
	TIME INT NOT NULL,
	orderno INT NOT NULL,
	ACTION SMALLINT NOT NULL,
	price decimal(20, 10) NOT NULL,
	volume INT NOT NULL,
	tradeno BIGINT,
	tradeprice decimal(20, 10) 
	);
	
#Шаг 3: Создание таблицы ‘PreferredStock’ для последующей выгрузки данных по привилегированным акциям.
CREATE TABLE
IF
	NOT EXISTS PreferredStock (
	NO INT NOT NULL auto_increment PRIMARY KEY,
	seccode TEXT NOT NULL,
	buysell VARCHAR ( 1 ) NOT NULL,
	TIME INT NOT NULL,
	orderno INT NOT NULL,
	ACTION SMALLINT NOT NULL,
	price decimal(20, 10) NOT NULL,
	volume INT NOT NULL,
	tradeno BIGINT,
	tradeprice decimal(20, 10)
	);
	
#Шаг 4: Создание таблицы ‘CommonStock’ для последующей выгрузки данных по обыкновенным акциям.
CREATE TABLE
IF
	NOT EXISTS CommonStock (
	NO INT NOT NULL auto_increment PRIMARY KEY,
	seccode TEXT NOT NULL,
	buysell VARCHAR ( 1 ) NOT NULL,
	TIME INT NOT NULL,
	orderno INT NOT NULL,
	ACTION SMALLINT NOT NULL,
	price decimal(20, 10) NOT NULL,
	volume INT NOT NULL,
	tradeno BIGINT,
	tradeprice decimal(20, 10)
	);
	
#Шаг 5: Создание таблицы ‘Bonds’ для последующей выгрузки данных по облигациям.
CREATE TABLE
IF
	NOT EXISTS Bonds (
	NO INT NOT NULL auto_increment PRIMARY KEY,
	seccode TEXT NOT NULL,
	buysell VARCHAR ( 1 ) NOT NULL,
	TIME INT NOT NULL,
	orderno INT NOT NULL,
	ACTION SMALLINT NOT NULL,
	price decimal(20, 10) NOT NULL,
	volume INT NOT NULL,
	tradeno BIGINT,
	tradeprice decimal(20, 10)
	);
