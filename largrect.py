def largest_rect3(histogram):
    #create a index table
    long=len(histogram)
    base = 0
    aire_record = 0
    for i in range(long):
        if base != histogram[i]:
            base = histogram[i]
            aire = base
            #additionner à gauche
            i_g=1
            while i_g<= i and histogram [i-i_g]>=base :
                aire = aire + base
                i_g += 1
            #additionner à droite
            i_d=1
            while i+i_d<long and histogram [i+i_d]>=base :
                aire = aire + base
                i_d+= 1
            if aire > aire_record:
                aire_record=aire
    return aire_record

#split the list
def splitthelist(liste,element):
    n_liste =[]
    liste_prov=[]
    i = 0
    while i < len(liste):
        if liste[i] == element:
            if liste_prov:
                n_liste.append(liste_prov)
                liste_prov=[]
            while i < len(liste) and liste[i] == element:
                i=i+1
        else:
            liste_prov.append(liste[i])
            i=i+1
    if liste_prov:
        n_liste.append(liste_prov) 
    return n_liste 

def largest_rect(histogram):
    if not histogram:
        return 0
    else:
        AIRES = []
        long=len(histogram)
        mini=min(histogram)
        if mini==max(histogram):
            AIRES.append(mini*long)
        else:
            AIRES.append(mini*long)
            A=splitthelist(histogram,mini)
            for minilist in A:
                maxair = largest_rect(minilist)
                AIRES.append(maxair)
        return max(AIRES)

print(largest_rect([3, 5, 12, 4, 10]))


