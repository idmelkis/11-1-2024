# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli,
# un spuldzi tajā.

class Spuldze:
    elektrības_patēriņš :float = 0.0
    ieslēgts: bool
    krāsa: str
class Lampa:
    spuldze: Spuldze = None
    ieslēgts: bool
    krāsa: str

# Polimorfisms
from enum import Enum
class Krāsa(Enum):
    SARKANA = 1,
    ZAĻA = 2
class Transportlīdzekļi:
    krasa :Krāsa
    marka :str = ""

    atrums :float = 0.0

    def __init__(self):
        print("Bāzes init!")
    def bazes_funkcija(self):
        print(':)')
    def paatrinat(self):
        self.atrums += 0
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 0

class Automasina(Transportlīdzekļi):
    riepu_skaits :int = 0

    def __init__(self):
        print("Apakšklases init!")
        super().__init__()

    def paatrinat(self):
        self.atrums += 0.5
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 0.5

class Lidmasina(Transportlīdzekļi):
    spārnu_platums :float = 0.0

    def paatrinat(self):
        self.atrums += 4
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 4

bmw = Automasina()
bmw.krasa = Krāsa.SARKANA
print(bmw.krasa.name)
bmw.bazes_funkcija()
bmw.paatrinat()
print(bmw.atrums)

boeing = Lidmasina()
boeing.paatrinat()
print(boeing.atrums)

# Uzdevums: Izveidojiet bāzes klasi, un mantojošo klasi. 
# Tēma: Pēc brīvas izvēles.
# Bāzes klasei divus mainīgos, vienu funkciju (var būt primitīva funkc. ar print())
# Mantojošā klase - vismaz viens unikāls mainīgais, pārrakstām kādu funkciju


# Uzdevums i/ni: Izveidot programmu
# Jāizveido klase "Bankas Konts". 
# * Šai klasei jāglabā informācija par lietotājam pieejamajiem naudas līdzekļiem.
# * Izveidojat funkcijas, kas ļauj ieskaitīt un/vai izņemt naudu no konta
# * Neļaut lietotājam izņemt naudu, ja kontā pēc izņemšanas paliek zem €50
# Izveidojat apakšklasi "Krājkonts" (manto no "Bankas konts").
# * Izmantot polimorfismu lai pārrakstītu izņemšanas funkciju,
#   lai tā kopā ar izņemto naudu izņem vēl 5% (t.i. izņemot €100, izņems €105).
#   (prasība par 50 eur minimumu paliek spēkā)
# Izveidojat apakšklasi (klasei "Bankas konts") "Akciju konts". 
# Šis konts satur arī sarakstu ar akcijām.
# * Akcijas tiek definētas: nosaukums, to skaits (cik pieder)
# * Izveidojat funkciju, kas izvada informāciju par to cik nauda, 
#   cik un kādas akcijas ir īpašniekam.

# Izveidojat objektus no šīm klasēm
# Izsaucat pirmās klases ieskaitīšanas funkciju (€100),
#   izsaucat izņemšanas funkciju €40.
# Izsaucat otrās klases ieskaitīšanas funkciju (€100), 
#   un izsaucat izņemšanas funkciju €90
# Izvadat pirmo divu kontu atlikumus

# Izsaucat trešās klases ieskaitīšanas funkciju (€100),
# Izvadat informāciju par trešo kontu
