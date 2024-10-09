# Uzdevums
# Izveidojat programmu, kas pieņem ievadē skaitli n
# un izvada asteriskus (*) n rindās, pirmajā rindā
# izvadot 1 asterisku, un n rindā - n asteriskus.
# Piemērs. Ievade: 4
# Izvade:
# *
# **
# ***
# ****
# n = int(input("Skaitlis: "))
# for iii in range(1, n+1):
#     print("*"*iii)

# Uzdevums
# Ar vienu ciklu nodrošināt kalkulatora programmas ievadi
# (skaitlis, darbības zīme, skaitlis, darbības zīme...)
# Programma darbu beidz, kad lietotājs ievada kādu simbolu 
# kas nav darbības zīme vai skaitlis.
# Darbības zīmes - -, +, /, *
# Piem.
# Ievade - 4 + 3 - 8
# Aprēķina daļu varat pagaidām neveikt

darbiba = []
while True:
    num = input("Skaitlis: ")
    if not num.isdigit():
        break
    else:
        # Ja pēdējā ievade bija zīme, izņemt to
        darbiba.append(int(num))

    zime = input("Darbības zīme: ")
    #if zime != "+" and zime != "-" and zime != "/" and zime != "*":
    if not zime in ['+', '-', '/', '*']:
        break
    else:
        darbiba.append(zime)
print(darbiba)

# Uzdevums (i/ni), jāiesniedz e-klasē
# "Uzmini skaitli" spēli
# Tiek uzģenerēts skaitlis no 0 līdz 100 
import random
x = random.randint(0,100)
# x = int(random.random() * 100)
# Jāuzraksta cikls, kurā lietotājs min skaitli.
# Programma pārbauda vai ievadītais skaitlis ir vienāds ar uzģenerēto
# Ja nav, programma izvada to, vai ģenerētais skaitlis ir lielāks/mazāks
# Ja ir - lietotājs uzvar spēli, programma izvada tekstu 'Uzvara', un
# izvada visus lietotāja minējumus, kopā ar minējumu skaitu (len(...)).
# Piez. Lai realizētu pēdējo daļu, programmai jāsaglabā visas lietotāja ievades (piem. sarakstā)