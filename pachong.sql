CREATE SCHEMA `xyft` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
CREATE TABLE `WebSiteName`.`Group` (
  `id` BIGINT(10) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(1024) NULL,
  `content` VARCHAR(10240) NULL,
  PRIMARY KEY (`id`));
CREATE TABLE `WebSiteName`.`GroupItem` (
  `id` BIGINT(10) NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(1024) NULL,
  `link` VARCHAR(1024) NULL,
  `time` DATE NULL,
  PRIMARY KEY (`id`));
CREATE TABLE `WebSiteName`.`ToDoTask` (
  `id` BIGINT(10) NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(1024) NULL,
  `lastTime` DATE NULL,
  `status` INT NULL,
  PRIMARY KEY (`id`));
CREATE TABLE `WebSiteName`.`DoneTask` (
  `id` BIGINT(10) NOT NULL,
  `url` VARCHAR(1024) NULL,
  `finishTime` DATE NULL,
  `status` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `xyft`.`history` (
  `qishu` VARCHAR(100) NOT NULL,
  `time` DATETIME NULL,
  `no1` VARCHAR(45) NULL,
  `no2` VARCHAR(45) NULL,
  `no3` VARCHAR(45) NULL,
  `no4` VARCHAR(45) NULL,
  `no5` VARCHAR(45) NULL,
  `no6` VARCHAR(45) NULL,
  `no7` VARCHAR(45) NULL,
  `no8` VARCHAR(45) NULL,
  `no9` VARCHAR(45) NULL,
  `no10` VARCHAR(45) NULL,
  UNIQUE INDEX `qishu_UNIQUE` (`qishu` ASC),
  PRIMARY KEY (`qishu`));