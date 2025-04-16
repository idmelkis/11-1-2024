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
    
class Profils:
    def __init__(self, LietotajaId, vards, uzvards, parmani):
        self.id = id
        self.LietotajaId = LietotajaId
        self.vards = vards
        self.uzvards = uzvards
        self.parmani = parmani
    def __str__(self):
        return f"Profils({self.id}, '{self.vards}', '{self.uzvards}', '{self.parmani}')"
    def uz_vaicajumu(self):
        return (self.id, self.LietotajaId, self.vards, self.uzvards, self.parmani)
    def atjauninat(self):
        return (self.vards, self.uzvards, self.parmani, self.id)
    def jauna_vertiba(self):
        return (self.LietotajaId, self.vards, self.uzvards, self.parmani)
    @classmethod
    def no_vaicajuma(cls, *args):
        args = args[0]
        return cls(args[0], args[1], args[2], args[3], args[4])

# https://github.com/idmelkis/11-1-2024/blob/main/23_nodarbiba.py
import sqlite3
con = sqlite3.connect("24_nodarbiba.db")
cur = con.cursor()

# Tabulas izveide
query = 'CREATE TABLE IF NOT EXISTS "Lietotajs" (\
	"Id"	INTEGER NOT NULL UNIQUE,\
	"Lietotajvards"	TEXT NOT NULL UNIQUE,\
	"Parole"	TEXT NOT NULL,\
	"Epasts"	TEXT,\
	PRIMARY KEY("Id" AUTOINCREMENT)\
);'
cur.execute(query)

# Uzdevums:
# Pievienot profila funkcionalitāti.
# 1. Izveidot jaunu tabulu (Profils) - 
# Lauki - Id, LietotajaId, Vards, Uzvards, ParMani
# LietotajaId vajadzētu būt saistīts ar Lietotajs.Id (FOREIGN KEY - ON DELETE CASCADE)
query = 'CREATE TABLE IF NOT EXISTS "Profils" (\
	"Id"	INTEGER NOT NULL UNIQUE,\
    "LietotajaId"	INTEGER NOT NULL,\
	"Vards"	TEXT NOT NULL,\
	"Uzvards"	TEXT NOT NULL,\
	"ParMani"	TEXT,\
	PRIMARY KEY("Id" AUTOINCREMENT)\
    FOREIGN KEY("LietotajaId") REFERENCES "Lietotajs"("Id") ON DELETE CASCADE\
);'
cur.execute(query)

def lietotaja_izveide(cursor :sqlite3.Cursor) -> Lietotajs:
    # TODO: Kļūdu pārbaude
    lietotajvards = input("Lietotajvards: ")
    # N.B. Vajadzētu veikt jaukšanu -- https://en.wikipedia.org/wiki/Hash_function
    parole = input("Parole: ")
    epasts = input("E-pasts: ")
    query = "INSERT INTO Lietotajs (lietotajvards, parole, epasts) VALUES (?,?,?)"
    cursor.execute(query, (lietotajvards, parole, epasts))

    query = 'SELECT * FROM Lietotajs ORDER BY "Id" DESC LIMIT 1'
    cursor.execute(query)
    rows = cur.fetchall()
    if len(rows) > 0:
        return Lietotajs.no_vaicajuma(rows[0])
    else:
        return None

def lietotaja_autorizacija(cursor :sqlite3.Cursor) -> Lietotajs:
    lietotajvards = input("Lietotajvards: ")
    # N.B. Vajadzētu veikt jaukšanu -- https://en.wikipedia.org/wiki/Hash_function
    parole = input("Parole: ")

    query = 'SELECT * FROM Lietotajs WHERE Lietotajvards == ? AND Parole == ?'
    cursor.execute(query, (lietotajvards, parole))
    rows = cur.fetchall()
    if len(rows) > 0:
        return Lietotajs.no_vaicajuma(rows[0])
    else:
        return None
    
# Ja lietotājs programmā ir autentificējies, tad
# Lietotājam vajadzētu varēt izvadīt savu profilu (ja tāds ir).
def izvadit_profilu(cursor :sqlite3.Cursor, lietotajs :Lietotajs) -> Profils:
    query = 'SELECT * FROM Profils WHERE LietotajaId == ?'
    cursor.execute(query, (lietotajs.id))
    rows = cur.fetchall()
    if len(rows) > 0:
        return Profils.no_vaicajuma(rows[0])
    else:
        return None

# Lietotājam vajadzētu varēt izveidot vai izmainīt (ja tāds ir) savu profilu.
# Pieņemt, ka pagaidām lietotājam ir viens profils
def izvadit_profilu(cursor :sqlite3.Cursor, lietotajs :Lietotajs) -> Profils:
    query = 'SELECT * FROM Profils WHERE LietotajaId == ?'
    cursor.execute(query, (lietotajs.id))
    rows = cur.fetchall()
    profils = None
    if len(rows) > 0:
        profils = Profils.no_vaicajuma(rows[0])
        profils.vards = input("Vārds: ")
        profils.uzvards = input("uzvārds: ")
        profils.parmani = input("Parmani: ")
        query = 'UPDATE "Profils" SET ("Vards", "Uzvards", "Parmani") = (?,?,?), WHERE "Id" == ?'
        cursor.execute(query, profils.atjauninat())
    else:
        print("Jāizveido jauns profils: ")
        vards = input("Vārds: ")
        uzvards = input("uzvārds: ")
        parmani = input("Parmani: ")
        profils = Profils(lietotajs.id, vards, uzvards, parmani)
        query = "INSERT INTO Profils (LietotajaId, Vards, Uzvards, Parmani) VALUES (?,?,?,?)"
        cursor.execute(query, profils.jauna_vertiba())

lietotajs = None
while True:
    if lietotajs is not None:
        print(lietotajs)
        print("Izvēlne: ")
        print("1. Izvadīt profilu")
        print("2. Izveidot profilu")
        print("0. Iziet")

        ievade = int(input("Ievade: "))
        if ievade == 0:
            break
        elif ievade == 1:
            profils = izvadit_profilu(cur, lietotajs)
            if profils is not None:
                print(profils)
            else:
                print("Lietotājam nav profila!")
        elif ievade == 2:
            izvadit_profilu(cur, lietotajs)
    else:
        print("Izvēlne: ")
        print("1. Lietotāja izveide")
        print("2. Lietotāja autorizācija")
        print("0. Iziet")

        ievade = int(input("Ievade: "))
        if ievade == 0:
            break
        elif ievade == 1:
            lietotajs = lietotaja_izveide(cur)
        elif ievade == 2:
            lietotajs = lietotaja_autorizacija(cur)
            if lietotajs == None:
                print("Lietotājs nav atrasts!")

cur.close()
con.commit()
con.close()