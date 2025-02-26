Uzdevums: uzrakstīt SQL vaicājumus, lai izveidotu sekojošo klasi kā tabulu, un uzrakstīt vaicājumus lai ievietotu tabulā apakšā esošos datus.

```py
class Darbinieks:
    id :int
    vards :str
    alga :float
    amats :str
    nostradats :int

janis = Darbinieks(1, "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks(2, "Ēriks", 2000, "Tirgotājs",	30)
anna = Darbinieks(3, "Anna",  500,  "Laborante",	2)
karlis = Darbinieks(4, "Kārlis", 9001, "Direktors", 36)
```

Risinājums:
```sql
CREATE TABLE IF NOT EXISTS "Darbinieks" (
	"Id" INTEGER NOT NULL,
	"Vards" TEXT,
	"Alga" REAL,
	"Amats" TEXT,
	"Nostradats" INTEGER,
	PRIMARY KEY ("Id" AUTOINCREMENT)
);
INSERT INTO "Darbinieks" ("Vards", "Alga", "Amats", "Nostradats") 
VALUES ("Jānis", 1000, "Slotas operators", 24), ("Ēriks", 2000, "Tirgotājs", 30),
("Anna",  500,  "Laborante", 2), ("Kārlis", 9001, "Direktors", 36);
```

Uzdevums (turpinājums): Izveidot tabulu projekti, kurš satur informāciju par projekta nosaukumu un identifikatoru. Realizēt darbinieku saistību ar vairākiem projektiem.

Risinājums:
```sql
CREATE TABLE IF NOT EXISTS "Darbinieks" (
	"Id" INTEGER NOT NULL,
	"Vards" TEXT,
	"Alga" REAL,
	"Amats" TEXT,
	"Nostradats" INTEGER,
	PRIMARY KEY ("Id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "Projekts" (
	"Id" INTEGER NOT NULL,
	"Nosaukums" TEXT,
	PRIMARY KEY ("Id" AUTOINCREMENT)
);

CREATE TABLE IF NOT EXISTS "DarbiniekaProjekti" (
	"Darbinieka_Id" INTEGER NOT NULL,
	"Projekta_Id" INTEGER NOT NULL,
	FOREIGN KEY("Darbinieka_Id") REFERENCES "Darbinieks"("Id") ON DELETE RESTRICT,
	FOREIGN KEY("Projekta_Id") REFERENCES "Projekts"("Id") ON DELETE RESTRICT
);
```

Nākošajā nodarbībā - JOINS & Unions