def permutations(s):
    liste2=[]
    if len(s)==1:
        liste2.append(s)
    else:
        lettreseule = s[0]
        reste = s[1:]
        liste_mix=permutations(reste)
        for element in liste_mix:
            for i in range(len(element)+1):
                nouveau = element[:i]+lettreseule+element[i:]
                if not nouveau in liste2:
                    liste2.append(nouveau)
    return liste2



print(permutations('adefgg'))
 