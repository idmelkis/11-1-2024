import json
vardnica = {
    "key": "value",
    "True": True,
    23: 32,
    False: True
}
teksts = json.dumps(vardnica)
print(teksts)
print(vardnica)

#json_str = "{\"123\":true,\"312\":\"World\"}"
json_str = '{"123":true,"312":"World"}'
vardnica_2 = json.loads(json_str)
print(type(vardnica_2))
print(vardnica_2)

# fails = open("nosaukums", "w")
# print("Hello")
# fails.close()

# Open funkcija
# 1. Parametrs - faila nosaukums
# 2. Faila atvēršanas režīms
# r - read (lasam)
# w - write (rakstam - pārraksta faila saturu)
# a - append (rakstam - pievienojam faila galā)
# r+ - raksta (append) + lasa
# w+ - raksta (write) + lasa
# Vairāk informācija: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# 3. Encoding - faila kodējums
import os
#print(os.path.dirname(__file__))
faila_mape = os.path.dirname(__file__)

#with open(f"{faila_mape}\\nosaukums", "r", encoding="UTF-8") as faila_m:
    # Rakstam
    #faila_m.write("234")
    #faila_m.writelines(["123", "311"])
    # Lasam
    # for line in faila_m:
    #     print(line.strip())

    # dati = faila_m.read(5)
    # print(dati)
    # dati = faila_m.read(5)
    # print(dati)

    # dati = faila_m.readlines()
    # print(dati)

vardnica = {
    "key": "value",
    "True": True,
    23: 32,
    False: True
}
#with open(f"{faila_mape}\\nosaukums.json","r", encoding="UTF-8") as f:
    # vardnica_json = json.dumps(vardnica)
    # f.write(vardnica_json)
    #json.dump(vardnica, f)
    
    #print(json.loads(f.read()))
    #print(json.load(f))\
    #0_0

# Pārbauda vai fails eksistē
import os
os.path.isfile(f"{faila_mape}\\nosaukums.json")

# Uzdevums: Uzrakstat programmu, 
# kurā lietotājs ievada vairāku cilvēku datus (vārds; uzvārds, vecums). 
# Visiem laukiem jābūt atsevišķi 
# (t.i. neapvienojat vārdu un uzvārdu).
# Individuālu cilvēka dati jāsaglabā vārdnīcā. 
# Vārdnīcas jāapvieno sarakstā.
# Saglabājat šos datus failā. 
# Uzsākot programmu izvadat šos datus ja fails eksistē.