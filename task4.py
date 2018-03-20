"""
===================   TASK 4   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def sum_digits(number):

    # Chek if passed number is integer
    if not isinstance(number, int):
        return -1

    # Initialize sum value
    digit_sum = 0

    # NOTE: Fix this solution so it can work
    # for negative integers

    while number > 0:
        digit = number % 10
        number = number // 10
        digit_sum = digit_sum + digit

    return digit_sum


def main():

    int_number = 1234
    digit_sum = sum_digits(int_number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()
