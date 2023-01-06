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