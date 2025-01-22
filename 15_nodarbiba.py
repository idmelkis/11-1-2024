class BankasKonts:
    atlikums :float = 0.0
    def __init__(self):
        self.atlikums = 0.0
    def iznem(self, summa):
        if (self.atlikums - summa >= 50):
            self.atlikums -= summa
        else:
            print("Kļūda: nepietiek līdzekļi")
    def ielikt(self, summa):
        self.atlikums += summa
    def __str__(self):
        return(f"Atlikums:\t{self.atlikums}")

class KrajKonts(BankasKonts):
    def iznem(self, summa):
        iznemtaSumma = summa * 1.05
        super().iznem(iznemtaSumma)
   
class Akcija:
    nosaukums: str
    skaits: str
    def __init__(self, nosaukums, skaits = 0):
        self.nosaukums = nosaukums
        self.skaits = skaits
        super().__init__()
class AkcijuKonts(BankasKonts):
    akcijas :'list[Akcija]'
    def __init__(self):
        self.akcijas = []
    def pievienot_akcijas(self, akcija):
        self.akcijas.append(akcija)
    def __str__(self):
        izvade = f"Klientam ir EUR {self.atlikums}, un {len(self.akcijas)} akcijas!"
        for akcija in self.akcijas:
            izvade += f"\nNosaukums:\t{akcija.nosaukums}\nSkaits:\t{akcija.skaits}"
        return izvade

konts1 = BankasKonts()
konts1.ielikt(100)
konts1.iznem(40)
print(konts1)

konts2 = KrajKonts()
konts2.ielikt(100)
konts2.iznem(90)
print(konts2)

konts3 = AkcijuKonts()
konts3.ielikt(100)
konts3.pievienot_akcijas(Akcija("MSFT", 1))
print(konts3)

# 1. Uzdevums
class Prece:
    nosaukums: str
    cena: float
    def __init__(self, nosaukums, cena):
        self.nosaukums = nosaukums
        self.cena = cena
class Grozs:
    preces: 'list[Prece]'
    def __init__(self):
        self.preces = []
    def pievienot(self, prece):
        self.preces.append(prece)
    def iznemt(self, prece :Prece):
        for idx in range(0, len(self.preces)):
            if prece.nosaukums == self.preces[idx].nosaukums:
                self.preces.pop(idx)
                break
    def aprekinatVertibu(self):
        sum = 0.0
        for prece in self.preces:
            sum += prece.cena
        return sum


class Darbinieks:
    id :str
    vards :str
    alga :float
    amats :str
    nostradats :int
    def __init__(self, id, vards, alga, amats, nostradats):
        self.id = id
        self.vards = vards
        self.alga = alga
        self.amats = amats
        self.nostradats = nostradats
    def __str__(self):
        return f"{self.vards} - {self.amats}, pelna {self.alga} EUR/mēn, strādā {self.nostradats} mēnešus."
    def izmaksataAlga(self):
        return self.nostradats * self.alga

janis = Darbinieks("01", "Jānis", 1000, "Slotas operators", 24)
eriks = Darbinieks("02", "Ēriks", 2000, "Tirgotājs",	30)
anna = Darbinieks("03", "Anna",  500,  "Laborante",	2)
karlis = Darbinieks("04", "Kārlis", 9001, "Direktors", 36)

print(janis)
print(eriks)
print(anna)
print(karlis)
print(karlis.izmaksataAlga())