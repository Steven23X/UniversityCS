#FUNCTII
"""
def functie(parametri formali): - antetul functiei
    corp
    return...
functia se apeleaza cu paramteri actuali/efectivi
(valori sau expresii care se trimit la apelul functiei
"""
def f(x): #param formal x
    print(x)
f(3+5) #param actual 3+5

#RETURNEAZA - orice tip de date si oricat valori (separate cu virgula= > tuplu)
#daca nu returneaza ceva explicit - returneaza None
print(f(3+5))
ls=[5,3]
#l=sorted(ls)
#l=ls.sort()!!!l=None
print(sorted(ls))
print(ls.sort()) #None

#TRANSMITEREA PARAMETRILOR
#C/C++ - valoare (copie), referinta (adresa)
"""
Python - prin atribuire (se transmite prin valoare referinta catre obiect
=>singurele modificari vizibile dupa incheierea exec functiei sunt
cele asupra valorii parametrilor mutabili
"""
def modifica(x):
    x=8
    print(x)
a=9
modifica(a)
print(a)

def creare(ls):
    ls=[1,2,3] #nou obiect=> se modifica referinta
ls=[]
creare(ls)
print(ls)

def modificare(ls):
    ls.extend([1,2,3]) #nu cream un nou obiect, modific valoarea celui existent
ls=[]
creare(ls)
print(ls)

#DOMENIUL DE VIZIBILITATE
#la interogare - variabila este cautata in spatiul curent, apoi in cel global;
# mai exact-regula LEGB (Local, Enclosing(pt functii incluse in alte functii), G-global, B-builtin)

def f():
    print(x)
x=90
f()

#o variabila se creeaza prima data cand i se atribuie o valoare
#la prima atribuire intalnita, daca variabila nu exista in spatiul curent, se creeaza
# (la atribuire nu cauta LEGB)
def f():
    x=15 #prima atribuire- se creeaza o variabila x in local
    print(x) #x din local =>15
x=90
f()
print(x) #x din global =>90

"""
def f():
    print(x) #UnboundLocalError: local variable 'x' referenced before assignment
    x=15 #x este var locala
x=90
f()
print(x)  
"""
def f():
    global x #specificam spatiul(domeniul) unde cauta variabila
    print(x) # x din global
    x=15 #modifica x din global
x=90
f()
print(x)  #va afisa 15
"""
def f(x):
    x[0]=1

x=5
f(x)
"""
"""
Tipuri de parametri:
- parametri obligatorii (trebuie sa primeasca obligatoriu valoare la apel)
- parametri cu valoare implicita, atribuita in antet (optionali- pot lipsi la apelul 
functiei si atunci se foloseste valoare implicita)
- functii cu nr variabil de parametri (paremtru care aduna in el mai multe valori)
"""
"""
Parametri obligatorii
la apelul functiei putem trimite valori pt parametri obligatorii:
-prin pozitie (param actuali respecta ordinea si numarul param din antet)
-prin nume nume_param=valore => nu mai trebuie respectata ordinea
se pot combina - dar intai se dau cei prin pozitie
in anumite contexte - este obligatoriu ca param sa fie dati prin pozitie (positional only)
sau obligatoriu prin nume (keyword only argument)
"""
def scrie(x,y,z):
    print(x,y,z)
scrie(1,2,3) #prin pozitie
scrie(y=2,x=1,z=3) #prin nume
scrie(1,z=3,y=2)
"""
SUPLIMENTAR - putem specifica in antet ca este obligatoriu ca param sa fie dati prin pozitie
scrie(x,y,z,/)
sau obligatoriu din nume
scrie(*,x,y,z)
"""
"""
Parametri cu valori default (implicita) - in antet dupa cei obligatorii
exp: index(x), index(x,start)...
"""


# suma elementelor din lista cupprinse in intrevalul [lim_inf,lim_sup]
def suma(lista,lim_inf=0,lim_sup=100):
    s=0
    for x in lista:
        if lim_inf<=x<=lim_sup:
            s+=x
    return s
lista=[-1,3,6,120,2]
print(suma(lista)) #elementele din [0,100] - val implicite pt lim_inf si lim_sup
print(suma(lista,5))#lim_inf devine 5, pentru lim_sup se foloseste valoarea implicita
print(suma(lista,5,150))
print(suma(lista,lim_sup=150))

"""
FUNCTII CU NUMAR VARIABIL DE PARAMETRI
*parametru (prefixat de *) - poate primi la apel mai multe valori
"""
"""
def suma(val_initiala,*numere,lim_inf,lim_sup=100):
    print(val_initiala)
    print(numere) #impachetate in tuplu


print(suma(1,6,7,-1,102)) 
#daca lim_inf nu are voare default => eroare "missing 1 required keyword-only argument: 'lim_inf'"
print(suma(1,6,7,-1,lim_inf=102)) 
print(suma(5,2))
#parametri de dupa paramterul variabil trebuie specificati prin nume (!obligatoriu prin nume)
"""

def suma(val_initiala,*numere,lim_inf=0,lim_sup=100):
    print(val_initiala)
    print(numere) #impachetate in tuplu
    s=val_initiala
    for x in numere:
        if lim_inf<=x<=lim_sup:
            s+=x
    return s

print(suma(0,1,6,7,-1,lim_sup=102))

#o functie poate primi ca parametru o alta functie
def f(x):
    return x*x
def suma(*numere,functia):
    s = 0
    for x in numere:
        s += functia(x)
    return s
print(suma(3,5,-1,10,functia=abs))
print(suma(3,5,-1,10,functia=f))
ls="12 34 198"
print(list(map(int,ls.split())))
#SORTARE
ls=[("Primul",101,8),("Nume 1",100,10),("Alt nume",100,10),("Eu",101,9) ]
#sortam dupa nume:
print(sorted(ls)) #implcit -dupa prima componenta, in caz de egalitate dupa urmatoarea...
#Sortam dupa grupa crescator si in cadrul grupei dupa nota tot crescator
def cheie(element):
    #un tuplu
    #fiecare element din tuplu -corespunde unui criteriu
    return element[1],element[2]
print(sorted(ls,key=cheie))
#putem sorta descrescator dupa un criteriu
print(sorted(ls,key=cheie,reverse=True))
cuvinte=["nu","cuvinte","multe","gata","am"]
#sortam dupa lungime descrecator
cuvinte.sort(key=len,reverse=True ) #sortare stabila - in caz de egalitate pastreaza ordinea din sirul initial
print(cuvinte)
#sortam dupa ultima litera
def cheie(x):
    return x[-1]
cuvinte.sort(key=cheie)
print(cuvinte)
cuvinte.sort(key=lambda x:x[-1]) #suplimentar x->(x[1m)
print(cuvinte)
#ls de numere=>numere pare inaintea celor impare, cele pare sortate crescator, cele impare descrescator
ls=[13,4,5,16,7,8,1,11]
def cheie(x):
    if x%2==0:
        return 0,x
    else:
        return 1,-x
ls.sort(key=cheie)
print(ls)

"""
SUPLIMENTAR -generator
"""
def f(n):
    for i in range(1,n):
        yield i*i #furnizeaza, nu returneaza
t=f(5)
print(next(t))
print(next(t))
#print(sum(t))
for x in t:
    print(x,end=" ")
