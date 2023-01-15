#%%
#Scrieți o funcție care primește ca parametru un număr natural și stabilește dacă numărul este prim.
def prim(n):
    if n<1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for d in range(3,n,2):
        if n%d==0:
            return False
    return True

print(prim(257))
#%%
#Scrieți o funcție care primește ca parametru o listă de numere naturale și returnează  două  liste:  una cu  numere  prime  și  alta  cu  numere  compuse, folosind funcția de la punctul a).
def f(lista):
    l_prime=[]
    l_compuse=[]
    for x in lista:
        if prim(x):
            l_prime.append(x)
        else:
            l_compuse.append(x)
    return l_prime,l_compuse

print(f([1,4,5,7,3,23,22,15]))

#%%
#c) Scrieți un program care citește din fișierul ”numere.txt”o listă de numere și afișează în fișierul ”prime.txt”lista numerelor prime, folosind funcția de la punctul b).
def prim2(ls):
    prime=[x for x in ls if prim(x)]
    compuse=[x for x in ls if not prim(x)]
    return prime,compuse

f=open("numere.txt","r")
ls=[int(x) for x in f.readline().split(",")]
with open("prime.txt", 'w')as g:
    g.write(str(prim2(ls)[0]))
f.close()
g.close()

#%%
#Definiți o funcție care primește ca parametru un număr variabil de numere naturale și întoarce lista formată doar din numerele pare.
def lspar(*argv):
    ls=[]
    for elem in argv:
        if elem%2==0:
            ls.append(elem)
    return ls

print(lspar(1,5,6,8,10))

#%%
#a) Scrieți o funcție care primește un număr variabil de parametri, numai liste de numere întregi, și returnează rezultatul concatenării listelor.
def concatls(*liste):
    ls=[]
    for lista in liste:
        ls+=lista
    return ls

print(concatls([1,4,5],[2,45,61],[1,7,8]))

#%%
#b) Scrieți un program care citește din fișierul ”liste.txt”, de pe fiecare linie, câte o listă de numere întregi și scrie în același fișierrezultatul concatenării listelor, folosind funcția de la punctul a).
f=open("liste.txt","r")
liste=[[int(x) for x in linie.split(",")] for linie in f.readlines()]
f.close()
with open("liste.txt","a") as g:
    g.write(str(concatls(*liste)))
#%%
#Ipoteza  Collatz  spune  că  plecând  de  la  orice  număr  natural,  dacă  aplicăm repetat următoarea operație𝑛⟼#𝑛2,𝑑𝑎𝑐𝑎𝑛𝑝𝑎𝑟3𝑛+1,𝑑𝑎𝑐𝑎𝑛𝑖𝑚𝑝𝑎𝑟șirul ce rezultă va atinge valoarea 1. Implementați o funcție recursivă, care returnează numărul de operații efectuatepână la atingerea valorii 1.

