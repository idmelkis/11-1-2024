# Uzdevums: Uzrakstat programmu, 
# kurā lietotājs ievada vairāku cilvēku datus (vārds; uzvārds, vecums). 
# Visiem laukiem jābūt atsevišķi 
# (t.i. neapvienojat vārdu un uzvārdu).
# Individuālu cilvēka dati jāsaglabā vārdnīcā. 
# Vārdnīcas jāapvieno sarakstā.
# Saglabājat šos datus failā. 
# Uzsākot programmu izvadat šos datus ja fails eksistē.
# import os
# import json
# if os.path.isfile(f"nosaukums.json"):
#     with open("nosaukums.json", "r", encoding="UTF-8") as f:
#         saraksts = json.load(f)
#         print(saraksts)
# else:
#     print(f"Fails nosaukums.json nav atrasts")

# cilveki = []
# while True:
#     vards = input("Vārds: ")
#     uzvards = input("Uzvārds: ")
#     vecums = int(input("Vecums: "))
#     cilveks = {
#         "vards": vards,
#         "uzvards": uzvards,
#         "vecums": vecums,
#     }
#     cilveki.append(cilveks)

#     if input("Beigt?") == "jā":
#         break

# with open("nosaukums.json", "w", encoding="UTF-8") as f:
#     json.dump(cilveki, f)

#import os
# Pārbauda vai eksistē fails
#os.path.isfile(f"nosaukums.json")
# Pārbauda vai eksistē mape
#os.path.isdir("mape")
# Pārbauda vai eksistē mape VAI fails
#os.path.exists("Ceļš/uz/failu/vai/mapi")

#import os
#faila_mape = os.path.dirname(__file__)

#import sys
#print(sys.argv[0])
#faila_mape = os.path.dirname(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
# argc - argument count
# argv - argument vector

# Absolūtie failu ceļi
# piem. C:\Users\user\Desktop\11-1-2024\10_nodarbiba.py

# Relatīvie failu ceļi
# Piemēram, ja mēs atrodamies "C:\Users\user\Desktop\11-6-2024"
# Lai nokļūtu mapē "C:\Users\user\Desktop\11-1-2024"
# Mēs varam izmantot relatīvo ceļu "..\11-1-2024"
# . - Pašreizējā mape
# .. - Vienu līmeni augstāk
# ..\.. - Divus līmeni augstāk
# u.t.t.

# Var miksēt, piem.
# with open("C:\Users\user\Desktop\11-1-2024\..\..\nosaukums.json", "w", encoding="UTF-8") as f:
# Saglabās failu mapē "C:\Users\user\"

# Piem.
# import os
# faila_mape = os.path.dirname(__file__)
# with open(f"{faila_mape}\\..\\..\\nosaukums.json", "w", encoding="UTF-8") as f:
#     f.write("!")

# Iegūstam ceļu augstākā līmenī
# import pathlib
# p = pathlib.Path("Ceļš\\līdz\\failam")
# p.parents[0] # "Ceļš\\līdz"
# p.parents[1] # "Ceļš"

# Failu dzēšana
# import os
# with open("nosaukums.json", "w", encoding="UTF-8") as f:
#     0_0
# os.remove("nosaukums.json") # rm komanda - iekš konsoles

# Mapju izveide
# import os
# if not os.path.isdir("test"):
#     os.mkdir("test")
#     #os.makedirs("test/test2/test4")

# # Variants 1 mapju (ar failiem) dzēšanai:
# for file in os.listdir("test"): # listdir izvada relatīvos ceļus ievadītajai mapei
#     os.remove(f"test\\{file}") # tādēļ manuāli jāpievieno ceļš līdz šai mapei iekš .remove funkcijas
# os.rmdir("test")

# Variants 2:
# import shutil # shell utils
# shutil.rmtree("test") # Izdzēš mapi ar visiem failiem tajā

# Uzdevums: Uzrakstat programmu kura izveido mapi "mape"
# Mapē izveidojat failus ar nosaukumiem no 1 līdz 100
import os
faila_mape = os.path.dirname(__file__)
if not os.path.isdir(f"{faila_mape}\\mape"):
    os.mkdir("mape")
for iii in range(1, 101):
    with open(f"{faila_mape}\\mape\\{iii}", "w") as f:
        pass

# Turpināsim nākošajā stundā...