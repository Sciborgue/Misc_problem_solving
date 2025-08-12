# https://www.codewars.com/kata/64cfc5f033adb608e2aaedef


def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum


def jmp_to_zero_bu(n, echelon={}):
    echelon[0] = 0
    if n < echelon[-1]:
        return echelon[-1]

    return 1


def jmp_to_zero_td(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 10:
        return 1
    memo[n] = jmp_to_zero_td(n - sum_digit(n)) + 1
    return memo[n]


def jmp_to_zero(l):
    for n in l:
        print((n, jmp_to_zero_td(n)))


print(jmp_to_zero([i for i in range(1, 1000)]))
