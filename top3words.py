def top_3_words(text):
    N=len(text)
    indice=0
    liste_mots=[]
    mot=""
    i=0
    index_max=0
    max_list=[]
    while i < len(text):
        mot_valide=False
        #former un mot
        while i < len(text) and (text[i].isalpha() or text[i]=="'"):
            if text[i].isalpha():mot_valide=True
            mot=mot+text[i].lower()
            i=i+1
        #si le mot est déjà dans la liste on augmente son indice
        k=0
        trouve=False
        while trouve==False and k < len(liste_mots):
            if mot == liste_mots[k][0] :
                liste_mots[k][1]=liste_mots[k][1]+1
                trouve=True
            k=k+1
        #sinon enregistrer ce mot nouveau
        if trouve==False and mot_valide:
            liste_mots.append([mot,1])
        #avancer jusqu'au prochain mot
        mot=""
        while i < len(text) and not (text[i].isalpha() or text[i]=="'") :
            i=i+1
    #sort
    k_final=0
    l2=[]
    liste_finale=[]
    l2=sorted(liste_mots,key=lambda x: x[1], reverse=True)
    i=0
    #ne prendre que les 3 premiers
    while i<len(l2) and i<3:
        liste_finale.append(l2[i][0])
        i=i+1
    return liste_finale

print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  //wont won't won't "))
print(top_3_words("  '''  "))
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))
