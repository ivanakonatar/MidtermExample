
"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

def mala_u_velika(recenica):

    if not isinstance(recenica,str):
        print("Pogresan unos! ")

    nova_recenica = ''

    for karakter in recenica:
        broj_chr = ord(karakter)
        if broj_chr > 96 and broj_chr < 123:

            broj_veliko_slova = broj_chr - 32
            karakter = chr (broj_veliko_slova)

        nova_recenica+= karakter

    return nova_recenica

def main():

    recenica="IvaNa KONatAr"
    print("Velikim slovima napisana je: ", mala_u_velika(recenica))
    pass

main()