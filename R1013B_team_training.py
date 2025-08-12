import sys

sys.stdin = open("input.txt", "r")


def team_a_team(list_a, x):
    result = 0
    if len(list_a) == 0:
        return 0
    a_test = list_a[:]
    while a_test:
        test_list = []
        score = 0
        while score < x:
            if len(a_test) == 0:
                result = 0
                break
            mi = min(a_test)
            test_list.append(mi)
            a_test.remove(mi)
            score = min(test_list) * len(test_list)
        if score >= x:
            result += 1
    if result == 0:
        list_a_copy = list_a[:]
        list_a_copy.remove(min(list_a_copy))
        return team_a_team(list_a_copy, x)
    else:
        return result


def team_training():
    # Input
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(team_a_team(a, x))


t = int(input())  # Test cases
for _ in range(t):
    team_training()
