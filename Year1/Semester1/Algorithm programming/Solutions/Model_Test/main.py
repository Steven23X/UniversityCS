def citire_numere(nume_fisier):
    f=open(nume_fisier,"r")
    ls=[]
    for linie in f:
        subls=[int(x) for x in linie.split()]
        ls.append(subls)
    f.close()
    return ls

def prelucrare_lista(ls):
    for i in range(len(ls)):
        minim=min(ls[i])
        ls[i]=[x for x in ls[i] if x!=minim]

    m=len(ls[0])
    for x in ls:
        if m>len(x):
            m=len(x)

    for x in range(len(ls)):
        ls[x]=ls[x][:m]

    return ls

l=citire_numere("numere.in")
l=prelucrare_lista(l)

for linie in l:
    for x in linie:
        print(x,end=" ")
    print()


def d():
    l= citire_numere("numere.in")
    ls=set()
    k=int(input("k="))
    g = open("cifre.out", "w")
    for i in l:
        ls=ls | (set([x for x in list(map(str,i)) if len(x)==k]))
    g.write(" ".join(sorted(ls,reverse = True)))
    g.close()
d()