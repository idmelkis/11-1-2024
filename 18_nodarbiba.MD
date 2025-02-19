# Noderīgi linki
* [DBMS](https://en.wikipedia.org/wiki/Database)
* [ACID](https://en.wikipedia.org/wiki/ACID)
* [Relacionālās datu bāzes](https://en.wikipedia.org/wiki/Relational_database)
* [SQlite](https://www.sqlite.org/index.html)
* [DB Browser](https://sqlitebrowser.org/)

# Svarīgākie vaicājumu tipi
Tabulas izveide -- CREATE TABLE
Ievietošana -- INSERT  
Atjaunošana -- UPDATE  
Dzēšana     -- DELETE
Datu iegūšana -- SELECT

![Bilde ar dizainu](https://planetscale.com/assets/blog/content/schema-design-101-relational-databases/db72cc3ac506bec544588454972113c4dc3abe50-1953x1576.png)

Piemērs vaicājumam:
```sql
INSERT INTO Employees (employeeID, firstName, lastName) VALUES (1, 'Vārds', 'Uzvārds')
```

Tabulu nosaukumi vienskaitlī - loģiskāk ar klasēm:  
```py
class Employee:
    employeeID

list[Employee]
```

Nākošajā stundā - relācijas