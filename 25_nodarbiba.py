# Chinook db fails: https://s.ayy.lv/chinook

import sqlite3
con = sqlite3.connect("chinook.sqlite")
cur = con.cursor()

# 1. Uzdevums
# Iegūt no tabulas "Employee" visus cilvēku vārdus, uzvārdus un e-pastus.
#query = "SELECT FirstName, LastName, Email FROM Employee"
#cur.execute(query)
#print(cur.fetchall())

# 2. Uzdevums
# Iegūt māksliniekus/grupas no tabulas "Artist" kuriem nosaukumā (kolona "Name") ir vārds "Black".
# query = "SELECT Name FROM Artist WHERE \"Name\" LIKE \"%Black%\""
# cur.execute(query)
# print(cur.fetchall())

# 3. Uzdevums
# Iegūt pirmos 3 ierakstus no tabulas "InvoiceLine" kur kolonas "InvoiceId" vērtība ir 3
# 1. var
#query = "SELECT * FROM InvoiceLine WHERE InvoiceId == 3 LIMIT 3"
#cur.execute(query)
#print(cur.fetchall())
# 2. var
#query = "SELECT * FROM InvoiceLine WHERE InvoiceId == 3"
#cur.execute(query)
#print(cur.fetchmany(3))

# 4. Uzdevums 
# Izvadīt dziesmas nosaukumu no tabulas "Track" un tā žanru (tabula "Genre" ir saistīta ar Track.GenreId)
# query = "SELECT a.Name, b.Name FROM Track a INNER JOIN Genre b ON a.GenreId == b.GenreId"
# cur.execute(query)
# print(cur.fetchall())

# 5. Uzdevums
# Izvadat no tabulas "Customer" informāciju pa to cik klienti ir katram atbalsta personālam (Id tiek glabāts kolonā "SupportRepId", Personāla informācija ir tabulā "Employee"). Izvade - Darbinieka vārds, klientu skaits.
query = "SELECT b.FirstName, COUNT(*) FROM Customer a INNER JOIN Employee b ON a.SupportRepId == b.EmployeeId GROUP BY a.SupportRepId"
cur.execute(query)
print(cur.fetchall())

cur.close()
con.commit()
con.close()