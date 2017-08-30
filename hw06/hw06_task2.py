# John Green
# 1001011958
# 10/12/13
"""
shift() function that assumes the shifting is to the left and takes
3 arguments ( list, interger less then length of list, shift direction)

main()  prints the lists both before and after shifting

"""

def shift(ls,k,dr):
        new_ls = []
        if dr == "right": # test for right shift
                for i in range(len(ls)):
                        index = (i-k)%len(ls) # find index location
                        new_ls.append(ls[index])
                return new_ls
        
        for i in range(len(ls)):
                        index = (i+k)%len(ls) # find index location
                        new_ls.append(ls[index])
        return new_ls
       
def main():
        n_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        k = 4
        if k < len(n_list):
                left = shift(n_list,k,"left")
                right = shift(n_list,k,"right")
                print("original list: ",n_list)
                print("shifted by "+str(k)+", to the left:",left)
                print("shifted by "+str(k)+", to the right:",right)

main()
