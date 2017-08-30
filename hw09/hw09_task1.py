# John Green
# UT ID 1001011958
# 11/20/13   
"""
Convert the following numbers (from base 10) to base 2:
13
85
219
511
512

Convert the following numbers (from base 2) to base 10. You should assume they are all positive values:
1010
10001
11011
0111011
01010101

Convert the following numbers:
7A1 (base 16) to: base 10
567 (base 8) to : base 5
567 (base 10) to : base 5
2121 (base 3) to : base 4
7778 (base 10) to: base 16

Convert the following negative numbers (from base 10) to base 2 using 2's complement on 8 bits:
-1
-13
-59
-83
-128

Convert the following numbers (from base 2) to base 10. This binary representation is using 2's complement on 8 bits to represent negative numbers:
10101010
10011010
11001001
10001000
01111111

"""

def main():

    print("Base 10: 13       Base 2: 1101")
    print("Base 10: 85       Base 2: 1010101")
    print("Base 10: 219      Base 2: 11011011")
    print("Base 10: 511      Base 2: 111111111")
    print("Base 10: 512      Base 2: 1000000000")
    print()
    print("Base 2:  1010     Base 10: 10")
    print("Base 2:  10001    Base 10: 17")
    print("Base 2:  11011    Base 10: 27")
    print("Base 2:  0111011  Base 10: 59")
    print("Base 2:  01010101 Base 10: 85")
    print()
    print("Base 16: 7A1      Base 10: 1953")
    print("Base 8:  567      Base 5: 3000")
    print("Base 10: 567      Base 5: 4232")
    print("Base 3:  2121     Base 4: 1012")
    print("Base 10: 7778     Base 16: 1E62")
    print()
    print("base 2 using 2's complement on 8 bits")
    print()
    print("Base 10: -1       Base 2: 11111111")
    print("Base 10: -13      Base 2: 11110011")
    print("Base 10: -59      Base 2: 11000101")
    print("Base 10: -83      Base 2: 10101101")
    print("Base 10: -128     Base 2: 10000000")
    print()
    print("Base 2:  10101010 Base 10: -86")
    print("Base 2:  10011010 Base 10: -102")
    print("Base 2:  11001001 Base 10: -55")
    print("Base 2:  10001000 Base 10: -120")
    print("Base 2:  01111111 Base 10: 127")
    print()

main()
