# Lasāmviela

* https://www.sqlite.org/lang_datefunc.html

# Uzdevumi

* Piemēra datu bāze "Chinook": https://s.ayy.lv/chinook

1. Uzrakstat vaicājumu, kas izvada visus rēķinus (Tabula `Invoice`), kuru identifikators ir lielāks par 400, un kuru vērtība (kolona `Total`) ir lielāka par 5.00

```sql
SELECT * FROM Invoice WHERE Invoice.InvoiceId > 400 AND Invoice.total > 5.00;
```

2. Uzrakstat vaicājumu, kas izvada visus rēķinus (Tabula `Invoice`) no 2009. gada līdz 2011. gadam.

```sql
-- Datuma & laika funkcija: datetime(<datums teksta, vai unix formātā>);
                         -- datetime('2009-01-01 00:00:00')
SELECT * FROM "Invoice" WHERE InvoiceDate 
BETWEEN datetime('2009-01-01 00:00:00') AND datetime('2011-01-01 00:00:00')
```

2.1. Izmainat iepriekšējo vaicājumu, lai izvadītu šajā laika posmā izrakstīto rēķinu skaitu

```sql
SELECT count(*) FROM "Invoice" WHERE InvoiceDate 
BETWEEN datetime('2009-01-01 00:00:00') AND datetime('2011-01-01 00:00:00')
```

3. Uzrakstat vaicājumu, kas izvada cik katrā atskaņošanas sarakstā ir dziesmas (tabula `PlaylistTrack`). Pietiek, ka parāda playlist identifikatoru un dziesmu skaitu (nav jātaisa join lai izvadītu nosaukumu).

```sql
SELECT PlaylistId, count(TrackId) FROM PlaylistTrack GROUP BY PlaylistId
```

3.1. Papildinat iepriekšējo vaicājumu, lai identifikatora vietā tiktu izvadīts playlist nosaukums.

```
SELECT b.Name, count(TrackId) as "Count"
FROM PlaylistTrack a
INNER JOIN Playlist b ON a.PlaylistId == b.PlaylistId
GROUP BY a.PlaylistId
```

# i/ni darbs

Dotas 15min. 2 Vaicājumi - jāatbilst nosacījumiem!

1. Uzrakstat vaicājumu, kas izvada nosaukumu un garumu (sekundēs) visām dziesmām (tabula `Track`), kuras ir garākas par 1min (kolona - `Miliseconds`). Piezīme - tabulā dati ir milisekundēs, izvadē jāpārveido uz sekundēm.
2. Uzrakstat vaicājumu, kas izvada cik daudz rēķini (tabula - `Invoice`) ir katrā valstī (kolona - `BillingCountry`). Rezultātam vajadzētu būt sakārtotam no lielākā uz mazāko.

Iesniegt e-klasē pie šīs stundas.