# Uzdevums: Uzrakstat while (!) ciklu, kas izvada skaitļus no 0 līdz
# 10, izlaižot skaitļus 4 un 6.

x = 0
sar = [ 0, 1, 2, 3]
while x <= 10:
    if x == 4 or x == 6:
        x += 1
        continue
    print(x)
    x += 1

# Uzdevums:
# Uzrakstīt ciklu, kas iet pāri skaitļiem no 1 līdz 100, UN
# Ja skaitlis dalās ar 3, izvada vārdu "Fizz"
# Ja skaitlis dalās ar 5, izvada vārdu "Buzz"
# Attiecīgi, ja skaitlis dalās ar 3 un 5, izvada FizzBuzz
# Ja skaitlis nedalās ar nevienu no šiem skaitļiem, izvadat to
# Dalīšanas atlikuma pārbaudei izmatot - % - modulus operators
# Piem.
# 4 % 2 == 0
# 5 % 2 == 1
for iii in range(1, 101):
    if iii % 3 == 0 and iii % 5 == 0:
        print("FizzBuzz")
    elif iii % 3 == 0:
        print("Fizz")
    elif iii % 5 == 0:
        print("Buzz")
    else:
        print(iii)

# Uzdevums:
# Uzrakstīt ciklu, kas 
# * ļauj lietotājam ievadīt vērtību un saglabā to
# * izvada visu ievadīto skaitļu vidējo vērtību (pēc ievades)
# * programma beidz darbu, kad lietotājs ievada kādu burtu
#piem.
#Iterācija 1: ievada 2, izvada 2
#Iterācija 2: ievada 4, izvada 3 (2, 4)
#Iterācija 3: ievada 10, izvada 5.3 (2, 4, 10)
#...
# skaitli = []
# while True:
#     skaitli.append(int(input("Skaitlis: ")))
#     # 1. Variants ar sum
#     print(sum(skaitli) / len(skaitli))

#     # 2. Variants - tie kas neatceras, ka sum funkcija eksistē
#     summa = 0
#     for iii in skaitli:
#         summa += iii
#     print(summa / len(skaitli))


# Uzdevums: Izmainīt kalkulatora ievadi (zemāk), lai glabātu
# gan skaitļus, gan darbības zīmes starp skaitļiem
skaitli = []
while True:
    if len(skaitli) % 2 == 0:
        ievade = input("Skaitlis: ")
        if ievade.isnumeric():
            skaitli.append(int(ievade))
        else:
            break
    else:
        darb = input("Darbība: ")
        if darb == "+" or darb == "-" or darb == "/" or darb == "*":
            skaitli.append(darb)
        else:
            break

# t.i. lai ievade var būt vienādojums - 5 + 4 - 3 / 2
# 2. Uzdevums: veik aprēķinus (ievadīto darbību)
# rezultats = 0
# for cipars in skaitli:
#     if darb == "+":
#         rezultats += cipars
#     elif darb == "/":
#         if cipars == 0:
#             print("nevar dalīt")
#         else:
#             rezultats /= cipars
#     elif darb == "-":
#         rezultats -= cipars
#     elif darb == "*":
#         rezultats *= cipars