# John Green
# 1001011958
# 10/5/13
# Given a list listA of numbers, the program that generates a 
# new list listB with the same number of elements as listA, 
# such that each element in the new list is the average of its 
# neighbors and itself in the original list.

# listA
a_list = [5, 1, 3, 8, 4]

# listB
b_list = []

# loop through the list
for i in range(len(a_list)):
	if i == 0 : # test for first index
		temp = (a_list[0]+a_list[1])/2 
	elif i == (len(a_list)-1) : # test for last index
		temp = (a_list[i-1]+a_list[i])/2
	else:
		temp = (a_list[i-1]+a_list[i]+a_list[i+1])/3
	b_list.append(temp)
	
print("listA = ",a_list)
print("listB = ",b_list)
