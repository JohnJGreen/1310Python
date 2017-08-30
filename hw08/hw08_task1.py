# John Green
# 1001011958
# 11/8/13
"""
the program prints out

keys
values
key and value pairs
key and value pairs in order of key
key and value pairs in order of value

"""



def main():
    d = {'a':15, 'f':35, 'b':120}
    keys = list(d.keys())
    print("The keys are: ", end = "")
    for i in keys: # prints the keys
        if i == keys[-1]: # test for last key
            print(i)
            break
        print(i, end = ",")

    values = list(d.values())
    print("The values are: ", end = "")
    for i in values: # prints out the values
        if i == values[-1]: # test for last value
            print(i)
            break
        print(i, end = ",")

    items = list(d.items())
    print("The (key,value) pairs are: ", end = "")
    for i in items: # print item pairs
        if i == items[-1]: # tests for last pair
            print(i)
            break
        print(i, end = "")

    sets = sorted(d.items())
    print("The values in order of the keys are: ", end = "")
    for i in sets: # sorts pairs by keys
        if i == sets[-1]: # tests for last pair
            print(i)
            break
        print(i, end = ",")
                
    values.sort()
    print("The keys in order of the values are: ", end = "")
    for i in values: # sorts pairs by values
        for N in sets:
            if N[1] == i:
                if i == values[-1]:# tests for last pair
                    print(N)
                    break
                print(N, end = ",")


main()
