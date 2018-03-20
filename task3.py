"""
===================   TASK 3   ====================
* Name: Cube Volume
*
* Write a function `cube_volume` that will return
* volume of a cube for a given side length.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def cube_volume(side):
    """
    Calculates cube volume for given side.
    Returns -1 if argument is not int or float
    """
    # Side is not integer or float
    if (not isinstance(side, int)) and (not isinstance(side, float)):
        return -1

    # NOTE: Fix this solution in order to work
    # with negative numbers

    # Calculate cube volume (side^3)
    return side ** 3


def main():

    side_in_cm = 5.0
    volume_of_cube = cube_volume(side_in_cm)
    print("Volume of a cube is: ", volume_of_cube)

main()
