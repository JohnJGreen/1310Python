# John Green
# 1001011958
# 9/14/13
# The program takes an integer N as input. If N is between 1 and 100 (inclusive),
# it prints out (on a single line) all the divisors of N.
# Input validation: If N is outside the [1,100] interval, the program should display
# an error message and keep asking for a valid N

# initialize the counter
count = 1

while True :
    N_int = int(input("Enter N: "))
    if N_int >= 1 and N_int <= 100 : #test if n is in range [1,100]
        break
    print("Error. Please enter only numbers in the range [1,100].")

print("The divisors of N are:",end = " ")

while count <= N_int :
    if N_int%count == 0 : #test if count is a divisor
        print(count,end = " ")
    count += 1
    
# haven't talked about it in class yet

#for i in range(1,N_int+1) :
#    if N_int%i == 0 :
#        print(i,end = " ")
    
