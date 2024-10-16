
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
# y = -1
# skaitli = []
# while x != y:
#     y = int(input("Skaitlis: "))
#     skaitli.append(y)
#     if x > y:
#         print("Ievadītais skaitlis ir mazāks")
#     elif y > x:
#         print("Ievadītais skaitlis ir lielāks")
#     else:
#         print("Uzvara")
#         print(f"Min skaits: {len(skaitli)}, Minējumi: {skaitli}")
#         break

# Funkcijas
#F(x) = x^2
# def F(x):
#     return x^2

# funkcijas_nosaukums
def funkcijasNosaukums(parametrs1, parametrs2):
    pass

x = 1
x = 2

# def fun1():
#     print("!")
# def fun1(param1):
#     print("!!!!!!!")
# fun1(param1=1)

# globMain = 5
# def F(x):
#     global globMain
#     main1 = "asd"
#     print(globMain)
#     return x^2
# x2 = F(2)

print("kaut kas")
def funkcija(param1:int, param2:str, param3:'list[int]') -> int:
    """Kaut kāds funkcijas apraksts"""
    return 1
#rez = funkcija()

# Lūdzu tā nedarat
# def funkcija1():
#     def funkcija2():
#         print("!")
#     funkcija2()
# funkcija2()
#print("1", "9", "2", sep=";")
# def parametri(param1 = 1, *parametri, param3 = ""):
#     print(parametri)
# parametri(1,23,4,5,56,6,7,8,9)
def stdVert(param1 = 1, param2:str = "2"):
    print(param1)
    print(param2)
    return 0
stdVert(param2=5)

# Uzdevums
# Lietotājs ievada vairākus skaitļus:
# def skaitluIevade() -> 'list[int]':
#     skaitli = []
#     while True:
#         ievade = input("Skaitlis:")
#         if ievade.isdigit():
#             skaitli.append(int(ievade))
#         else:
#             break
#     return skaitli
# Jāuzraksta funkcija, kas saskaita skaitļu summu sarakstā
# un izsaucat to izmantojot funkcijas skaitluIevade izvadi.
# def sumList(saraksts:'list[int]') -> None:
#     summa = 0
#     for iii in saraksts:
#         summa += iii
#     return summa

# saraksts = skaitluIevade()
# summa = sumList(saraksts)
# print(summa)
# ===
#print(sumList(skaitluIevade()))

# Uzdevums: Uzrakstīt funkciju, kas pieņem bezgalīgu daudzumu
# skaitļus kā parametrus, un izvada lielāko skaitli
# Neizmantot iebūvētās python matemātiskās funkcijas (max())
def maxNum(*skaitli):
    x = skaitli[0]
    for iii in skaitli:
        if iii > x:
            x = iii
    return x
print(maxNum(123,345,12,33,777,12))

# Funkcija izvada skaitļus no n (ievade) līdz 0 skaitot uz leju
# Paskatīsimies pēc KD
def recurse(param1):
    print(param1)
    if param1 > 0:
        return recurse(param1-1)
    elif param1 <= 0:
        return 0
recurse(3)

param1 = 3
while param1 >= 0:
    print(param1)
    param1 -= 1

def factorial(n):
   if n == 1:
        return 1
   else:
        return n * factorial(n-1)
print(factorial(4)) # 4! = 4 * 3 * 2 * 1 (24)

# Uzdevums: Pārveidojiet funkciju 
# factorial(n) par while ciklu
rezultats = 1
n = 5
while n > 0:
    rezultats *= n
    n -= 1
print(rezultats)