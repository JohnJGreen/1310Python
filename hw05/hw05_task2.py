# John Green
# 1001011958
# 10/5/13
# Given a list (l_list), and an element (find), the program creates 
# a new list, index_list, that has the indexes (positions) of the 
# occurrences of find in l_list. At the end, the program prints a 
# message about how many occurences were found and what they were. 
# If x is not found in L, the program print a message about that.

l_list = [4, 10, 4, 2, 9, 5, 4]
index_list = []

print("L = ",l_list)

find = int(input("Enter an element to search for in the list: "))

# loopthrough the indexes
for i in range(len(l_list)):
	if l_list[i] == find :
		index_list.append(i)

if len(index_list) == 0 :
	print(find,"does not occur in L.")
else:
	print(find,"occurs in L at the following positions: ",index_list)
