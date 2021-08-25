BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Visitor" (
	"NRIC"	TEXT,
	"LocationID"	TEXT,
	"Name"	TEXT,
	"Contact"	TEXT,
	"Date"	TEXT,
	"TimeIn"	TEXT,
	"TimeOut"	TEXT
);
CREATE TABLE IF NOT EXISTS "Location" (
	"LocationID"	TEXT,
	"Name"	TEXT,
	"Address"	TEXT,
	"URL"	TEXT,
	PRIMARY KEY("LocationID")
);
COMMIT;
