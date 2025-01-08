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

# objekts = Automasina("Sarkans", "BMW")
# objekts2 = Automasina("Zils", "Audi")
# print(objekts.getAtrums())
# print(objekts)
# print(objekts.__dict__)
#Automasina.klasesmetode()

# Programma - simulācija kurā automašīnu var braukt (paātrināt un bremzēt)
# nobraukts = 0.0
# masina = Automasina("kaut kada", "masina")
# while True:
#     i = input() # Problēma: bloķē ciklu, idejiski vajadzētu nebloķējošu ievadi.
#     if i == "w":
#         masina.paatrinat()
#     elif i == "s":
#         masina.bremzet()

#     nobraukts += masina.getAtrums()
#     print(f"masina {masina.krasa} {masina.marka} ir nobraukusi {nobraukts},\
# paslaik brauc ar atrumu {masina.getAtrums()}")

# Uzdevums: 
# Izveidot klasi, kas aprakstītu priekšmetu e-klasē
# Vismaz 4 mainīgie, un 2 funkcijas kas strādā ar šiem datiem.
# Izveidojat objektu, un uzrakstat kodu, kas pielieto šīs funkcijas.
class Skolens:
    vards = ""
    def __init__(self, vards, uzvards):
        self.vards += vards + " " + uzvards
class Nodarbiba:
    datums :str = ""
    tema :str = ""
    def __init__(self, datums, tema):
        self.datums = datums
        self.tema = tema
class Prieksmets:
    nosaukums :str = ""
    skolotajs :str = ""
    skoleni :'list[Skolens]' = []
    nodarbibas :'list[Nodarbiba]' = []
    def __init__(self, nosaukums, skolotajs):
        self.nosaukums = nosaukums
        self.skolotajs = skolotajs
    def __str__(self):
        return f"Priekšmets {self.nosaukums} ar {len(self.skoleni)} skolēniem."
    
    def izveidotNodarbibu(self, datums :str, tema :str):
        self.nodarbibas.append(Nodarbiba(datums, tema))
    def pievienotSkolenu(self, skolens :Skolens):
        self.skoleni.append(skolens)

programmesana = Prieksmets("Programmēšana I", "Ingmārs")
programmesana.pievienotSkolenu(Skolens("Jānis", "Bērziņš"))
print(programmesana)

fizika = Prieksmets("Fizika", "Mihno")
fizika.pievienotSkolenu(Skolens("Jānis", "Bērziņš"))
print(fizika)

# Uzdevums 2: 
# Uzrakstīt klasi "Lampa", kas apraksta lampu, un spuldzi tajā.
# Lampas objektam vajadzētu uzglabāt informāciju par lampas stāvokli,
# un spuldzi tajā.