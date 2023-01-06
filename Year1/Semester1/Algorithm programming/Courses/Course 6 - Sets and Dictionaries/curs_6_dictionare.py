#Am facut in cursul 5:
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
print(d, type(d))
#DICTIONARE - clasa dict
#colectii care memoreaza perechi de forma cheie:valoare,
# care sa permita interogari rapide legate de chei
#cautarea unei chei pentru a determina valoarea asociata,
# stergerea unei perechi cheie:valoare- O(1) mediu
#CREARE
#d={cheie1:valoare1,cheie2:valoare2}
d={1:"unu",2:"doi"}
#cheia - imutabila+cu hash code asociat
#valoarea- de orice tip
d={1:["abc","d"],"doi":{3,1}}
print(d)
#d={[1,2]:"punctul 1",[1,3]:"punctul 3"} #TypeError: unhashable type: 'list'
d={(1,2):"punctul 1",(1,3):"punctul 3"}
#dict(iterabil de perechi chie,valoare)
d=dict([(1,"unu"),(2,"doi")])
print(d)
#comprehenisune
#Exc- frecventa elementelor dintr-o lista sub forma element:frecventa
ls=[4,5,1,3,5,4,4,5]
d={x:ls.count(x) for x in set(ls)}
print(d)
#accesarea valorii asociate unei chei:
# d[cheie]- KeyError daca cheia nu exista in dictionar
print(d[4])
d={(1,2):"punctul 1",(1,3):"punctul 3"}
print(d[(1,3)])
#print(d[(1,5)]) #KeyError: (1, 5)
#d.get(cheie,valoare_default=None) - daca nu gaseste cheia intoarce valoarea default
# (sau None daca nu este specificata o valoare default)
print(d.get((1,5),"nu exista"))
print(d.get((1,5)))

#operatorul in:
if (1,5) in d:
    print(d[(1,5)])
else:
    print("nu exista")

#STERGEREA unei chei ( a perechii cheie:valoare)
"""
del d[cheie] - eroare daca nu exista cheia in dictionar
d.pop(cheie,valoare_default) - valoare_default este parametru optional, este intoarsa daca nu exista cheia
"""

#ADAUGAREA unei perechi cheie:valoare in dictionar
d={1:"unu",2:"doi"}
#d[cheie]=valoare - insereaza perechea cheie:valoare daca nu exista cheia in dictionar,
#respectiv actualizeaza valoarea asociata cheii, daca aceasta este deja in dictionar
d[3]="trei"
print(d) #inserare 3:"trei"
d[3]="alt trei" #actualizarea valorii asociate lui 3
print(d)
#d.setdefault(cheie, valoare)
d.setdefault(4,"patru") #inserare, cheia nu exista in d
print(d)
d.setdefault(4,"alt patru") # cheia   exista in d => nu modifica nimic
print(d)
del d[4]
print(d)

#parcugere
for x in d: #implicit- itereaza cheile (la fel si operatorul in
    print(x)
print(d.keys()) #o lista(view) cu cheile din dictionar
print(d.values()) #cu valorile
print(d.items()) #cu perechi (cheie,valoare)
#pentru lista(view) returnat de d.keys() se pot folosi operatorii pentru multimi  & |
d1={"unu":5,"doi":7}
d2={"unu":7,"trei":2}
print(d1.keys()&d2.keys())
#adunam frecventele cuvintelor
d={x:d1.get(x,0)+d2.get(x,0) for x in d1.keys()|d2.keys()}
print(d)
"""
d={x:d1[x]+d2[x] for x in d1.keys()&d2.keys()}
print(d)
"""
for c,v in d.items():
    print(c,v)
print(sorted(d.items()))