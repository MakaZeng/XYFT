import Calculate.CalculateManager as CM
import Dao.MysqlDBManager as DBM
import Dao.MysqlDBConfig as DBC
import Util.DateUtil as DU
import demjson

def touzhu(qishu,touzhu,userID):
    sql = "CREATE TABLE IF NOT EXISTS `xyft`.`user`(`userID` BIGINT(20) NOT NULL AUTO_INCREMENT,`userName` VARCHAR(512) NULL,`userPassword` VARCHAR(512) NULL,`phone` VARCHAR(45) NULL,`email` VARCHAR(45) NULL,`money` BIGINT(20) NULL,`point` BIGINT(20) NULL,`experience` BIGINT(10) NULL,`userType` INT NULL,PRIMARY KEY (`userID`),UNIQUE INDEX `userID_UNIQUE` (`userID` ASC));"
    DBM.maka_do_sql(sql)

    sql = "CREATE TABLE IF NOT EXISTS touzhu (`qishuUserID` varchar(100) COLLATE utf8_bin NOT NULL,`status` INT DEFAULT NULL,`touzhu` varchar(512) DEFAULT NULL,PRIMARY KEY (`qishuUserID`),UNIQUE KEY `qishuUserID_UNIQUE` (`qishuUserID`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"
    DBM.maka_do_sql(sql)

    qishuUserID = qishu + str(userID)
    insertsql = "INSERT INTO {0}.touzhu (qishuUserID,touzhu,status) VALUES ('{1}','{2}',{3});".format(
        DBC.Database, qishuUserID,demjson.encode(touzhu),0)
    DBM.maka_do_sql(insertsql)
