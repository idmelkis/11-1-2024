# Izveidot vārdnīcu, kurā atrodas atslēgas un vērtības no dict1 (izveidots
# ar kodu augstāk), tām atslēgām kurām vērtības ir > 500, un izprintēt to.
# Piem, ja
# dict1 = {
#   1: 100,
#   2: 600,
#   3: 200,
#   4: 800
# }, tad
# dict2 = {
#   2: 600,
#   4: 800
# }
import random
dict1 = {}
for i in range(0, 20):
    dict1[i] = random.randint(0, 1000)
print(dict1)
dict2 = {}
for key,val in dict1.items():
    if val > 500:
        dict2[key] = val
print(dict2)

# Uzdevums
# Apvienot abus sarakstus lai izveidotu vārdnīcu
# Garantēts, ka abi saraksti būs vienāda garuma
keys = [ 1, 2, "10", 3, random.randint(0, 100) ]
values = [ "viens", 4, False, [1,3,4], random.randint(0, 100) ]
# piem.
# dict = { 1: "viens", 2: 4 ...}
new_dict = {}
for iii in range(0, len(keys)):
    new_dict[keys[iii]] = values[iii]
print(new_dict)

# print(dict(zip(keys, values)))


vardn = {
    'V': 10,
    'VI': 10,
    'VII': 40,
    'VIII': 20,
    'IX': 70,
    'X': 80,
    'XI': 40,
    'XII': 20
}
# Izveidot programmu, kura ar ciklu izveido vārdnīcu, kura satur skaitu
# tam, cik reizes atkārtojas vērtības vārdnīcā. (piem. 10 atkārtojas 2x,
# 20 atkārtojas 2x utt.). Izvadīt rezultātu. 
# piem.
# rez = {
#    10: 2
#    20: 2
#   ...
#    80: 1
#}
rez = {}
for value in vardn.values():
    if value in rez:
        rez[value] += 1
    else:
        rez[value] = 1
print(rez)

# darbs(i/ni)
# Dots saraksts ar vārdnīcām
cilveki = [{
 "vārds": "Jānis",
 "uzvārds": "Bērziņš",
 "vecums": 18
}, {
 "vārds": "Pēteris",
 "uzvārds": "Egle",
 "vecums": 14
}, {
 "vārds": "Andris",
 "uzvārds": "Lācis",
 "vecums": 20
}]
#Uzrakstat programmu, kas ļauj lietotājam meklēt
# cilvēku pēc vārda vai uzvārda
# Atrasto cilvēku (vai cilvēkus) izvadīt.
# Pārbaudei var izmantot if <teksts> in <vārds/uzvārds> konstrukciju, 
# var nebūt pārāk sarežģīts.