"""
===================   TASK 5   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""


def is_even(number):

    if number % 2 == 0:
        return True
    else:
        return False


# Ask user how many numbers should list have an convert to int
list_length = int(input("How many numbers should list have? "))


# Create empty list where numbers will be stored
list_of_numbers = []

# Ask user to input list_length numbers and append to list_of_numbers
for i in range(list_length):
    new_number = int(input("Enter integer number #" + str(i+1) + ": "))
    list_of_numbers.append(new_number)  # Add new number to the list

# Initialize total number of even and odd numbers
total_even = total_odd = 0

for number in list_of_numbers:

    # Check if number is even
    if is_even(number):
        total_even += 1
    else:
        total_odd += 1


print("List of numbers: ", str(list_of_numbers))
print("Total even numbers: ", total_even)
print("Total odd numbers: ", total_odd)
