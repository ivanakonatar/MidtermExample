"""
===================   TASK 5   ====================
* Name: Del Boy Millionaire
*
* Help Del Boy become a millionaire. Del Boy is
* trading bitcoins on crypto-exchanges with simple
* algorithm. He is buying where the price of bitcoin
* is the lowest and selling where the bitcoin is
* the most expensive. Write a function `get_profit`
* which will take a list of bitcoin prices in USD as
* argument. The function should return what is the
* maximum possible profit for given bitcoin prices
* on different exchanges.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def get_profit(lista):

    maximum = max(lista)
    minimum = min(lista)


    return maximum-minimum






def main():
    lista=[11283.5, 10221,9896.6 ]
    print("Najveci profit je: ", get_profit(lista))
    pass

main()