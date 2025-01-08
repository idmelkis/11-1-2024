# class NosaukumsVards2:
#     vardsVards
#     vards_vards

# Klase - Skice/abstrakcija kaut kam
class Automasina:
    krasa :str = ""
    marka :str = ""

    atrums :float = 0.0
    virziens_x :float = 0.0
    virziens_y :float = 0.0

    def __init__(self, krasa, marka):
        self.krasa = krasa
        self.marka = marka
        print(f"Izveidots objekts: {krasa} {marka}")
    def __str__(self) -> str:
        return f"Mašīna {self.krasa} {self.marka}"

    def getAtrums(self) -> float:
        return self.atrums
    def setAtrums(self, atrums :float) -> None:
        self.atrums += atrums

    @classmethod
    def klasesmetode(cls):
        cls("Zala","Toyota")

    def paatrinat(self):
        self.atrums += 0.5
    def bremzet(self):
        if self.atrums > 0:
            self.atrums -= 0.5

objekts = Automasina("Sarkans", "BMW")
objekts2 = Automasina("Zils", "Audi")
print(objekts.getAtrums())
print(objekts)
print(objekts.__dict__)
#Automasina.klasesmetode()

# Programma - simulācija kurā automašīnu var braukt (paātrināt un bremzēt)
nobraukts = 0.0
masina = Automasina("kaut kada", "masina")
while True:
    i = input() # Problēma: bloķē ciklu, idejiski vajadzētu nebloķējošu ievadi.
    if i == "w":
        masina.paatrinat()
    elif i == "s":
        masina.bremzet()

    nobraukts += masina.getAtrums()
    print(f"masina {masina.krasa} {masina.marka} ir nobraukusi {nobraukts},\
paslaik brauc ar atrumu {masina.getAtrums()}")

