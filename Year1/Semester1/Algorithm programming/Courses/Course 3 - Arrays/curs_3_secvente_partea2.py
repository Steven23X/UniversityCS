#INTEROGARI, CAUTARI in secvente
#operatorii in, not in
s="un sir de caractere"
if "sir" not in s:
    print(s, 'nu contine subsecventa "sir"')
else:
    print('"',s, '" contine subsecventa "sir"',sep="")
#metoda count
#count(elemnt_cautat, start, end) - start si end sunt optinali, ca la feliere
#numara in felia s[start:end]
s="acesta este un exemplu"
print(s.count("a")) #in tot sirul
print(s.count("a",1)) #incepand cu pozitia 1
print(s.count("a",1,5))#numara in s[1:5] exclusiv 5

#index(element, start, end)
#pozitia primei aparitii, daca elementul se afla in secventa
#daca elementul nu se alfa in structura => eroare ValueError
s="acesta este un exemplu"
poz=s.index("a")
print("prima pozitie pe care apare a",poz)
poz=s.index("a",poz+1)
print("a doua pozitie pe care apare a",poz)
#poz=s.index("a",poz+1)
#print("a treia pozitie pe care apare a",poz) =>ValueError
try:
    #bloc de instructiuni
    poz=s.index("a",poz+1)
    print("a treia pozitie pe care apare a",poz)
except:
    #se executa cand blocul de instructiuni din try arunca exceptie
    print("nu apare de 3 ori")
#Exercitiu - toate pozitiile pe care apare in s un carater dat
s="acesta este un exemplu"
c="a"
try:
    poz=s.index(c)
    while True:
        print(poz,end=" ")
        poz=s.index(c,poz+1)
except:
    pass

print()
"""
Recomandare - cate o ramura except pt fiecare exceptie care poate fi aruncata din try,
pentru a trata exceptiile diferentiat
# except ValueError:
"""


#OPERATORI relationali,+,*n
#concatenare cu + => obiect nou, cu copierea operatorilor
s1="un"
s2="alt"
s=s1+" "+s2
ls=[2,3]
ls2=[4,5]
ls=ls+ls2 #obiect nou in care copiaza ls, ls2
#recomandare - pentru a adauga elementele unei liste la o alta lista -metoda extend,
# care modifica valoarea obiectului curent, nu creeaza altul nou
ls.extend(ls2)
print(ls)
#copiere - copiere superficiala, de referinte
ls = [[1,2],[4,5]]
ls2=[[5,6]]
ls3=ls+ls2+ls
print(ls3)
ls3[0][0]=130
print(ls3)
print(ls)
#multiplicare cu *n
s="ab"*5
n=10
ls=[0]*n
print(ls)
ls[1]=12
print(ls)

#operatorii relationali <,<=... - comparare lexicografica/element cu element, nu dupa lungime
ls=[4,5]
ls2=[1,2,3]
print(ls>ls2) #adevarat, pt ca 4>1
s="uv"
s2="abc"
print(s>s2)
ls=[1,2,3]
ls1=[2,3,1]
print(ls==ls1) #fals- conteaza ordinea elementelor in secventa


#SORTARE sorted(secventa)=>returneaza o lista
#exista posibilitate (vom reveni) sa specificam si un criteriu propriu de comparare
ls=[4,1,2]
print(sorted(ls))
print(ls) #lista initiala nu se modifica
print(sorted("pauza"))#=> tot lista ['a', 'a', 'p', 'u', 'z']