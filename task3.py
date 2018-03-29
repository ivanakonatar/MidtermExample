"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

n = int(input("Koliko brojeva unosite? "))

lista = []

nenegativni = negativni = 0

for i in range(n):
    novi_broj = int(input("Unesite "+ str(i+1)+ ".broj: "))
    lista.append(novi_broj)

    if novi_broj == 0:
        nenegativni += 1

    else:

        if novi_broj < 0:
            negativni += 1

print("Vasa lista: ", str(lista))
print("Nenegativnih brojeva u listi ima: ", negativni)
print("Negativnih brojeva u listi ima: ", negativni)



