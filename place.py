import sys
import math
sys.stdin = open("input_d.txt", "r")

def place():
    # Input
    m,n,k = map(int, input().split())  
    
    etudmax_per_line = math.ceil(k/m)
    if etudmax_per_line == n:
        bench = n
    else:
        bench = etudmax_per_line//(n-etudmax_per_line)-1
    print(bench)



t = int(input())  #Test cases
for _ in range(t):
    place()