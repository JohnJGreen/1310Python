# John Green
# 1001011958
# 11/8/13
"""
build_dictionary() builds a dictionary from file and returns the dictionary

translate(dictionary, word) takes a dictionary and a word returns the morse code of the word

"""

def build_dictionary():
    dictionary = {}
    file = open("Morse.txt","r")
    for line in file: # build dictionary
        line = line.strip("\n")
        temp = line.split("\t")
        dictionary[temp[0]] = temp[1]
    file.close()
    return dictionary

def translate(dictionary, word):
    translated_word = ""
    for i in word: # loop through letters
        if 47 < ord(i) < 58: # test for numbers
            translated_word += (dictionary[i]+" ")
            continue
        if 89 < ord(i) < 123: # test for lower case
            i = chr(ord(i)-32) # convert to upper case
        if 64 < ord(i) < 91: # test for upper case
            translated_word += (dictionary[i]+" ") # build morse code
        else:
            return("Not translatable")
            
    return translated_word

def main():
    dictionary = build_dictionary()
    word_ls = ["cab","Tin","suNny"]
    for word in word_ls:
        print("{:<8s}".format(word+":") + translate(dictionary, word)) # print formated word and morse code

    """
    # testing
    while True:
        word = input("input word: ")
        if word == "-1":
            break
        print("{:<8s}".format(word+":") + translate(dictionary, word))
    """

main()
