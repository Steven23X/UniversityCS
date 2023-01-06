"""
#vector de cifre => sa determine frecventa ficarei cifre in vector
v=[int(x) for x in input().split()]
frec=[0 for i in range(10)]
for x in v:
    frec[x]+=1
print(frec)
"""
#propozitie -> frecventa fiecarui cuvant in propozitie
prop="mere pere mere are pere prune mere"
#tabele indate dupa alte tipuri de chei decat numere mici
#dictionare - tabele dispersie
d={}
for cuv in prop.split():
    if cuv in d: #=>O(1)? cautare/accesare eficienta a cheii
        d[cuv]+=1 #d[cuv] => O(1)
    else:
        d[cuv]=1
print(d)

"""
#Tabele de dispersie
structuri de date indexate dupa chei care au asociate un cod numeric, numit hash code
(functie de dispersie), a carui valoare nu se schimba pe parcursul existentei cheii
(de aceea cheiea trebuie sa fie de tip imutabil)
Doua obiecte cu valori egale au acelasi hashcode
Ideal ar fi ca doua obiecte cu valori diferite sa aiba coduri hash diferite, dar acest lucru 
de obicei nu este posibil pentru ca plaja de valori pe care o pot lua obiectele este mai mare =>
apar coliziuni (obiecte diferite cu acelasi cod hash)
tabelele de dispersie sunt implementate cat sa optimizeze cautarea dupa cheie
in principu, cautarea in tabel se face astfel:
cheie => se transforma in index numeric hash(cheie)%lungimea tabelului  =>
in t[index] se cauta cheia (!!!!t[index] este un bucket care contine informatii despre toate cheile 
pentru care hash(cheie)%lungimea tabelului are aceeasi valoare(pentru coliziuni)
=> putem folosi ca si cheie doar obiecte care au hash (in general imutabile)

"""
t=(1,2)
print(hash(t))
#ls=[3,4]
#print(hash(ls)) #TypeError: unhashable type: 'list'
"""
t=(1,[2,3])
print(hash(t)) #TypeError: unhashable type: 'list' pt t[1]
"""
s="abc"
print(hash(s))
"""
#in orice structura de date din python meomrata folosind tabele de dispersie vom 
avea doar elemente imutabile +cu hash code asociat"""
#ALTE TIPURI DE COLECTII - multimii si dictionare
#nu mai sunt indexate dupa indici numerici, de la 0 => nu s[i]
#MULTIMI - tipul set
#=colectie de obiecte cu valori diferite
#elementele care se pot adauga in set - imutabile
#CREARE - cu {}, ca si dictionarul
s={3,1,2}
print(s,type(s))
s={3,2,1,3}
print(s,type(s))
#ordinea de parcurgere a elementelor - nu este neaparat cea de la creare/inserare
#det literele distincte dintr-un cuvant
#s=set(iterabil)
s=set("avem un cuvant")
print(s)
#elementele distincte dintr-o lista
ls=[2,1,4,2,1,1,1]
print(set(ls))
#!!!! multimea vida
s={} #dictionar, nu multimea vida
s=set()
#comprehensiune -DA
print("elementele distincte pozitive")
ls=[2,3,4,2,2,2,-1]
s={x for x in ls if x>0}
print(s)
#--- continuare - curs 6





