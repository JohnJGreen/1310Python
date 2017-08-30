# John Green
# 1001011958
# 9/14/13
# The program takes a positive integer N and computes the sum (1 - 2 + 3 - 4 + 5 - 6 + .... N)
# then print out the sum, equation, posative sum, and negative sum

# initialize variables
count = 2 # counter (starts at 2 because 1 is the assumed base)
T_sum = 1 # total sum (1 is the smallest posative int)
P_sum = 1 # positive sum (1 is the smallest posative int)
N_sum = 0 # negative sum

#user input
N_int = int(input("Enter N: "))

print ("1",end = " ") # start equation 

while count < N_int+1 :
    
    if count % 2 == 1 : # test for posative
        P_sum += count
        T_sum += count
        print("+" , count, end = " ")
        
    else : # test for negative
        N_sum += count
        T_sum -= count
        print("-" , count, end = " ")

    count += 1
        
print("= ",T_sum) # finish equation
print("The positive sum is: ",P_sum)
print("The negative sum is: ",N_sum)
