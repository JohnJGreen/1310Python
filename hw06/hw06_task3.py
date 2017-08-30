# John Green
# 1001011958
# 10/12/13
"""
is_numeric() takes a string parameter and returns True if all the characters in the string
are digits, comma, space, or dot

string_to_list() takes a string parameter and returns the list of the numbers in the string

main() string_to_list() function to build a list out of the user string and then prints the resulting list
then ask the user if they want to continue

"""

def is_numeric(n_str):
        try:
               temp = n_str.split(",") # test for comma
               for i in temp:
                       if len(i.split(".")) > 2: # test for numbers
                               return False
                       elif len(i.split(".")) == 2: # test for float
                               float(i)
                       else: # test for int
                               int(i)                
               return True
        
        except:
                return False

def string_to_list(n_str):
        ls = []
        if is_numeric(n_str):
                for i in n_str.split(","):
                        if len(i.split(".")) == 2: # convert to float
                                ls.append(float(i))
                        else: # convert to string
                                ls.append(int(i))
        return ls

def main():
        n_str = input("Enter a set of numbers (integers or floats) separated by comma: ")
        print("The list is:",string_to_list(n_str)) # string_to_list is completed before printed
        while True:
                temp = input("continue ?( y / n):  ")
                if temp == "n":
                        break
                elif temp == "y":
                        main()
                
        

main()


