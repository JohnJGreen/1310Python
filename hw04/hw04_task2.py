# John Green
# 1001011958
# 9/30/13
# Asks the user to enter a string.
# Asks the user to enter a strictly positive (strictly greater than 0) integer.
# If the user does not enter a good value, the program will display an
# error message and prompt the user for the integer again.
# The program will keep on like this until the user enters a strictly positive integer.
# The program assumes the user will always enter integers.
# The program will refer to this integer as step
# If the length of the string is even the program will print the
# second half of the string and then the first half
# If the length of the string is odd, the program will print the middle letter,
# than the second half, and then the first half.
# Next it will print every step-th letter and a message explaining that.
# The message will depend on the value of step as follows:
# when step is 1, print "Every letter and it's index are:"
# when step is 2, print "Every second letter and it's index are:"
# when step is 3, print "Every third letter and it's index are:"
# for all other values for step print "Every step-th letter and it's index are:"
# Finally the program will print every step-th letter (starting from the first one)
# and the corrsponding index, one letter-index pair per line.

N_str = input("Enter a string: ")

while True:
    step = int(input("Enter a step: "))
    if step > 0 :
        break
    print("Error. The step should be strictly greater than 0.")

if len(N_str)%2 == 0 : #length is even
    temp = len(N_str)//2
    print(N_str[temp::])
    print(N_str[:temp:])

else : #length is odd
    temp = len(N_str)//2
    print(N_str[temp])
    print(N_str[(temp+1)::])
    print(N_str[:temp:])

if step == 1 : # step printou tests
    print("Every letter and it's index are:")
    
elif step == 2 :
    print("Every second letter and it's index are:")

elif step == 3 :
    print("Every third letter and it's index are:")
    
else :
    print("Every "+str(step)+"-th letter and it's index are:")

for i in range(0,len(N_str),step) : #step printout
    print(N_str[i],i)
