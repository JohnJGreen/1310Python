# John Green
# UT ID 1001011958
# 9/01/13
# Fix broken code (see below)

#The area of a rectangle with sides L and H is L*H.
#The following code is an incorrect attempt to write a program that computes the area of a rectangle.
#Write a corrected version of the program and save it as hw01_task2.py.

#This program calculates the area of a rectangle
#length = input("Enter the length, L: ")
#height = input("Enter the height, H: ")
#area = length * height
#print("Area =", area)


# hw01_task2.py


# This program calculates the area of a rectangle

length = input("Enter the length, L: ")
height = input("Enter the height, H: ")
area = int(length) * int(height) # correction: force int on variables
print("Area =", area)





