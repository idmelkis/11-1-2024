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
    
# Uzdevums:
# Pievienot profila funkcionalitāti.
# 1. Izveidot jaunu tabulu (Profils) - 
# Lauki - Id, LietotajaId, Vards, Uzvards, ParMani
# LietotajaId vajadzētu būt saistīts ar Lietotajs.Id (ON DELETE CASCADE)

# Ja lietotājs programmā ir autentificējies, tad
# Lietotājam vajadzētu varēt izvadīt savu profilu (ja tāds ir).
# Lietotājam vajadzētu varēt izveidot vai izmainīt (ja tāds ir) savu profilu.

lietotajs = None
while True:
    if lietotajs is not None:
        print(lietotajs)

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