BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Kiosk" (
	"KioskID"	INTEGER UNIQUE,
	"Location"	TEXT,
	"Rating"	REAL,
	PRIMARY KEY("KioskID")
);
CREATE TABLE IF NOT EXISTS "BentoBox" (
	"BentoName"	TEXT UNIQUE,
	"ProductionCost"	REAL,
	"ContainEgg"	INTEGER,
	"ContainNut"	INTEGER,
	"ContainSeafood"	INTEGER,
	PRIMARY KEY("BentoName")
);
CREATE TABLE IF NOT EXISTS "KioskBento" (
	"KioskID"	INTEGER,
	"BentoName"	TEXT,
	"SellPrice"	REAL,
	FOREIGN KEY("KioskID") REFERENCES "Kiosk"("KioskID"),
	FOREIGN KEY("BentoName") REFERENCES "BentoBox"("BentoName"),
	PRIMARY KEY("KioskID","BentoName")
);
COMMIT;
