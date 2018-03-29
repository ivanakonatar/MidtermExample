"""
===================   TASK 6   ====================
* Name: Attendance Checker
*
* Write a student attendance checker script. The
* script should take, as user input, minimum
* required number of attended classes for student
* in order to take an exam. File `attendance.csv`
* contains info about students and number of
* classes they attended. Print student names, that
* do not have right to take an exam.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
sve_linije = open("attendance.csv",'r').readlines()

minimum = abs(int(input("Unesi broj: ")))


lista=[]

for linija in sve_linije:

    linija_bez_praznina = linija.strip()

    student_i_broj = linija_bez_praznina.split(',')

    student = str(student_i_broj[0])
    broj = int(student_i_broj[1])

    if broj <  minimum:
        lista.append(student)

print("Studenti koji ne mogu da izadju na ispit su: ", lista)






