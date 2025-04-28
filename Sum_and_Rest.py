def revers(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

print(revers(1997))

def sum_dif_rev(n):
    for i in range(11,n):
        revi = revers(i)
        if i != revi:
            if (i + revi)%abs(i-revi)==0:
                print(i, revi)

sum_dif_rev(100000)