def candy(v):
    compteur = 0
    if len(v)==0:
        compteur =0
    elif len(set(v))==1:
        compteur = 1
    else:
        compteur += len(v)
        mini = min(v)
        j = 0
        sub_listes=[]
        debut = 0
        while j < len(v):
            #si c'est le dernier élément rentrer 
            if v[j]==mini:
                sub_listes.append(v[debut:j])
                while v[j]==mini and j < len(v)-1: j += 1
                debut = j 
            j+=1
        if v[j-1]!=mini:
            sub_listes.append(v[debut:j])    
        for element in sub_listes:
            compteur += candy(element)
    return compteur

v = [1,3,2,2,1]
print(candy(v))

def candy2(rankings):
    maxi=max(rankings)
    