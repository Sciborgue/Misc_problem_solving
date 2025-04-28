import sys
sys.stdin = open("input_a.txt", "r")

def olympiad_date():
    # Input
    n = map(int, input().split())  
    a = list(map(int, input().split())) 
    

    found = False
    sequence = [3,1,2,1,0,1]
    for i in range(len(a)):
        if a[i]<6 :
            if sequence[a[i]]>0:
                sequence[a[i]] -= 1
        if sum (sequence) == 0:
            found = True
            output = i+1
            print(output)
            break
    if found == False:
        print(0)




t = int(input())  #Test cases
for _ in range(t):
    olympiad_date()