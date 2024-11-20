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

with open(f"{faila_mape}\\nosaukums", "r", encoding="UTF-8") as faila_m:
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