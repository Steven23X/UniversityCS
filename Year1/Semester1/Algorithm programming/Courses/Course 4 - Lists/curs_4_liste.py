#SECVENTE - colectii indexate de la 0
#SIRURI DE CARACTR - clasa str
#formatare
#f-stringuri- template cu campuri de formatare cuprinse intre {} - care pot contine var sau expresii
x=8
y=2
print(f"{x}+{y}={y}+{x}={x+y:8.2f}")
print("{}+{}={}+{}={:8.2f}".format(x,y,y,x,x+y)) #campurile de formatare {} se inlocuiesc cu parametrii metodei format
print("{0}+{1}={1}+{0}={2:8.2f}".format(x,y,x+y)) #in campurile de formatare putem pune pozitia parametrului cu care vrem sa se inlocuiasca

#alte metode pentru formatare: center(dimensiune,[fillchar]), rjust...
s="titlu"
print(s.center(20)) #fillchar este implicit spatiu
print(s.center(20,"*"))
print(f"{s:20}") #implicit alinierea pt siruri de caractere se face la stanga in spatiul de dimensiune indicata,
# iar pentru numere la dreapta (v.exp anterior)
print(f"{s:^20}")#^ = aliniere in centrul spatiului de dimensiune indicata

#pt a elimina caractere de la inceputul si sfarsitul unui sir - metodele strip, rstrip, lstrip
#metodele primesc ca parametru sirul caracterelor pe care vrem sa le eliminam
s=" ,tit,lu ,, "
s=s.strip(", ")
print(s)
s=""
s=''
s=str()

#LISTE - clasa list
#memorate - vectori de referinte la elemente
#creare
ls=[3,1,4]
ls=[2,"abc"] #pot fi neomogene - elementele pot avea tipuri de date diferite
ls=[[1,2],[3,4]] #lista de liste - matrice
ls=[]
ls=list()
#constructor list(iterabil) creaza o lista avanad ca elemente elementele din iterabil:
#ls=[]
#for c in iterabil:
#    ls.append(c)
ls=list("abcde") #['a', 'b', 'c', 'd', 'e']
print(ls)
ls=list(range(10))
print(ls)

#listele sunt mutabile - se pot modifica (aduga elemente, sterg etc) fara a crea obiect nou
ls=[1,2]
ls[1]="abc" #[1, 'abc'] ls[i]=element
print(ls)
ls=[1,2]
ls.append("abc") #"abc privit ca element =>[1, 2, 'abc']
print(ls)
ls=[1,2]
ls.extend("abc") #"abc privit ca iterabil/secventa => [1, 2, 'a', 'b', 'c']
print(ls)


ls=[1,2]
ls.append([3,4]) #"abc privit ca element =>[1, 2, [3,4]]
print(ls)
ls=[1,2]
ls.extend([3,4]) #"abc privit ca iterabil/secventa => [1, 2, 3, 4]
print(ls)
#ACTUALIZARE UNEI LISTE (stergeri, inserare etc)
"""
modificarea unui element:  ls[i]=element (!IndexError dc i nu este corect)
actualizari folosind felieri (slice)
ls[i:j]=iterabil (nu neaparat de aceeasi dimensiune)
ls[i:j:k]=iterabil (de aceeasi dimensiune)
del ls[i] 
del ls[i:j]
del ls[i:j:k]
"""
ls=list(range(6)) #[0, 1, 2, 3, 4, 5]
print(ls)
ls[1:2]=[12,13,14] #[0, 12, 13, 14, 2, 3, 4, 5]
print(ls)
"""
ls[::2]=[0,0] #ValueError: attempt to assign sequence of size 2 to extended slice of size 4
print(ls)
"""
ls[::2]=[0]*((len(ls)+1)//2)
print(ls)


ls=[1,2,3]
ls[len(ls):]=[4,5] #nu da IndexError, ci adauga la finalul listei - ca si extend
print(ls) #[1, 2, 3, 4, 5]
i=1
ls[i:i]=[8,9] #[1, 8, 9, 2, 3, 4, 5] - inserarea secventei incepand cu pozitia i
print(ls)

del ls[1]
print(ls)
del ls[3:5]
print(ls)
"""
Metode pentru a modifica lista:
append(element)
extend(iterabil)
insert(poz, element) - insereaza pe pozitia i elementul element
pop(poz) => elimina elementul de pe pozitia pe pozitia pos si il returneaza; implicit poz=-1
=>daca apelam pop fara parametru sterge ultimul element
remove(element) - elimina prima aparitie din lista a elementului element (!Eroare daca nu exista)
clear()
"""
ls=[1,2,3,4,5]
ls.insert(2,"abc") #elementul abc
print(ls)
ls[2:2]=["abc"]
print(ls)
#ls[2:2]=5 TypeError: can only assign an iterable
ls[2:2]=[5]
print(ls)
poz=2
x=ls.pop(poz)
print(f"am sters elementul {x} de pe pozitia {poz}")
#pop(poz) cu feliere?
ls[poz:poz+1]=[]
print(ls)

ls.remove("abc")
print(ls) #sterge doar prima aparitie
#ls.remove(12)#ValueError: list.remove(x): x not in list
x=12
if x in ls:
    ls.remove(x)
try:
    ls.remove(x)
except ValueError:
    print(f"{x} nu se afla in lista {ls}")

#crearea unei liste cu secvente de initializare /list comprehension /comprehensiune
"""
ls=[expresie for x in iterabil]
ls=[]
for x in iterabil:
    ls.append(expresie)
"""
#vector initializat cu 0
ls=[0 for i in range(10)]
print(ls)
#primele 10 patrate perfecte
ls=[i*i for i in range(1,11)]
print(ls)
#citirea unei liste de numere intregi cu elementele date pe o linie
"""
cuvinte=input("dati lista").split()
ls=[int(x) for x in cuvinte]
"""

ls=[int(x) for x in input("dati lista").split()]
print(ls)

#secvente de initializare conditionate
"""
ls=[expresie for x in iterabil if conditie]
ls=[]
for x in iterabil:
    if conditie:
        ls.append(expresie)
"""
#exemplu
ls=[1,-3,-2,5,9]
ls_pozitive=[x for x in ls if x>0]
print(ls_pozitive)

ls1=[1,3,5,7,9]
ls2=[9,7,2,4,1,10,11]
#intersectia celor 2 liste =elementele comune
ls=[x for x in ls1 if x in ls2]
print(ls)

"""
inlocuiri in iterabil:
ls=[expresie1 if conditie2 else expresie 2 for x in iterabil ]
"""
#inlocuim in lista elemetele negative cu 0 => noua lista
ls=[1,2,3,-4,-6,9]
ls1=[x if x>0 else 0 for x in ls]
print(ls1)

#suma cuvintelor care sunt numere (naturale) din sir => lab jurnalul Anei
prop="am dat 20 lei pe mere si 10 lei pe pere"
print(sum([int(x) for x in prop.split() if x.isdigit()]))
perechi=[(x,y) for x in range(3) for y in range(3) if x!=y]
print(perechi)
"""
ls=[]
for x in range(3):
  for y in range(3): 
    if x!=y:
        ls.append((x,y))
"""


