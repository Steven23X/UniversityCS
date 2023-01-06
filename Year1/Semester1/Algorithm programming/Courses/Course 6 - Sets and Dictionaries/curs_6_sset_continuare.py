#toate elemente-imutabile
#s={[2,3],[4,5]} #TypeError: unhashable type: 'list'
#nu sunt indexate => nu putem scrie s[i]
#PARCURGERE:
for s in set("un cuvant"): #ordinea elementelor in set nu este neaparat cea de la inserare
    print(s, end=" ") #caracterele distincte
print()
#sorted, len, min, max
#afisare ordonata crescator a literelor:
for s in sorted(set("un cuvant")):
    print(s, end="")
#OPERATORI
#in, not in => mediu O(1)
s={1,2,6}
if 0 in s:
    print("contine 0")
else:
    print("nu contine 0")
#==, !=
#[1,2,3]!=[3,2,1]
#{1,2,3}=={3,1,2}
s1={1,2,3}
s2={3,1,2}
print(s1==s2)
#<, <= - testeaza incluziunea
s1={1,2,3}
s2={3,2}
print(s2 <s1) #s2 este strict inclus in s1
#Operatori pentru operatii cu multimi - intre obiecte de tip set
# operatorul | reuniune
# operatorul & pentru intersectie
# operatorul - pentru diferenta
# operatorul ^ pentru diferenta simetrica
# a^b=elementele necomune =(a-b) reunit cu (b-a)=(a reunit cu b)- (a intersectat cu b)
s1={1,2,4,5,6}
s2={5,2,7}
s=s1^s2
print(s)
#se pot inlantui
s3={10,2}
s=s1|s2|s3
print(s)
#METODE pentru operatii cu multimi- pot primi ca parametri obiecte iterabile (liste, siruri) nu neaparat multimi
#tipul 1 de metode - returneaza multimea rezultat: union, intersection, difference,symettric_difference(*iterabili)
s1={1,2,4,5,6}
s2={5,2,7}
l3=[11,2,11]
s=s1.union(s2,l3, "ab")
print(s)

#s=s1|s2|l3|"ab" - TypeError: unsupported operand type(s) for |: 'set' and 'list'
#tipul 2 de metode - care modifica multimea care apeleaza metoda: update, intersection_update, difference_update...
s1.intersection_update(s2) #se modifica s1, nu returneaza o noua multime
print(s1)
s1={1,2,4,5,6}
s2={5,2,7}
s=s1.intersection(s2)
print(s,s1) #s1 nu s-a modificat

#add(element) - adauga un element la multime
# remove(element), discard(element) - elimina un element din multime (daca nu exista elementul remove da eroare)
s1={1,2,4,5,6}
s1.add(7)
s1.add(6) #daca exista deja nu da eroare
print(s1)
s1.discard(100)
#s1.remove(100) #KeyError: 100

#MULTIME IMUTABILA - frozenset
s1=frozenset({1,2,3,4})
s2=frozenset([4,5])
print(s1)
print(s2&s1) #operatii si metode ca la set, mai putn cele care modifica multimea
#s={{1,2},{3,4}} #TypeError: unhashable type: 'set'
s={(1,2),(3,4)}
s={frozenset({1,2}),frozenset({3,4})}
print(s)

