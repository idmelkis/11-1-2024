# Linki:

* [Foreign keys](https://www.sqlite.org/foreignkeys.html)
* [Transactions](https://www.sqlite.org/lang_transaction.html)
* [Indeksi - kas tie ir un kā tie strādā](https://www.sqlitetutorial.net/sqlite-index/)
* [Agregāta funkcijas](https://www.sqlite.org/lang_aggfunc.html)

Dokumentācija vaicājumiem - meklējat vaicājuma tipu (piem. INSERT) Google + "sqlite". Rezultāti būs zem sqlite.org domēna, piem. https://www.sqlite.org/lang_insert.html

# SQL kods

Tabulas izveide
```sql
CREATE TABLE "Employee" (
	"employeeID"	INTEGER NOT NULL UNIQUE,
	"firstName"	TEXT,
	"lastName"	TEXT,
	"birthDate"	INTEGER,
	PRIMARY KEY("employeeID" AUTOINCREMENT)
);
```

FOREIGN KEY:
```sql
CREATE TABLE "Order" (
	"orderID"	INTEGER NOT NULL UNIQUE,
	"customerID"	INTEGER NOT NULL,
	"employeeID"	INTEGER NOT NULL,
	"productID"	INTEGER NOT NULL,
	"orderTotal"	REAL,
	"orderDate"	REAL,
	PRIMARY KEY("orderID" AUTOINCREMENT),
	CONSTRAINT "Klients" FOREIGN KEY("customerID") REFERENCES "Customer"("CustomerID")
);
```

INSERT
```sql
INSERT INTO "Employee" ("firstName", "lastName") VALUES ("Vārds", "Uzvārds"), ("Vārds", "Uzvārds")
```

UPDATE:
```sql
UPDATE "Employee" SET "firstName" = "Jānis" WHERE "employeeID" == 10
```

SELECT --  
Iegūt visus elementus:
```sql
SELECT * FROM "Employee"
```
Komentāri:
```sql
-- asd
/*
asd
asd
*/
```

Select ar filtru:
```sql
SELECT "employeeID", "lastName", "firstName" FROM "Employee" WHERE "employeeID" < 4 OR "employeeID" > 6
ORDER BY "firstName" DESC
LIMIT 2;
```

GROUP BY
```sql
SELECT "employeeID", "lastName", "firstName", "birthDate", count("lastName")
FROM "Employee" WHERE "employeeID" < 4 OR "employeeID" > 6 GROUP BY "lastName"
```

Nākošajā nodarbībā - JOINS & Unions