"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
broj = eval(input("Unesi cijeli broj: "))

if not isinstance(broj,int):
    print("Pogresan unos! ")
    quit()

proizvod = 1


for i in str(abs(broj)):

    proizvod *= int(i)  # ako je dati broj negativan proizvod ce negativan broj



print("Proizvod cifri je: ", proizvod)
