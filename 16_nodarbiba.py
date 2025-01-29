class Darbinieks:
    vards :str
    uzvards :str
    stazs :int
    alga :float
    amats :str
    def __init__(self, vards, uzvards, stazs, alga, amats):
        self.vards = vards
        self.uzvards = uzvards
        self.stazs = stazs
        self.alga = alga
        self.amats = amats
    def aprekiniBonusu(self):
        return 0
    def aprekiniKopalgu(self):
        return self.alga * self.stazs + self.aprekiniBonusu()
    def __str__(self):
        return f"{self.vards} {self.uzvards} nopelna {self.aprekiniKopalgu()}"
class Menedzeris(Darbinieks):
    darbinieki :int
    def __init__(self, vards, uzvards, stazs, alga, amats, darbinieki):
        self.darbinieki = darbinieki
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.darbinieki * 100
class Programmetajs(Darbinieks):
    projekts :str
    def __init__(self, vards, uzvards, stazs, alga, amats, projekts):
        self.projekts = projekts
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.alga * 0.10
class Testetajs(Darbinieks):
    projekts :str
    stunduSkaits :float
    def __init__(self, vards, uzvards, stazs, alga, amats, projekts, stunduSkaits):
        self.projekts = projekts
        self.stunduSkaits = stunduSkaits
        super().__init__(vards, uzvards, stazs, alga, amats)
    def aprekiniBonusu(self):
        return self.alga * 0.5
    def aprekiniKopalgu(self):
        return self.stunduSkaits * 7 + self.aprekiniBonusu()
janis = Menedzeris("Jānis", "Uzvārds", 10, 10, "Menedžeris", 10)
pēteris = Programmetajs("Pēteris", "Uzvārds", 10, 10, "Menedžeris", "Proj1")
gunita = Testetajs("Gunita", "Uzvārds", 1, 0, "Testētājs", "Proj1", 10)
print(janis)
print(pēteris)
print(gunita)

# 1. Uzd
class Galdins:
    numurs :int
    aiznemts :bool
    pirkumi :'list[str]'
    def __init__(self, numurs):
        self.numurs = numurs
        self.aiznemts = False
        self.pirkumi = []
    def pievienot_pirkumu(self, pirkums):
        self.pirkumi.append(pirkums)
class Restorans:
    edieni :'dict[str, float]'
    galdini :'list[Galdins]'
    def __init__(self):
        self.edieni = {}
        self.galdini = []
    def pievienot_edienu(self, nosaukums, cena):
        self.edieni[nosaukums] = cena
    def izvadit_edienkarti(self):
        print("Ēdienkarte:")
        for ediens, cena in self.edieni.items():
            print(f" - {ediens}: {cena}")
        print("===========")
    def pievienot_galdinu(self, galdins :Galdins):
        self.galdini.append(galdins)
    def rezervet_galdinu(self, numurs):
        for galdins in self.galdini:
            if galdins.numurs == numurs:
                if not galdins.aiznemts:
                    galdins.aiznemts = True
                    print(f"Galdiņš {numurs} tika rezevēts!")
                else:
                    print("Galdiņš jau ir aizņemts!")
                break
    def registret_pirkumu(self, numurs, pirkums):
        atrasts = False
        for galdins in self.galdini:
            if galdins.numurs == numurs:
                atrasts = True
                if galdins.aiznemts:
                    galdins.pievienot_pirkumu(pirkums)
                else:
                    print("Galdiņš nav aizņemts!")
                break
        if not atrasts:
            print("Nav šāda galdiņa!")
    def izvadit_galdinus(self):
        print("Galdiņi:")
        for galdins in self.galdini:
            print(f" - Nr. {galdins.numurs} (Aizņemts: {galdins.aiznemts}). Pirkumi: ")
            for pirkums in galdins.pirkumi:
                print(f"    - {pirkums}")
        print("===========")

restorans = Restorans()
galds = Galdins(1)
restorans.pievienot_galdinu(galds)
restorans.pievienot_edienu("Maize", 0.6)
restorans.pievienot_edienu("Ūdens", 1.0)
restorans.izvadit_edienkarti()
restorans.rezervet_galdinu(1)
restorans.registret_pirkumu(1, "Maize")
restorans.izvadit_galdinus()
