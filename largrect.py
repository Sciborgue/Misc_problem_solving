"""https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.



Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4



Constraints:

    1 <= heights.length <= 105
    0 <= heights[i] <= 104

"""


def largest_rect3(histogram):
    # create a index table
    long = len(histogram)
    base = 0
    aire_record = 0
    for i in range(long):
        if base != histogram[i]:
            base = histogram[i]
            aire = base
            # additionner à gauche
            i_g = 1
            while i_g <= i and histogram[i - i_g] >= base:
                aire = aire + base
                i_g += 1
            # additionner à droite
            i_d = 1
            while i + i_d < long and histogram[i + i_d] >= base:
                aire = aire + base
                i_d += 1
            if aire > aire_record:
                aire_record = aire
    return aire_record


# split the list
def splitthelist(liste, element):
    n_liste = []
    liste_prov = []
    i = 0
    while i < len(liste):
        if liste[i] == element:
            if liste_prov:
                n_liste.append(liste_prov)
                liste_prov = []
            while i < len(liste) and liste[i] == element:
                i = i + 1
        else:
            liste_prov.append(liste[i])
            i = i + 1
    if liste_prov:
        n_liste.append(liste_prov)
    return n_liste


def largest_rect(histogram):
    if not histogram:
        return 0
    else:
        AIRES = []
        long = len(histogram)
        mini = min(histogram)
        if mini == max(histogram):
            AIRES.append(mini * long)
        else:
            AIRES.append(mini * long)
            A = splitthelist(histogram, mini)
            for minilist in A:
                maxair = largest_rect(minilist)
                AIRES.append(maxair)
        return max(AIRES)


print(largest_rect([2, 1, 5, 6, 2, 3]))
