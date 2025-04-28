def smaller(arr):
    arr_out = []
    for i in range(len(arr)-1):
        s = 0
        ref = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<ref:
                s+=1
        arr_out.append(s)
    arr_out.append(0)
    return arr_out


a=smaller([5, 4, 3, 2, 1])
print(a)