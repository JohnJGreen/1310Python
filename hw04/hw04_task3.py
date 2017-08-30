# John Green
# 1001011958
# 9/30/13
# The program asks the user to think of a number.
# the program then asks if the number is in the first half of the interval
# the program only accepts y or Y for yes and n or N for no.
# 

low_int = 1
high_int = 100

print("Think of a number between 1 and 100 (inclusive)")
print("Answer the following questions with letters y or Y for yes and n or N for no.")

while low_int != high_int : #test for corect number
    mid_int = (low_int+high_int)//2 #find midpoint
    print("interval: [{},{}]. Is your number <= {}? ".format(low_int,high_int,mid_int),end = "") #ask if correct
    temp = input()
    if temp == "y" or temp == "Y" : # test input and set new interval
        high_int = mid_int
    elif temp == "n" or temp == "N" :
        low_int = mid_int+1

print("Your number is: ",low_int)
    
