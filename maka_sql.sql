
/*Create Database*/
CREATE SCHEMA `scheme_name` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
/*Create Table*/
CREATE TABLE `scheme_name`.`table` (
  `id` BIGINT(10) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `time` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_bin;
/*Insert Line*/
ALTER TABLE `scheme_name`.`table` 
ADD COLUMN `more` VARCHAR(45) NULL AFTER `time`;
/*change line*/
ALTER TABLE `scheme_name`.`table` 
CHANGE COLUMN `more` `change` VARCHAR(45) CHARACTER SET 'utf8' NULL DEFAULT NULL ;
/*delete line*/
ALTER TABLE `scheme_name`.`table` 
DROP COLUMN `change`;
/*insert*/
INSERT INTO `scheme_name`.`table` (`id`, `name`, `time`) VALUES ('1', '23232', '44444');
/*update*/
UPDATE `scheme_name`.`table` SET `name`='232222232' WHERE `id`='1';