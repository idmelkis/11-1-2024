#nosaukums = 2 - 1
#x = 1
#x += 1 # x = x + 1
#x -= 1 # x = x - 1

# bool (True/False) (1/0)
#if True == 1:
#    print("!")

# int (1, 2...)
# float (1.1, 1.2,...)

# string ("...") - "asdasdasd"
mainigais = 10
#print("Kaut kāds teksts: " + str(mainigais))
#int("123") | float("123.0")

# mainigais = 10
# print("Kaut kāds teksts: " + str(mainigais))
# print(f"Kaut kāds teksts: {mainigais}")

# ctrl + /
# Tikai pielikt '#' rindas sākumā: ctrl + k + c
# print("Rinda1\nRinda2")
# print("""Rinda1
# Rinda2
# Rinda3""")

"""
Komentārs
Kaut kas vēl
Rinda3
"""
# list ([...])
# x = [ "123", 123 ]
# print(len(x)) # 2

# texts = "Teksts"
# # chr('...') - char - 's'
# #print(texts[<sākums>:<beigas>])
# print(len(texts))
# print(len(x))


# x[1] = 123
#texts[2] = "2"

# tuple ()
# x = ( "123", 123 )
#x[1] = 2131

#x = [ 'A', 'B', 'C' ]
#print(','.join(x))
# x = 5
# y = x == 1
# ==, is - vienāds
# !=, not - nav vienāds
# > - lielāks par (neieskaita vērtību)
# >= - lielāks & vienāds par (ieskaita vērtību)
# < - mazāks par
# <= - mazāks & vienāds par
# if not x == 5 or x == 1 and x == 2:
#     print("!!!")
# elif x == 8:
#     print("111")
# else:
#     print("000")

# print(y)
# if y:
#     print("Patiess")

#x = input("Ievade: ")
#
#if x.isdecimal():
    # ....
#x.isnumeric()

# Uzdevums: Kalkulators
# Ievade: divi skaitļi un darbība
# Izvade: darbības rezultāts
# Darbības - Saskaitīt, Atņemt, Reizināt, Dalīt
# Dalīšanai jāņem vērā, ka nevar dalīt ar 0!
x = int(input("Pirmais skaitlis "))
y = int(input("Otrais skaitlis "))
darb = input("Darbība: ")
if darb == "+":
    print(f"{x}+{y}={x+y}")
elif darb == "/":
    if y == 0:
        print("nevar dalīt")
    else:
        print(f"{x}/{y}={x/y}")
    # ...