SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mellow_buffalo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mellow_buffalo` ;

-- -----------------------------------------------------
-- Table `mellow_buffalo`.`fips_2010`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mellow_buffalo`.`fips_2010` ;

CREATE  TABLE IF NOT EXISTS `mellow_buffalo`.`fips_2010` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT ,
  `state_postal` VARCHAR(8) NOT NULL ,
  `state_fips` VARCHAR(8) NOT NULL ,
  `county_fips` VARCHAR(8) NOT NULL ,
  `county_name` VARCHAR(64) NOT NULL ,
  `class_code` VARCHAR(8) NOT NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB;

USE `mellow_buffalo` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
