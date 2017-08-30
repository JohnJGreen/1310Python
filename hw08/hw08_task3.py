# John Green
# 1001011958
# 11/8/13
"""
build_file() takes a file name and returns a list of the file's lines

find_anagrams() takes a file name prints all anagrams in the file

the program find anagrams in a file

"""


def build_file(file_name):
    file = []
    file_raw = open(file_name,"r")
    for i in file_raw: # build list
        file.append(i.strip("\n"))
    file_raw.close()
    return file

def find_anagrams(file_name):
    ana_dic = {} # initialize
    file = build_file(file_name) # get list
    file.sort(key=len) # sort by length
    index = 1
    for line in file:
        temp_ls =[] # initialize new list
        sorted_line = sorted(line) # sort first word
        temp_ls.append(line)
        
        for line2 in file[index:]: # start loop at the next item (efficiency)
            if len(line2) != len(line): # test if words are not the same length (efficiency)
                break
            sorted_line2 = sorted(line2)
            if sorted_line == sorted_line2 and line != line2: # test for anagram and not the same word
                temp_ls.append(file.pop(file.index(line2))) # add anagram to list
                
        if len(temp_ls) > 1: # test if anagram exists      
            sorted_str = ""
            for i in sorted_line: # create a key
                sorted_str += i        
            if len(temp_ls) > 1 and sorted_str not in ana_dic: # test if more than one item and not in the dictionary
                ana_dic[sorted_str] = temp_ls
                print(temp_ls)
            
        index += 1

def main():
    find_anagrams("words.txt")

main()
