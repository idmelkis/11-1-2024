saraksti = []
kortezs = () # tuple

# Atslēga => Vērtība
atslega = "key"
vertiba = "value"
vardnica = {
    "atslēga": "vērtība",
    "atslēga1": "vērtība2",
    1: "2",
    3: 6,
    atslega: vertiba
}
print(vardnica["atslēga"])
print(vardnica[1])
print(vardnica["key"])
print(vardnica[atslega])

cilveks = {
    "vārds": "Jānis",
    "uzvārds": "Egle",
    # ...
}

# Uzdevums: Izmantot vārdnīcas lai pārveidotu tekstā burtus āēīū
# formā bez garumzīmes, t.i. aeiu
burti = {
    "ā": "a",
    "ē": "e",
    "ī": "i",
    "ū": "u",
}
def changeLetter(text):
    result = ""
    for letter in text:
        if letter in burti:
            result += burti[letter]
        else:
            result += letter
    return result
print(changeLetter("Māja"))
print(changeLetter("Skolēns"))
print(changeLetter("Atzīme"))

print(burti.keys())
print(burti.values())
print(burti.items())
for j,k in burti.items():
    print(f"Atslēga: {j}, Vērtība: {k}")

saraksts = {}
saraksts["key1"] = "vērtība"
saraksts.update({"key2": "vērtība", "key3": "vērtība"})
print(saraksts)


# Uzdevums
# Uzrakstīt programmu, kas izveido vārdnīcu, kurā atslēgas 
# ir ar ciklu atslēgās ievietoti skaitļi no 1 līdz n 
# (lietotāja ievadīts skaitlis) un vērtības ir šis skaitlis kvadrātā.
# Piem. ja n = 3, tad
# {1:1, 2:4, 3:9}
saraksts = {}
n = int(input("Skaitlis līdz: "))
for iii in range(1, n+1):
    saraksts[iii] = iii*iii
    #saraksts.update({iii: iii*iii})
print(saraksts)

# Uzdevums: Pacelt vērtības iekš dotās vārdnīcas kvadrātā
# Hint: Vajadzēs izmantot vienu no šīm funkcijām
# print(<>.keys())
# print(<>.values())
# print(<>.items())
vardnica = {
    1: 1,
    "a": 2,
    3: 3
}
# Piem. 
# vardnica = {
#     1: 1,
#     "a": 4,
#     3: 9
# }
for atslega, vertiba in vardnica.items():
    vardnica[atslega] = vertiba * vertiba
print(vardnica)

# Uzdevums:
# Ar vienu vai vairākiem cikliem apvienot vārdnīcas
# iekš mainīgā dict3 (jāievieto dict1 un dict2 vērtības iekš dict3)
dict1 = {
    1: 10,
    2: 20,
    3: 30
}
dict2 = {
    4: 40,
    5: 50,
    6: 60
}
dict3 = {}

for atslega, vertiba in dict1.items():
    dict3[atslega] = vertiba
for atslega, vertiba in dict2.items():
    dict3[atslega] = vertiba
print(dict3)

# VAI
#for iii in (dict1, dict2):
#    dict3.update(iii)

if 1 in dict3: # vai dict3 ir atslēga '1'
    del dict3[1] # izdzēst vērtību ar atslēgu 1 no dict3
    # vai
    #dict3.pop(1)
print(dict3)

# Uzdevums: (Dots) Tiek ģenerēts saraksts ar 20 vērtībām
# Ar ciklu izdzēst katru otro vērtību
# Vārdnīcas garums: len(vardnica)
import random
vardnica = {}
for iii in range(0, 20):
    vardnica[iii] = random.randint(1, 10)
print(vardnica)

# 1. variants
# for iii in range(0, 20, 2):
#     del vardnica[iii]

i = 0
n = len(vardnica)
keys = list(vardnica.keys())
while i < n:
    if i%2 == 0:
        atslega = keys[i]
        del vardnica[atslega]
    i += 1
# 2. 