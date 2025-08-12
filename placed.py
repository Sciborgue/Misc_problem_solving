import sys

sys.stdin = open("input_c.txt", "r")


def place():
    # Input
    m, n, k = map(int, input().split())

    etudmax_per_line = k // m + 1
    bench = n // (n - etudmax_per_line) - 1
    print(test_bench)


t = int(input())  # Test cases
for _ in range(t):
    place()
