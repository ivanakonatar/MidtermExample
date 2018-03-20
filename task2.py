"""
===================   TASK 2   ====================
* Name: Convert Kilometers To Miles
*
* Write a script that will convert kilometers to
* miles. Script should ask user for input and check
* if user input is valid. If not, the script should
* quit immediately with appropriate message.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Note: You may use `can_string_be_float` function
* from previous task to validate user input.
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


# Take user input
user_input_kilometers = input("Enter distance in kilometers: ")

# Check if user input is invalid
if not can_string_be_float(user_input_kilometers):
    print("Input is invalid")
    quit()
else:
    # Convert `str` input to `float`
    distance_in_kilometers = float(user_input_kilometers)

    # Calculate distance in miles with formula
    distance_in_miles = distance_in_kilometers * 0.6213

    # Print result
    print("Distance in miles is: ", distance_in_miles)