def collatz(n,op=0):
    if n==1:
        return op
    if n%2==0:
        return collatz(n//2,op+1)
    else:
        return collatz(3*n+1,op+1)

print(collatz(n=234))

#%%
#distanța  Levenshtein 
def lev(a,b):
    if len(a)==0:
        return len(b)
    if len(b)==0:
        return len(a)
    if a[0]==b[0]:
        return lev(a[1:],b[1:])
    return 1+min(lev(a[1:],b),lev(a,b[1:]),lev(a[1:],b[1:]))

print(lev("ana","alunelei"))

#%%
#nr cifre prime
def nr_cif_prime(n):
    if n<10 and n in [2,3,5,7]:
        return 1
    if n<10:
        return 0
    if n%10 in [2,3,5,7]:
        return 1+nr_cif_prime(n//10)
    return nr_cif_prime(n//10)

print(nr_cif_prime(157297))

#%%
#lista sortare
ls=[1,412,532,53,42,1241,24,21,4321]
#ls.sort(key= lambda x:len(str(x)),-sum([int(x) for x in str(x)]))

#%%

f=open("teatru.in","r")
d={}
pct="!?.,"
for linie in f:
    for x in pct:
        linie=linie.replace(x,"")
    ls=linie.strip("\n").split(": ")
    personaj=ls[0]
    replica=ls[1]
    cuvinte=replica.split(" ")
    for cuvant in cuvinte:
        key=cuvant.lower()
        if key in d.keys():
            if personaj not in d[key]:
                d[key].append(personaj)
        else:
            d[key]=[personaj]

ls=list(zip(d.keys(),d.values()))
ls.sort(key= lambda x : (-len(x[1]),x))

with open("teatru.out","w") as g:
    for tuplu in ls:
        personaje=tuplu[1]
        personaje.sort()
        str=",".join(personaje)
        g.write(f"{tuplu[0]} : {str}\n")
    
#%%
def citire(fisier):
    ls=[]
    with open(fisier,"r") as f:
        ls=[[int(x) for x in linie.split()]for linie in f]
    return ls

def modifica_matr(m,*indici):
    n=len(m)
    m.append([-1 if not j in indici else sum([m[i][j] for i in range(j) ]) for j in range(n)])
    m[:]=[[-1 if not i in indici else max(m[i][n-i-1:])] +m[i] for i in range(n+1)]
    
    
mat=citire("date.in")
n=len(mat)
modifica_matr(mat,0,1,n-1,n//2,(n-1)//2)
print('\n'.join([str(x).rjust(4) for x in mat[i]])for i in range(n+1))

#%%
def modifica_stare(d,s,o1,o2=""):
    cnt=0
    if o2:
        if (o1,o2) in d.keys():
            tuplu=d[(o1,o2)]
            tuplu[1]=s
            d[(o1,o2)]=tuplu
            cnt+=1
        
        

d={}
with open("drumuri.in") as f:
    for linie in f:
        ls=linie.strip("\n").split("-")
        oras1=ls[0]
        string=ls[1]
        ls=string.rsplit(" ",2)
        oras2=ls[0]
        dist=ls[1]
        stare=ls[2]
        d[(oras1,oras2)]=(int(dist),int(stare))

print(d)

#%%
d={}
f=open("text.in","r")
for linie in f:
    linie=linie.lower()
    for x in ":.,!?":
        linie=linie.replace(x,"")
    ls=linie.split()
    for cuv in ls:
        key=cuv
        if key in d.keys():
            d[key]+=1
        else:
            d[key]=1
n=max(d.values())
with open("text.out","w") as g:
    for i in range(n,0,-1):
        g.write(f"Frecventa {i}:\n")
        ls=[]
        for x in d.keys():
            if d[x]==i:
                ls.append(x)
        ls.sort()
        for elem in ls:
            g.write(f"{elem} \n")
            
#%%
def citire_matrice():
    with open("date1.in") as f:
        ls=[[int(x) for x in linie.split()] for linie in f]
        return ls
def functie(m,ch,x=0,y=0):
    n=len(m)-1
    if ch=="c":
        for i in range(n+1):
            aux=m[i][x]
            m[i][x]=m[i][y]
            m[i][y]=aux
    elif ch=="d":
        for i in range(n+1):
            aux=m[i][i]
            m[i][i]=m[i][n-i]
            m[i][n-i]=aux

mat=citire_matrice()
n=len(mat)-1
for i in range(n//2):
    functie(mat,"c",i,n-i)

functie(mat,"d")
print(mat)

i=0
with open("date1.out","w") as g:
    for linie in mat:
        if i%2==0:
            for elem in linie:
                g.write(f"{elem} ")
        else:
            linie.sort(key=lambda x : x)
            for elem in linie:
                g.write(f"{elem} ")
        i+=1
            
#%%
def citire_catalog():
    d={}
    f=open("catalog.in","r")
    n=int(f.readline())
    print(n)
    for elev in range(n):
        linie=f.readline().strip().rsplit(" ",1)
        nume=linie[0]
        materii=int(linie[1])
        for i in range(materii):
            ls=f.readline().strip().split(",",1)
            materie=ls[0]
            note=[int(x) for x in ls[1].split(",")]
            d[(nume,materie)]=note
    return d  

def detalii_elev(d,elev):
    ls=[]
    for cheie in d.keys():
        if cheie[0]==elev:
            note=d[cheie]
            media=sum(note)/len(note)
            if media<5 or len(note)<=1:
                media=0
            tuplu=(cheie[1],media)
            ls.append(tuplu)
    
    ls.sort(key= lambda x : x[0])
    for elem in ls:
        print(f"{elem[0]} : {elem[1]}")

def clasament(d,*nume_elevi):
    ls=[]
    for elev in nume_elevi:
        medie_generala=0
        cnt=0
        ok=0
        for cheie in d.keys():
            if cheie[0]==elev:
                note=d[cheie]
                media=sum(note)/len(note)
                if media<5 or len(note)<=1:
                    media=0
                    ok=1
                medie_generala+=media
                cnt+=1
        medie_generala/=cnt
        if ok:
            ls.append((elev,0))
        else:
            ls.append((elev,medie_generala))
    ls.sort(key= lambda x : -x[1])
    return ls

d=(citire_catalog())
#elv=input("elev=")
#detalii_elev(d,elv)
print(clasament(d,"Alin Enache","Ioana Matei"))


#%%
import math

def citire_matrice1(fisier):
    f=open(fisier,"r")
    ls=[[int(x) for x in linie.split()]for linie in f]
    n=len(ls[0])
    for linie in ls[1:]:
        if len(linie)!=n:
            return None
    return ls

def cifr(n): #prima si ult cifra egale
    nr=len(str(n))
    if n%10 == n//math.pow(10,nr-1):
        return True
    return False

def multimi(m,*indici):
    n=len(m)
    i=indici[0]
    set_neg_f={m[i][j] for j in range(n) if m[i][j]<0}
    set_poz_f={m[i][j] for j in range(n) if m[i][j]>=0 and cifr(m[i][j])==True}
    for i in indici[1:]:
        set_neg={m[i][j] for j in range(n) if m[i][j]<0}
        set_poz={m[i][j] for j in range(n) if m[i][j]>=0 and cifr(m[i][j])==True}
        set_neg_f&=set_neg
        set_poz_f|=set_poz
    return set_poz_f,set_neg_f

mat=citire_matrice1("matrice.in")

tuplu=multimi(mat,len(mat)-3,len(mat)-2,len(mat)-1)
ls_poz=[int(x) for x in tuplu[0]]
ls_poz.sort()
print(*ls_poz,sep=" ")

tuplu=multimi(mat,len(mat)-1,0)
ls_neg=[int(x) for x in tuplu[1]]
print(len(ls_neg),sep=" ")

#%%
def modifica_prefix(x,y,prop):
    ls=prop.split()
    prop_nou=[]
    cnt=0
    for cuv in ls:
        if cuv.startswith(x):
            cuv=cuv.replace(x,y)
            prop_nou.append(cuv)
            cnt+=1
        else:
            prop_nou.append(cuv)
    prop_nou=" ".join(prop_nou)
    return prop_nou,cnt

def poz_max(ls):
    pozitii=[i+1 for i in range(len(ls)) if ls[i]==max(ls)]
    return pozitii
            
a=input("a=")
b=input("b=")
f=open("propozitii.in")
ls=[]
for linie in f:
    prop_nou,nr=modifica_prefix(a,b,linie)
    with open("propozitii.out","a") as g:
        g.write(f"{prop_nou}\n")
    ls.append(nr)
rez=poz_max(ls)
print(*rez)

#%%
def sterge_carte(d,cod_carte):
    if cod_carte in d.keys():
        id_scriitor=d[cod_carte][0]
        d.pop(cod_carte)
        nume=d[id_scriitor]
        return nume
    else:
        return None
def carti_autor(d,cod_autor):
    nume=d[cod_autor]
    ls=[]
    for x in d.values():
        if x[0]==cod_autor:
            ls.append([x[3],x[1],x[2]])
    return nume,ls
            
f=open("autori.in")
ls=f.readline().split()
d={}
n=int(ls[0])
m=int(ls[1])
for i in range(n):
    ls=f.readline().strip("\n").split(maxsplit=1)
    key=(int(ls[0]))
    d[key]=ls[1]
for i in range(m):
    ls=f.readline().strip("\n").split(maxsplit=4)
    key=int(ls[0])
    cod_carte=int(ls[1])
    an=int(ls[2])
    nr_pag=int((ls[3]))
    nume=ls[4]
    d[cod_carte]=(key,an,nr_pag,nume)

#print(d)\
'''
cod_input=int(input("cod carte="))
nume=sterge_carte(d,cod_input)
if nume :
    print(f"Cartea a fost scrisa de {nume} \n {d}")
else:
    print("Cartea nu exista.")
'''
cod_autor=int(input("cod autor="))
nume,ls=carti_autor(d,11)

print(nume)
for carte in ls:
    print(" ".join(map(str,carte)))

#%%
f=open("text1.in")
d={}
n=0
for linie in f:
    linie=linie.strip("\n").lower()
    for x in linie:
        if x.isalpha():
            n+=1
            if x in d.keys():
                d[x]+=1
            else:
                d[x]=1
print(n)
print(d["e"])
for x in d.keys():
    d[x]=d[x]/n
    d[x]=round(d[x],3)

ls=list(zip(d.keys(),d.values()))
ls.sort(key=lambda x: (-x[1],x[0]))
for elem in ls:
    print(f"{elem[0]} : {elem[1]}")
#%%
def insereaza_legatura(d,cap1,cap2,culoare,eticheta):
    tuplu=tuple([cap1,cap2])
    for x in d.values():
        if tuplu==x:
            return False
        else:
            d[(culoare,eticheta)]=tuplu
            return True

f=open("legaturi.in")
d={}
for linie in f:
    ls=linie.strip("\n").split(maxsplit=3)
    culoare=ls[2]
    eticheta=ls[3]
    tuplu=tuple([[int(x) for x in ls[i].rstrip("]").lstrip("[").split(",")] for i in range(0,2)])
    cheie=(culoare,eticheta)
    d[cheie]=tuplu

print(d)

insereaza_legatura(d,(1,2),(1,3),"negru","legatura noua")
print(d)
#%%
def citire_numere(nume_fisier):
    f=open(nume_fisier,"r")
    ls=[[int(x) for x in linie.split()]for linie in f]
    return ls

def prelucrare_lista(ls):
    for subls in ls:
        minim=min(subls)
        subls[:]=[x for x in subls if x!=minim]
    m=min([len(subls) for subls in ls])
    for subls in ls:
        subls[:]=subls[:m]
    
    
ls=citire_numere("numere.in")
for linie in ls:
    print(" ".join(map(str,linie)))

k=int(input("k="))
ls_f=[]
for linie in ls:
    for elem in linie:
        if len(str(elem))==k and elem not in ls_f:
            ls_f.append(elem)
with open("numere.out","w") as g:
    if ls_f:
        ls_f.sort(key= lambda x : -x)
        g.write(" ".join(map(str,ls_f)))
    else:
        g.write("Imposibil!")

#%%
def sterge_ore(d,cinema,film,ore):
    for ora in ore:
        d[cinema][film].remove(ora)
    print(d[cinema][film])

def cinema_film(d,*cinemauri,ora_minima,ora_maxima):
    ls_f=[]
    for cinema in cinemauri:
        for film in d[cinema]:
            ls=[x for x in d[cinema][film] if x >= ora_minima and x<= ora_maxima]
            if ls:
                ls_f.append((film,cinema,ls))
    ls_f.sort(key= lambda x:(x[0],-len(x[2])))
    return ls_f
f=open("cinema.in","r")
d={}
for linie in f:
    ls=linie.strip("\n").split(" % ")
    ore=[x for x in ls[2].split()]
    cinema=ls[0]
    film=ls[1]
    if cinema in d.keys():
        d[cinema][film]=ore
    else:
        d[cinema]={film:ore}

ls=cinema_film(d,"Cinema 1","Cinema 2",ora_minima="14:00",ora_maxima="22:00")
print(ls)
