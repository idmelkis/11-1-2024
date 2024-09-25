# if <expr>:
# elif <expr>:
# #...
# x = 1
# match x:
#     case 1:
#         print("Viens!") 
#     case 2:
#         print("Divi!")
#     case "txt":
#         print("Kaut kāds teksts!")

# if x == 1:
#     print("Viens!") 
# elif x == 2: 
#     print("Divi!")
# elif x == "txt":
#     print("Kaut kāds teksts!")




# x = 0
# while x <= 3:
#     x += 1
#     if x == 2:
#         continue
#     print(x)
    #break
# else:
#     print("Beidzās")

# while - kamēr <nosacījums> patiess
for i in range(0, 10):
    pass
    # 0_0

saraksts = [ "1", "2", "3" ]
#print(','.join(saraksts))
saraksts.append("4")
#saraksts[1]
#print(saraksts[:2]) # Pirmie divi elementi
# for i in saraksts:
#     pass
    #print(i)

print(saraksts[::2])
for i in saraksts[2::1]:
    print(i)

# komentāri: ctrl + /
# for i in range(0, 10):
#     print(i)
"""
ASD
ASD
ASD
"""


# x = 0
# while x <= 3:
#     x += 1
#     if x == 2:
#         continue
#     print(x)
    #break
# else:
#     print("Beidzās")

# for i in range(0, 10):
#     pass


# Uzdevums: Uzrakstīs while UN for (divus atsevišķus) ciklus, kuros
# veic 3 ievades kādā sarakstā, t.i. katrā ciklā 3 reizes sarakstā tiek
# pievienota kāda vērtība.
# saraksts = []
# for i in range(4):
#     saraksts.append(input("Vērtība: "))

# skaititajs = 1
# while skaititajs < 4:
#     saraksts.append(input("Vērtība: "))
#     skaititajs += 1

# Uzdevums: Izmainīt kalkulatora kodu tā, 
# lai var ievadīt un veikt aprēķinus ar
# tik skaitļiem, cik lietotājs vēlas.
# (ar vienu darbību visiem skaitļiem)
darb = input("Darbība: ")
# 1. Kā uzglabāt skaitļus/rezultātu
# 2. Kā ievadīt
# 3. Kā veikt aprēķinus visiem skaitļiem
skaitli = []
# 1. Ievadam cik skaitļus vajadzēs ievadīt
# x = int(input())
# for i in range(0, x):
# 2. Veicam ievadi, līdz lietotājs ievada speciālu vērtību
while True:
    ievade = input("Skaitlis: ")
    if ievade.isnumeric():
        skaitli.append(int(ievade))
    else:
        break

rezultats = 0
for cipars in skaitli:
    if darb == "+":
        rezultats += cipars
    elif darb == "/":
        if cipars == 0:
            print("nevar dalīt")
        else:
            rezultats /= cipars
    elif darb == "-":
        rezultats -= cipars
    elif darb == "*":
        rezultats *= cipars

# Par ko padomāt uz nākošo stundu:
# 1. Kā apvienot šos ciklus (t.i. visu veikt vienā ciklā)
# 2. Kā pārveidot šo kodu tā, lai var veikt dažādu tipu darbības