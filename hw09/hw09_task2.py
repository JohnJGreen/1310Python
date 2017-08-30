# John Green
# UT ID 1001011958
# 11/20/13
"""
any_base_to_base(tup,dic) takes a list and a dictionary. the list is number, original base,
convertion base in that order. returns the converted number

convert(ls,dic) takes a list and a dictionary. the list is number, original base, convertion base in that order.
tests for real number i.e.(127 in base 7 does not exist) then calls any_base_to_base. returns the converted number

print_menu() prints out the menu and takes an input. returns the input

creat_dic() creates a dictionary for bases 2 to 16. returns the dictionary

open_file(name) takes a string(file name). opens file and creates a list of the files lines.
returns a list of lines or false if file does not exist

print_to_file(file,file_name,dic) takes a file list, file name, and dictionary in that order. calls convert() for each item in file list.
writes convert()'s return to a file based on a modifided file_name.

print_file(file) takes a file name. calls open_file and prints out the return if file exists

"""

def any_base_to_base(tup,dic):
    temp = str(tup[0]) # seperate in parts
    b1 = int(tup[1])
    b2 = int(tup[2])
    dictionary = dic
    if b1>=b2: # find larger base
        base = b1
    else:
        base = b2
    new_num = "" # initialize string
    temp_2 = temp   
    base_10 = 0
    start = len(temp_2)-1 # find starting exponent
    for i in temp_2:
        base_10 += int(dictionary[i]*(b1**(start))) # convert to base ten
        start -= 1
    start = 0
    num = base_10
    while True:
        if num//(b2**start) == 0: # find convertion base exponent
            start -= 1
            break
        start += 1   
    while start >= 0 : # convert to secondary base
        if (num//(b2**start)) > 9:
            new_num += str(chr(55+(num//(b2**start))))
        else:
            new_num += str(dictionary[str(num//(b2**start))])
        num -= (num//(b2**start)*(b2**start))
        start -= 1
    return new_num

def convert(ls,dic):
    for i in ls[0]:
        if dic[str(i)] >= int(ls[1]): # test for real number (127 in base 7 does not exist)
            return
    converted = any_base_to_base(ls,dic)
    return converted
    
def print_menu():
    print()
    print("\t0. Exit.")
    print("\t1. Convert a number.")
    print("\t2. Solve a test (from a file).")
    print("\t3. Print a file.")
    print()
    return input("Enter your choice: ")

def creat_dic():
    dictionary = {}
    for i in range(16): # create base 2 to 16 dictionary
        if i<10:
            dictionary[str(i)] = i
        else:
            dictionary[chr(87+i)] = i # lower case
            dictionary[chr(55+i)] = i # upper case
    return dictionary

def open_file(name):
    try: # test for valid file name
        temp_file = []
        file = open(name, "r")
        for i in file:
            temp_file.append(i) # build list from file
        file.close()
        return temp_file
    except:
        print("Invalid file name")
        return False

def print_to_file(file,file_name,dic):
    if file == False: # if file does not exist
        return False
    new_name = file_name.split(".")
    new_name = new_name[0]
    new_name = new_name+"_solution.txt" # build new file name
    new_file = open(new_name, "w")
    for line in file:
        temp_line = ""
        line = line.strip("\n") # build string to print to file
        temp = line.split(",")
        N = temp.pop(0)
        N = N.split(":")
        base = N[0]
        num = N[1]
        temp_line += (str(base)+":"+str(num)+" ,")
        for i in temp:
            converted = convert([num,base,i],dic)
            if converted == None: # test for base error
                temp_line = temp_line.strip(",")
                temp_line += " base number error"
                print("Error number format given base: ",base,":")
                break
            temp_line += str(i)+":"+str(converted)+"," # add convertions to string
        temp_line = temp_line.strip(",")
        print(temp_line, file = new_file) # print string to file
    new_file.close()
    print("Written solution to file: ",new_name)
    print("The solution is:")
    print_file(new_name)

def print_file(file):
    temp = open_file(file)
    if temp == False: # test if file exists
        return False
    print("-"*20)
    for i in temp:
        i = i.strip("\n") # print file list to console
        print(i)
    print("-"*20)

def main():
    dic = creat_dic()
    while True:
        choice = print_menu()
        if choice == "0": # exit
            break
        elif choice == "1": # convert number from user input
            ls = input("Enter a number, current_base, new_base(e.g.: 129,10,2): ").split(",")
            if len(ls) == 3:
                temp = convert(ls,dic)
                if temp != None: # test for base error
                    print(ls[2],":",temp)
                else:
                    print("Invalid representation n ="+"{:^6s}".format(str(ls[0]))+"in base : ",ls[1])
            else:
                print("Invalid input")       
        elif choice == "2": # convertion from file
            file_name = input("Enter the name of the test file: ")
            file = open_file(file_name)
            print_to_file(file,file_name,dic)   
        elif choice == "3": # print to console from file
            print_file(input("Enter the name of the file to be printed: "))
        else:
            print("Invalid choice.")
            
main()
