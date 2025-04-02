# Dokumentācija: https://docs.python.org/3/library/sqlite3.html
# SQL Injekcija: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md
import sqlite3

# Atvērt datu bāzi atmiņā
#con = sqlite3.connect(":memory:")

con = sqlite3.connect("23_nodarbiba.db")
cur = con.cursor()

# SELECT
# cur.execute("SELECT * FROM Tabula")
# cur.executemany()

#cur.fetchmany(3)
#cur.fetchone()
# for row in cur.fetchall(): # Atgriež tuple
#     print(row)

# INSERT
# NEKAD NEĻAUJAM LIETOTĀJAM PA TAISNO IEVADĪT VĒRTĪBAS VAICĀJUMĀ
#ievade = input("...")
#ievade = "otrā vērtība'), ('trešā vērtība"
#query = f"INSERT INTO 'Tabula' ('Vert') VALUES ('{ievade}')"
#cur.execute(query)

#ievade = "otrā vērtība'), ('trešā vērtība"
# Parameterizētais vaicājums
#parametri = (ievade)
#query = "INSERT INTO 'Tabula' ('Vert') VALUES (?)"
# Parameterizētais vaicājums ar nosaukumiem
# parametri = (
#     {"nosaukums": ievade, "id": -1}
# )
# query = "INSERT INTO 'Tabula' ('Vert') VALUES (:id, :nosaukums)"
# cur.execute(query, parametri)

# cur.close()
# con.commit()
# con.close()

###########

class Lietotajs:
    def __init__(self, id, lietotajvards, parole, epasts):
        self.id = id
        self.lietotajvards = lietotajvards
        self.parole = parole
        self.epasts = epasts
    def __str__(self):
        return f"Lietotajs({self.id}, '{self.lietotajvards}', '{self.parole}', '{self.epasts}')"
    def uz_vaicajumu(self):
        return (self.id, self.lietotajvards, self.parole, self.epasts)
    def jauna_vertiba(self):
        return (self.lietotajvards, self.parole, self.epasts)
    @classmethod
    def no_vaicajuma(cls, *args):
        args = args[0]
        return cls(args[0], args[1], args[2], args[3])

lietotajs_1 = Lietotajs(1, "Lietotajvards", "******", "mail@mail.com")

con = sqlite3.connect("23_nodarbiba.db")
cur = con.cursor()
 
# Tabulas izveide
query = 'CREATE TABLE IF NOT EXISTS "Lietotajs" (\
	"Id"	INTEGER NOT NULL UNIQUE,\
	"Lietotajvards"	TEXT NOT NULL,\
	"Parole"	TEXT NOT NULL,\
	"Epasts"	TEXT,\
	PRIMARY KEY("Id" AUTOINCREMENT)\
);'
cur.execute(query)

# Datu ievietošana
# query = "INSERT INTO Lietotajs(Lietotajvards, Parole, Epasts) VALUES(?, ?, ?)"
#cur.execute(query, lietotajs_1.uz_vaicajumu())
#cur.executemany(query, (lietotajs_1.jauna_vertiba(), lietotajs_1.jauna_vertiba()))

# Pēdējās vērtības iegūšana
query = "SELECT * FROM Lietotajs ORDER BY Id DESC LIMIT 1"
cur.execute(query)
rezultats = cur.fetchone()
#lietotajs_2 = Lietotajs(rezultats[0], rezultats[1], rezultats[2], rezultats[3])
# Alt metode - labāk izskatās, bet praktiski tas pats
lietotajs_2 = Lietotajs.no_vaicajuma(rezultats)
print(lietotajs_2)

# Atjaunināšana -- Automatizēt var, bet sarežģīti
#lietotajs_2.epasts = "jauns@epasts.com"
#query = 'UPDATE "Lietotajs" SET "epasts" = "?" WHERE "Id" == 3'
#cur.execute(query, lietotajs_2.epasts)

# Dzēšana
#query = 'DELETE FROM Lietotajs WHERE Id = 3'
#cur.execute(query)

cur.close()
con.commit()
con.close()