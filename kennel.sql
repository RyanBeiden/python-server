PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

DROP TABLE Employee;

CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);

INSERT INTO `Employee` VALUES (null, "Madi Peper", 1);
INSERT INTO `Employee` VALUES (null, "Kristen Norris", 1);
INSERT INTO `Employee` VALUES (null, "Meg Ducharme", 2);
INSERT INTO `Employee` VALUES (null, "Hannah Hall", 1);
INSERT INTO `Employee` VALUES (null, "Leah Hoefling", 2);

COMMIT;

PRAGMA foreign_keys=on;
