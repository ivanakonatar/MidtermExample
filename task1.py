"""
===================   TASK 1   ====================
* Name: Can String Be Float
*
* Write a function `can_string_be_float` that will
* check whether the passed string value can be
* converted to float. If the string value can be
* successfully converted to float, function should
* return `True` otherwise it should return `False`.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def can_string_be_float(string_value):
    """
    Checks whether string_value can be converted
    to float. Each character in string_value will
    be checked against list of allowed characters
    for float numbers.
    """

    # If passed value is not type of 'str'
    if not isinstance(string_value, str):
        return False

    # Float number might have decimal point '.' and be negative '-'.
    allowed_float_characters = ['0', '1', '2', '3', '4', '5',
                                '6', '7', '8', '9', '.', '-']

    # Loop through characters in string_value and check if there
    # are any invalid characters
    for character in string_value:

        if character not in allowed_float_characters:
            return False

        # NOTE: This solution will fail if '-' appears in the
        # string on other position beside first. Fix this
        # issue by checking '-' position in string.

        # NOTE: This solution will fail if multiple dots '.'
        # are found in the middle of the string. Fix this
        # issue by check number of dots and their position.

    # If there were no invalid characters return `True`
    return True


def main():

    user_value = input("Enter string which will be evaluated: ")
    print(can_string_be_float(user_value))
    print(float(user_value))

main()
