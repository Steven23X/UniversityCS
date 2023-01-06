#copiere superficiala = de referinte
ls=[1,2]
ls1=[[3,5]]
ls1.append(ls)
print(ls1,ls)
ls[0]=78
print(ls1,ls) #se modifica si ls si ls1[1] pentru ca refera acelasi obiect
ls1[1]=[4,6]
print(ls1,ls)
x=5
ls1.append(5)
print(ls1)
ls1[2] =ls1[2]+2#ls[1] va referi alt obiect fata de x
print(ls1,x)

#metoda copy - tot copiere superficiala
#pntru copiere "deep" - exista metoda deepcopy din modul copy
ls=[[1,2],[2,3],8]
ls1=ls.copy()
ls[0][0]=12
print(ls,ls1) #ls[0] si ls1[0] refera acelasi obiect
ls[2]=7 #acum ls[2] va referi un alt obiect decat ls1[2]
print(ls,ls1)
ls[0]=[3,4]#acum ls[0] va referi un alt obiect decat ls1[0]
print(ls,ls1)
import copy
ls1=copy.deepcopy(ls) #ls[0] si ls1[0] NU mai refera acelasi obiect
ls[0][0]=12
print(ls,ls1)

#si operatorii +, * fc copiere superficiala
n=2
m=3
a=[[0]*n]*m
print(a)
a[0][0]=13 #a[0],a[1],..., a[m-1] refera acelasi obiect, lista [0]*n
print(a)
a=[[0 for i in range(n)] for j in range(m)]
a[0][0]=13 #a[0],a[1],..., a[m-1] refera obiecte diferite,
# pentru fiecare j se creaza o lista [0 for i in range(n)] corespunzatoare liniei j
print(a)

#sortarea:sorted vs sort
#metoda comuna sorted(iterabil)=> returneaza o lista ce elementele din iterabil ordonate
ls=sorted("pauza")
print(ls)
#sorted(lista) nu modifica lista, ci returneaza una noua cu elementel ordonate
ls=[5,3,1,5]
sorted(ls)
print(ls) #ramane nesortat
ls_sortat=sorted(ls)
print(ls_sortat,ls)
#ls=sorted(ls) - nerecomandat
#daca vrem ca sortarea sa modifice lista - metoda sort din clasa list
ls=[5,3,1,5]
ls.sort() #modifica ls
print(ls)
#NU ls=ls.sort() - sort() nu returneaza lista, returneaza None
#print(ls) #None

#NU ls=ls+ls1 (copiere+creare alt obiec) => DA ls.extend(ls1)

#COMPLEXITATI OPERATII
#listele- vectori de referinte
#ls[i]=>O(1)
#pop(0), del ls[0]=> O(n) face deplasari
#-------------------
#TUPLURI - secvente indexate de la 0, ca si list, dar imutabil
#clasa tuple - acelasi operatii ca si list, mai putin cele care permit modificarea valorii
#+aceeasi operatori, feliere
print("TUPLURI")
x,y=1,2
#CREARE
t=(3,5)#cu () in loc de []
print(t,type(t))
t=3,4 #parantezele pot lipsi
print(t,type(t))
t=(3,[2,3]) #neomogene
t=()
print(t,type(t))
t=(2) #nu este tuplu cu un singur element, () pt prioritate, ca sa fie privit ca tuplu tb sa apara ,
print(t,type(t))
t=(2,) #tuplu cu un singur element
print(t,len(t),type(t))
#t=tuple(iterabil)
t=tuple("abcd")
print(t)
t=tuple(range(3))
print(t)
s="o vocala"
print(s.startswith(tuple("aeiou"))) #testeaza daca s incepe cu un element din tuplu
#comprehensiune - NU are
ls=[x for x in range(10)]
print(ls)
t=(x for x in range(1,10))#generator - genereaza elemente "la cerere" dupa o regula
print(t,type(t))
print(next(t)) #genereaza un element =>1, mai raman de generat 2,3,...10
print(sum(t)) #genereaza 2,3,...,10 => 44
print(sum(t)) #suma 0
#imutabile
t=(1,2)
#t[0]=4 #TypeError: 'tuple' object does not support item assignment
#nu putem modifica catre ce obiect refera t[0]
t=([5,6],2)
t[0][1]=23 #pot modifica valoare obiectului referit de t[0], daca acesta este mutabil
print(t)
#UTILIZARE
#tuple assignment
x,y=1,2 #despachetare, nr de variabile din stg tb = lungime tuplu
x,*y=1,2,3 #*-impachetare
print(x,y)
#functii care returneaza mai multe valori
def f(x,y):
    return x+y,x*y #tipul returnat-tuplu
t=f(3,5)
print(t,type(t)) # t este tuplu
s,p=f(3,5)
print(s,p,type(s),type(p))
#cheie in dictionare