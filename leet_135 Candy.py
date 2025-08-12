# https://leetcode.com/problems/candy/description/
"""There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""


def candy(ratings):
    ranx = ratings
    # Initialization
    moving = ""
    down = 0
    up = 0
    plat = 0
    altitudes = []
    i = 0

    # each kid has at least one candy
    candies = len(ranx)

    # Address the empty list and 1-kid list
    if len(ranx) == 1:
        return candies
    # A. Change Ratings into an altitude list
    while i < len(ranx) - 1:
        # Case 1 : Descent
        if ranx[i + 1] < ranx[i] and (moving == "descent" or moving == ""):
            moving = "descent"
            down += 1
            i += 1
        # Case 2 : Ascent
        elif ranx[i + 1] > ranx[i] and (moving == "ascent" or moving == ""):
            moving = "ascent"
            up += 1
            i += 1
        # Case 3 : Plateau
        elif ranx[i + 1] == ranx[i] and (moving == "plateau" or moving == ""):
            moving = "plateau"
            plat += 1
            i += 1
        else:
            altitudes.append((moving, up + down + plat))
            moving = ""
            down = 0
            up = 0
            plat = 0
    total = down + up + plat
    if total > 0:
        altitudes.append((moving, up + down + plat))
        moving = ""
        down = 0
        up = 0
        plat = 0
    print(altitudes)

    j = 0
    # B. From the altitude list establish the number of candies
    while j < len(altitudes) - 1:
        if altitudes[j][0] == "ascent" and altitudes[j + 1][0] == "descent":
            candies += (
                (altitudes[j][1] * (altitudes[j][1] - 1)) / 2
                + (altitudes[j + 1][1] * (altitudes[j + 1][1] - 1)) / 2
                + max(altitudes[j + 1][1], altitudes[j][1])
            )
            print(up, down, candies)
            j += 2
        elif altitudes[j][0] != "plateau":
            candies += (altitudes[j][1] * (altitudes[j][1] + 1)) / 2
            print(up, down, candies)
            j += 1
        else:
            j += 1
    # Manage the last altitude
    if altitudes[-1][0] != "plateau" and j == len(altitudes) - 1:
        candies += (altitudes[-1][1] * (altitudes[-1][1] + 1)) / 2
        print(up, down, candies)
    return int(candies)


v = [1, 2, 4, 3, 2, 1, 2, 6, 9, 9, 9, 2, 1]
# print(candy(v))
w = [1, 3, 4, 5, 2]
print(candy(w))
