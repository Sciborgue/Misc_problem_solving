# https://www.codewars.com/kata/58925dcb71f43f30cd00005f


def latest_clock(a, b, c, d):
    liste = [a, b, c, d]
    h_max = [2, 9, 0, 5, 9]
    heure = ""
    for i in range(0, 4):
        trouve = False
        if i == 2:
            heure = heure + ":"
        else:
            k = 0
            if heure == "2":
                h_max[1] = 3
            while trouve == False and k < h_max[i]:
                valeur_test = h_max[i] - k
                if valeur_test in liste:
                    heure = heure + str(valeur_test)
                    liste.remove(valeur_test)
                    trouve = True
                k = k + 1
    heure = heure + str(liste[0])
    return heure


print(latest_clock(1, 9, 8, 3))
