import sys
sys.stdin = open("input_2090.txt", "r")


def dining_hall():
    # Input
    n = int(input())
    t = list(map(int, input().split())) 

    nx_table = (1,1)
    rang = 0
    list_of_all = [(1,1)]
    for j in range(2,n):
        k = j
        tuple_test = (1,k)
        if not (j%3==0):
            while k > 0:
                if tuple_test[0]%3 == 0 and tuple_test[1]%3 == 0:
                    list_of_all.insert(-1,(tuple_test[0]-1, tuple_test[1]-1))
                elif not (tuple_test[0]%3 == 0 or tuple_test[1]%3 == 0):
                    list_of_all.append((tuple_test[0], tuple_test[1]))
                k-=1
                tuple_test = (tuple_test[0]+1, k)
        
    for i in range(n):
        if t[i] == 0:
            print(nx_table[0], nx_table[1])
            if nx_table in list_of_all:
                list_of_all.remove(nx_table)
            if nx_table[1] == 1:
                rang +=1
                nx_table = (1, nx_table[0]*3+1)
            else:
                nx_table = (nx_table[0]+3, nx_table[1]-3)
        else:
            print(list_of_all[0][0], list_of_all[0][1])
            if nx_table == list_of_all[0]:
                if nx_table[1] == 1:
                    rang +=1
                    nx_table = (1, nx_table[0]*3+1)
                else:
                    nx_table = (nx_table[0]+3, nx_table[1]-3)
            list_of_all.pop(0)
    




q = int(input())  #Test cases
for _ in range(q):
    dining_hall()