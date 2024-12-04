# Uzdevums: Uzrakstat programmu kura izveido mapi "mape"
# Mapē izveidojat failus ar nosaukumiem no 1 līdz 100
import os
import random

fails = random.randint(0, 100)
vertiba = random.randint(0, 1000)
print(f"fails: {fails}; {vertiba}")

faila_mape = os.path.dirname(__file__)
if not os.path.isdir(f"{faila_mape}\\mape"):
    os.mkdir("mape")
for iii in range(1, 101):
    with open(f"{faila_mape}\\mape\\{iii}", "w") as f:
        if iii == fails:
            f.write(str(vertiba))

while True:
    minejums = int(input("Minējums: "))
    if minejums == vertiba:
        break
print("!")

import shutil
shutil.rmtree(f"{faila_mape}\\mape")

# Uzdevums: Izmainīt šo (^) programmu lai kādā no izveidotajiem failiem (nejauši izvēlēts)
# ierakstītu vērtību uz labu laimi. Pēc tam prasīt lietotājam ievadīt
# šo vērtību un izvadīt, vai ievade bija pareiza, vai nepareiza.