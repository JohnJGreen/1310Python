# John Green
# 1001011958
# 10/20/13

"""

menu() prints the options menu

comp_file(file) takes a file and creates a list from the file. returns the list if rows and collums are equal
and returns False if they are unequal

print_file(file) takes a list and print the list in exel format. if the list is false, print No file selected.

find_min(file) takes a list and askes the user for a collum or row and finds the lowest value in the collum or row

find_max(file) takes a list and askes the user for a collum or row and finds the highest value in the collum or row

find_sum(file) takes a list and askes the user for a collum or row and sums the values in the collum or row

delete(file) takes a list and askes the user for a collum or row and removes the collum or row

save_file(file,location) takes a list(file) and a string(location). prints contents of list in comma seperated
format to the file name from the string

save_as(file) takes a list and asks for user input of the file name. if the file name exists promps user for
save confermation. if confirmed call save_file(file,location)

find_row_or_collum(file) takes a list and asks for user input of row or collum. returns a list of th row or collum if exists.

"""

def menu():
        print("1 - Open and load from a file")
        print("2 - Minimum")
        print("3 - Maximum")
        print("4 - Sum")
        print("5 - Delete")
        print("6 - Save")
        print("7 - Save as (specify new file name)")
        print("0 - Exit")



def comp_file(file):
        file_list = []
        for line in file:
                index_list = []
                temp_line = line.strip("\n") 
                temp_list = temp_line.split(",") #strip to a list of strings
                for i in temp_list:
                        index_list.append(float(i)) # convert to a float and append to row
                file_list.append(index_list) #append the rows to the final list
        for line in file_list:
                if len(line) != len(file_list[0]): # test if row & collum are unequal
                        return False                        
        return file_list



def print_file(file):
        if file == False: #no file was selected
                print("No file selected.")
                print("\n"*2)
                return
        width = 8*(len(file[0])+1)+1 # calculate width
        print("\n"*2)
        print("-"*(width)) # start collum header
        print ("|       ", end = "")      
        for N in range(len(file[0])):
              print("|{:^7s}".format(chr(N+65)),end = "") # lable based on UTF-8 codes
        print("|")
        print("-"*(width)) # end collum header
        row = 1
        for line in file:
                print("|{:>6d} ".format(row),end = "") # print row number
                for i in line:
                        print("|{:^7.2f}".format(i),end = "") # print row elements
                print("|")
                row += 1
        print("-"*(width)) # finish table
                

def find_min(file):
        temp = find_row_or_collum(file)
        if temp:
                print("Minimum is: ", min(temp))
                print_file(file)
         

def find_max(file):
        temp = find_row_or_collum(file)
        if temp:
                print("Maximum is: ", max(temp))
                print_file(file)
                

def find_sum(file):
        temp = find_row_or_collum(file)
        if temp:
                print("Sum is: ", sum(temp))
                print_file(file)


def find_row_or_collum(file):
        row_or_collum = input("Enter a row (as a number) or a column (as an uppercase letter): ")
        try: # test if input row
                if 0 <= int(row_or_collum)-1 < len(file):
                        return file[int(row_or_collum)-1]
                else:
                        print("Invalid selection")
                        print_file(file)
                        return False
        except ValueError:
                try: # test if input valid letter
                        if 65 <= ord(row_or_collum) <= len(file[0])+65:
                                temp_list = [] # set initial value
                                for line in file:
                                        temp_list.append(line[ord(row_or_collum)-65]) # add item to list
                                return temp_list
                        else:
                                print("Invalid selection") # out of range
                                print_file(file)
                                return False
                except:
                        print("Invalid selection") # 2.2, none, ect
                        print_file(file)
                        return False
        
def delete(file):
        row_or_collum = input("Enter a row (as a number) or a column (as an uppercase letter): ")
        try: # test if input row
                if 0 <= int(row_or_collum)-1 < len(file):
                        file.pop(int(row_or_collum)-1) # remove selected row
                        print_file(file)
                else:
                        print("Invalid selection")
                        print_file(file)
        except ValueError:
                try: # test if input valid letter
                        if 65 <= ord(row_or_collum) <= len(file[0])+65:
                                for line in file:
                                        line.pop(ord(row_or_collum)-65) # remove selected collum
                                print_file(file)
                        else:
                                print("Invalid selection") # out of range
                                print_file(file)
                except:
                        print("Invalid selection") # 2.2, none, ect
                        print_file(file)
                        return
                

def save_file(file,location):
        if file == False: # no list
                print("No file selected.")
                print("\n"*2)
                return
        else:
                save_file = open(location,"w") # print list to file name(location)
                for line in file:
                        for i in line:
                                if i == line[len(line)-1]:
                                        print((str(i)), file = save_file)
                                else:
                                        print((str(i)+", "), file = save_file, end = "") # comma seperated format
                print_file(file)
                save_file.close()

                
                
def save_as(file):
        if file == False: # no list
                        print("No file selected.")
                        print("\n"*2)
                        return
        location = input("Enter a new filename: ")
        try: # test if file exists
                open(location, "r")
                while True:  # ask for overwrite
                        temp = input("This file already exists. Do you want to overwrite it (y/n)? ")
                        if temp == "n":
                                return
                        elif temp == "y":
                                break
                save_file(file,location) # save file
                
        except FileNotFoundError:
                if location == "": # no file name was entered
                        print("Invalid file name")
                        print_file(file)
                        return
                save_file(file,location)

                                

def main():
        while True:
                menu()
                user_choice = input("Your choice: ")
               
                if user_choice == "0":
                        break
                elif user_choice == "1":
                        try: # test if file exists
                                file_name = input("Enter a filename (if you hit enter, data1.txt will be opened): ")
                                if file_name == "":
                                        file_name = "data1.txt"
                                user_file = open(file_name,"r")
                                comped_file = comp_file(user_file)
                                user_file.close()
                                if comped_file != False:
                                        print_file(comped_file)
                                else:
                                        print("Data could not be loaded (the number of columns is not the same for all rows).")
                                        print("\n"*2)
                        except: # file does not exist
                                print("File could not be opened.")
                                print("\n"*2)
                else:
                        try: # test if file was selected
                                if user_choice == "2":
                                        find_min(comped_file)
                                elif user_choice == "3":
                                        find_max(comped_file)
                                elif user_choice == "4":
                                        find_sum(comped_file)
                                elif user_choice == "5":
                                        delete(comped_file)
                                elif user_choice == "6":
                                        save_file(comped_file,file_name)
                                elif user_choice == "7":
                                        save_as(comped_file)
                                else:
                                        print("invalid entry")
                                        print("\n"*2)
                        except UnboundLocalError: # file not selected
                                print_file(False)
               

main()
