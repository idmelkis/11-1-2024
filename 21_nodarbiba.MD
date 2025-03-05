# Lasāmviela

* Vizuāls attēlojums JOINiem - https://miro.medium.com/v2/0*Nrjozs1i0XIiACKd.png
* JOIN operatoru tabula - https://www.sqlite.org/syntax/join-operator.html

# Vaicājumi

Unions -- apvieno rezultātus no vairākiem vaicājumiem -- abiem vaicājumiem rezultātā jābūt vienādam kolonu skaitam

```sql
SELECT "Id", "Vards", "Amats", "Nostradats" FROM "Darbinieks" -- 1. vaicājums
UNION
SELECT "employeeID", "firstName", "lastName", "birthDate" FROM "Employee"; -- 2. vaicājums
```

JOINS -- apvieno rezultātus no vairākām tabulām
```sql
SELECT * FROM "Darbinieks" CROSS JOIN "Employee"; -- CROSS JOIN -- Katrai vērtībai no vaicājuma atbilst vērtības no tabulas vai vaicājuma (šajā gadījumā tabulas Employee -- vaicājums būtu iekavās).
SELECT * FROM "Darbinieks" A LEFT JOIN "Employee" B ON A."Id" == B."employeeID"; -- Izvēlās visas vērtības no "darbinieks", ja ir vērtība ar vienādu ID iekš "Employee", izvada to, citādi - izvada NULL. Rezultātā ir visas abu tabulu kolonas.
SELECT * FROM "Darbinieks" A RIGHT JOIN "Employee" B ON A."Id" == B."employeeID"; -- Līdzīgs LEFT JOIN, bet izvada visas vērtības labās puses tabulai (šajā gadījumā "Employee"), un saistītās kolonas no "Darbinieks" (ja ir, ja nav - NULL).
SELECT * FROM "Darbinieks" A INNER JOIN "Employee" B ON A."Id" == B."employeeID"; -- Izvēlās visas vērtības no "darbinieks", un vērtība ar vienādu ID iekš "Employee". Izvada tikai vērtības kurām izpildās pārbaude.
SELECT * FROM "Darbinieks" A FULL JOIN "Employee" B ON A."Id" == B."employeeID"; -- Izvēlās vērtības no abām tabulām - ja ir atbilstība, tad izvada abu tabulu vērtības. Ja nav atbilstība, tad izvada NULL šīs tabulas kolonām.

SELECT A.Id, B.employeeID -- Kolonu izvēle ļauj izvēlēties no visām rezultāta kolonām, norādot no kuras tabulas nāk kolona
FROM "Darbinieks" A RIGHT JOIN "Employee" B ON A."Id" == B."employeeID"
WHERE B.employeeID < 4; -- WHERE nostrādā pēc JOIN, un ļauj izvēlēties no abām kolonām.
```

DELETE - dzēst rindu
```sql
DELETE FROM "Employee" WHERE "employeeID" == 8;
```

DROP TABLE - izdzēš tabulu
```sql
DROP TABLE "Order_2";
```

# Uzdevumi

* Piemēra datu bāze "Chinook": https://s.ayy.lv/chinook

1. Uzdevums - Uzrakstīt vaicājumu, kas izvada Albumus ar to autoru nosaukumiem.
(Tabula Album + tabula Artist).

Risinājums:
```sql
SELECT A."Title", B."Name" FROM Album A INNER JOIN Artist B ON A.ArtistId == B.ArtistId;
```

2. Uzdevums - Izvēlēties kādu tabulu, izveidot tai kopiju, un pārkopēt datus no oriģināla uz jauno tabulu.
Hint - pie INSERT VALUES ir SELECT vaicājums

Risinājums
```sql
-- Izveidojam tabulas "Artist" kopiju
CREATE TABLE IF NOT EXISTS "Artist_2" (
	"ArtistId"	INTEGER NOT NULL,
	"Name"	NVARCHAR(120),
	CONSTRAINT "PK_Artist" PRIMARY KEY("ArtistId" AUTOINCREMENT)
);

-- Pārkopējam visas vērtības no "Artist" uz "Artist_2"
INSERT INTO "Artist_2" ("Name") SELECT "Name" FROM "Artist";
```