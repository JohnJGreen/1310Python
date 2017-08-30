# John Green
# UT ID 1001011958
# 9/01/13
# Write a program that asks the user to enter two real numbers (not integers) and
# computes and displays the following opertations between the two:
# multiplication, division, integer division, modulo , exponentiation


# hw01_task4


# First number
first_flt = float(input("Enter the first number: "))

# Second number
second_flt = float(input("Enter the second number: "))

# multiply
print(first_flt, "*", second_flt, "=", first_flt*second_flt)

# divide
print(first_flt, "/", second_flt, "=", first_flt/second_flt)

# int divition
print(first_flt, "//", second_flt, "=", first_flt//second_flt)

# modulis
print(first_flt, "%", second_flt, "=", first_flt%second_flt)

# exponetial
print(first_flt, "**", second_flt, "=", first_flt**second_flt)
