#testtest

a = 1.645*(0.2*0.8/200)**(1/2)
b = (1.05-0.95)/(0.12/40**(1/2))
print(a,b)

def how_many_steps(a,b):
    j=0
    if a!=b:
        while a<b:
            if b%2:
                b=b-1
            else:
                b=b/2
            j+=1
    return j

test1=how_many_steps(1,10)
#print(test1)
test2=how_many_steps(50,100)
#print(test2)
test3=how_many_steps(100,100)
#print(test3)
test4=how_many_steps(5,8)
#print(test4)


def decode(msg, contents):
    alphabet={chr(i+96):i for i in range(1,27)}
    copie_jeu=msg
    a = [msg]
    for j in range(0,24):
        message=''
        for i in range(len(msg)):
            index = alphabet[copie_jeu[i]]
            modulo = index%26 + 97
            message += chr(modulo)
        copie_jeu = message
        a.append(message)
        print(message)

    list_occ = [i for i in a if contents in i] 

    return list_occ


from string import ascii_lowercase as u

TABLES = [str.maketrans(u, u[i:] + u[:i]) for i in range(26)]

def decode2(msg, contents):
    candidates = [msg.translate(tbl) for tbl in TABLES]
    return [x for x in candidates if contents in x]


#print(decode2('ymjxvznwwjqnxhzyj','squirrel'))

def somm(n):
    return (n*(n+1))//2

def sommf(n):
    som = 0
    for i in range(n):
        som += i 
    return som

print(somm(10)) 
print(sommf(10)) 