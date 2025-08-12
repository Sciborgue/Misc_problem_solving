# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
"""The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:

    Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)

Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.
"""


import numpy as np
from numpy.linalg import matrix_power


def old_Fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n < 0:
        return old_Fib(n + 2) - old_Fib(n + 1)
    if n > 1:
        return old_Fib(n - 1) + old_Fib(n - 2)


def M_Fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == -1:
        return 1
    matrix_pos = [[0, 1], [1, 1]]
    if n < 0:
        m_pn = np.matrix(matrix_pos, dtype=object) ** abs(n)
        if abs(n) % 2 == 0:
            return -m_pn[0, 1]
        else:
            return m_pn[0, 1]
    if n > 1:
        m_pn = np.matrix(matrix_pos, dtype=object) ** abs(n)
        return m_pn[0, 1]


print(M_Fib(2))
print(M_Fib(3))
print(M_Fib(4))
print(M_Fib(-96))
print(M_Fib(-97))
print(M_Fib(1000))
