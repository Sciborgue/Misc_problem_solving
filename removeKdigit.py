#testtest
def removeKdigits2(S, K):
    S_tr=chr(S)
    if K == len(S_tr):
        return 0
    else:
        S_first=S_tr[0:K+1]
        i_zero=0
        if 0 in S_first:
            i_zero=S_first.index(0)
            K=K-i_zero
        S2=S_tr[i_zero:]
        while K>0:
            S2.remove(max(S2))
            K=K-1
        S_final=""
        for i in S2:
            S_final=S_final+str(i)
        return int(S_final)

def removeKdigits3(S, K):
    S_tr=str(S)
    S_rec="0"
    i=0
    while K>0 and i<len(S_tr):
        S2=S_tr[i]
        if S2 < S_rec[-1]:
            S_rec=S_rec[0:-1]
            K=K-1
        else:    
            S_rec=S_rec+S2
            i=i+1    
    if K !=0:
        S_rec=S_rec[:len(S_rec)-K]
    else:
        S_rec=S_rec+S_tr[i:]
    return int(S_rec)

def removeKdigits(S, K):
    S_tr=str(S)
    stack = []
    i=0
    while K>0 and i<len(S_tr):
        S2=S_tr[i]
        if S2 < S_rec[-1]:
            S_rec=S_rec[0:-1]
            K=K-1
        else:    
            S_rec=S_rec+S2
            i=i+1    
    if K !=0:
        S_rec=S_rec[:len(S_rec)-K]
    else:
        S_rec=S_rec+S_tr[i:]
    return int(S_rec)

print(removeKdigits(971149, 6))
print(removeKdigits(123456, 3))
print(removeKdigits(132456, 3))
print(removeKdigits(124000291, 3))