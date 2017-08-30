# John Green
# 1001011958
# 10/12/13
"""
is_a_number tests for a number and returns the number or false

my_sum() takes two arguments and returns the sum of the arguments

main() takes 2 user inputs (as either int or float)
and calls my_sum() to add them. Prints the result

"""

def is_a_number(N):
        try:
               temp = N.split(".")
               if len(temp) > 2: # test for numbers
                       return False
               elif len(temp) == 2: # test for float
                       return float(N)
               else: # test for int
                       return int(N) 
        except:
                return False

def my_sum(a,b):
        if is_a_number(a) and is_a_number(b):
                return is_a_number(a)+is_a_number(b)
        return "UNKNOWN"
        
        
def main():
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        temp = my_sum(a,b)
        print(a,"+",b,"=",temp)

main()
