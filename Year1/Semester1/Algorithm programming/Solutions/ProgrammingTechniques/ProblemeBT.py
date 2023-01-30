#%%
#submultimile unei multimi date
#submultimile multimii {1,2,...,n}
#submultimi = combinari de n luate cate m=0,1,2,3,...n
#sumbmultime - vector caracteristic - binar de lungime n 00010.1..0 elementul i este in multime <=>xi=1
#pb se reduce la a genera toate sirurile binare de lungime n folosind backtracking:
#reprez sol x=(x0,...,x_{n-1})
#valori pt xk - 0 sau 1
#cond final - nimic
#cond continuare - nimic

def back(k):
    if k==n:
        #print(*x)
        print([a[i] for i in range(n) if x[i]==1])
    else:
        #dam valoare lui x[k]:
        for i in range(0,2):
            x[k]=i
            back(k+1)

a=[3,1,7,9]
n=len(a)
x=[0 for i in range(n)]
back(0)

#%%
"""
PERMUTARI(n)
Reprezentare solutie:
x=(x0,...,x_{n-1}) - o permutare
Fiecare pozitie xk poate lua valori de la 1 la n
Cond finale - elemente distincte
Cond de continuare la pasul k (valid(k)): xk sa fie diferit de x0...xk-1
"""
def bkt(k):
    for v in range(1,n+1):
        x[k]=v
        if x[k] not in x[:k]:
            if k==n:
                print(*x[1:])
            else:
                bkt(k+1)
n=int(input("n="))
x=[0 for i in range(n+1)]
bkt(1)
#%%
#aranjamente
def back1(k):
    global x,n
    for v in range(1,n+1):
        x[k]=v
        if x[k] not in x[:k]:
            if k==m:
                print(*x[1:],sep=" ")
            else:
                back1(k+1)
        
        

n=4
m=2
x=[0]*(m+1)
back1(1)

#%%
#combinari
def back2(k):
    global x,m,n
    for v in range(x[k-1]+1,n+1):
        x[k]=v
        if x[k] not in x[:k]:
            if k==m:
                print(*x[1:],sep=" ")
            else:
                back2(k+1)

n=4
m=2
x=[0]*(m+1)
back2(1)

#%%
def back3(k):
    global n,set_cuvant,x
    for i in range(1,n+1):
        x[k]=i
        if x[k] not in x[1:k]:
            if k==n:
                print("".join([cuvant[x[i]-1] for i in range(1,n+1)]))
            else:
                back3(k+1)
    
cuvant="rama"
n=len(cuvant)
set_cuvant=set(cuvant)
x=[0 for i in range(n+1)]
back3(1)

#%%
def suma(k):
    global n,x
    for v in range(1,n+2-k):
        x[k]=v
        suma_curenta=sum(x[:k+1])
        if suma_curenta<=n:
            if suma_curenta==n:
                print(*x[1:k+1],sep=" ")
            else:
                suma(k+1)
    
n=int(input("n="))
x=[0 for i in range(n+1)]
suma(1)
#%%
def suma1(k):
    global n,x
    for v in range(1,n-k+2):
        x[k]=v
        suma_curenta=sum(x[:k+1])
        if suma_curenta <=n and x[k] not in x[:k]:
            if suma_curenta==n:
                print(*x[1:k+1],sep=" ")
            else:
                suma1(k+1)
n=int(input("n="))
x=[0 for i in range(n+1)]
suma1(1)

#%%

def conditie(pas):
    elem=x[pas]
    if pas==1:
        return True
    
    for i in range(1,pas):
        if abs(x[i]-elem)>k:
            return False
    return True
    
def norocel(pas):
    global G,n,k,x
    for v in range(1,G-pas+2):
        x[pas]=v
        suma_curenta=sum(x[:pas+1])
        if suma_curenta<=G and pas<=n and conditie(pas):
            if suma_curenta==G and pas==n and len([i for i in x if i==1])==1:
                print(*x[1:pas+1],sep="+")
            else:
                norocel(pas+1)
        
G=int(input("G="))
n=int(input("n="))
k=int(input("k="))
x=[0 for i in range(G)]
norocel(1)

#%%
#monezi
def suma(x,k):
    sk = 0
    for i in range(k + 1):
        sk += x[i] * v[i]
    return sk

def solutie_posibila(k): # <=S
    return suma(x,k)<=s
def solutie():
    return suma(x,n-1)==s
def afisare():
    print(*x,sep=",")
    
def moneda(k):
    if k==n:
        if solutie():
            afisare()
    else:
        for i in range(s//v[k]+1):
            x[k]=i
            if solutie_posibila(k):
                moneda(k+1)
                
v=[1,5,10]
n=len(v)
s=20
x=[0 for i in range(n)]
moneda(0)
#%%
def suma1(x,k):
    sk = 0
    for i in range(k + 1):
        sk += x[i] * v[i]
    return sk

def solutie_posibila1(k): # <=S
    return suma(x,k)<=s
def solutie1():
    return suma(x,n-1)==s
def afisare1():
    print(*x,sep=",")
    
def moneda1(k):
    if k==n:
        if solutie1():
            afisare()
    else:
        for i in range(nr[k]+1):
            x[k]=i
            if solutie_posibila1(k):
                moneda1(k+1)
                
v=[1,5,10]
n=len(v)
s=20
M=8
nr=[4,5,3]
x=[0 for i in range(n)]
moneda1(0)
#%%
#produs cartezian
def solutie_posibila2(k):
    return True
def solutie2():
    return True
def afisare2():
    print(*x,sep=" ")
def produs(k):
    if k==n:
        if solutie2():
            afisare2()
    else:
        for i in range(len(ls[k])):
            x[k]=ls[k][i]
            if solutie_posibila2(k):
                produs(k+1)
n=3
ls=[]
for i in range(n):
    ls.append([int(x) for x in input().split()])
x=[0 for i in range(n)]
produs(0)
#%%
#intrebari - punctaj ???
def solutie_posibila3(k):
    if k==0:
        return True
    return sum(x[:k])<=p and y[k]>y[k-1]

def solutie3():
    return sum(x)==p

def afisare3():
    print("intrebarile:",end="")
    print(*y,sep=",")
        
def chestionar(k):
    if k==a:
        if solutie3():
            afisare3()
    else:
        for i in range(len(v)):
            x[k]=v[i][0]
            y[k]=v[i][1]
            if solutie_posibila3(k):
                chestionar(k+1)
                
#n=6
n=int(input("n="))
#a=3
a=int(input("a="))
#p=10
p=int(input("p="))
poz=1
for i in range(n):
    v[i]=[int(input()),poz]
    poz+=1
#v=[[1,1],[4,2],[2,3],[3,4],[5,5],[4,6]]

x=[0 for i in range(a)]
y=[0 for i in range(a)]
chestionar(0)
#%%
def prim(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for d in range(3,n//2,2):
        if n%d==0:
            return False
    return True

def solutie_posibila4(k):
    return sum(x[:k])<=n and x[k]>=x[k-1]
def solutie4(k):
    return sum(x[:k])==n
def afisare4(k):
    print(*x[:k],sep="+")
    
def prime(k):
    if solutie4(k):
        afisare4(k)
    else:
        for i in range(len(v)):
            x[k]=v[i]
            if solutie_posibila4(k):
                prime(k+1)
n=int(input("n="))
x=[0 for i in range(n)]
v=[i for i in range(n) if prim(i)]
prime(0)

#%%
import math

def solutie_posibila5(k):
    if x[k] in x[:k]:
        return False
    if k==0:
            return True
    return math.gcd(x[k],x[k-1])==1

def solutie5():
    return True

def afisare5():
    print(*x,sep=" ")
    
def bkt1(k):
    if k==n:
        if solutie5():
            afisare5()
    else:
        for i in range(n):
            x[k]=nr[i]
            if solutie_posibila5(k):
                bkt1(k+1)
                    
f=open("sirpie.in")
n=int(f.readline())
nr=[int(x) for x in f.readline().split()]
nr.sort()
print(nr)
x=[0 for i in range(n)]
bkt1(0)

#%%
def solutie_posibila6(k):
    if k==0:
        return True
    if x[k]>x[k-1]:
        return True
    return False
def solutie6():
    if v[0] not in x or v[nrf] not in x:
        return False
    baieti=len([i for i in range(nrf+1,nrb+nrf+1) if i in x])
    fete=len([i for i in range(nrf+1) if i in x])
    return fete==baieti
def afisare6():
    print(*x,sep=",")
    
def elevi(k):
    if k==s:
        if solutie6():
            afisare6()
    else:
        for i in range(k,len(v)):
            x[k]=v[i]
            if solutie_posibila6(k):
                elevi(k+1)
            
nrf=4
nrb=3
s=4
x=[0 for i in range(s)]
v=[i for i in range(1,nrb+nrf+1)]
elevi(0)
#%%
#problema teava
def afisare7(k):
    global cnt
    print(*x[:k],sep="+")
    cnt+=1
def solutie7(k):
    print(len(set(x[:k])))
    if True!=2:
        return False
    return sum(x[:k])==p
def solutie_posibila7(k):
    if k==0:
        return True
    else:
        return sum(x[:k+1])<=p and x[k]>=x[k-1]
def teava(k):
    if solutie7(k):
        afisare7(k)
    else:
        for i in range(len(v)):
            x[k]=v[i]
            if solutie_posibila7(k):
                teava(k+1)
cnt=0  
p=int(input("p="))
x=[0 for i in range(p)]
v=[i for i in range(1,p) if p%i==0]

teava(0)
print(cnt)

#%%
global cnt
def solutie_posibila8(k):
    if sum(x[:k+1])>c:
        return False
    elem=x[k]
    for i in range(0,k):
        if abs(x[i]-elem)>p:
            return False
    return True
def solutie8(k):
    if sum(x[:k])==c and x[0]==x[k-1]:
        return True
def afisare8(k):
    print(*x[:k],sep="")
def marginit(k):
    if solutie8(k):
        afisare8(k)
    else:
        for i in range(1,c+1):
            x[k]=i
            if solutie_posibila8(k):
                marginit(k+1)
        
p=int(input("p="))
c=int(input("c="))
x=[0 for i in range(c)]
marginit(0)
#%%
def conditie_posibila9(k):
    if k==0:
        if x[k] not in "aeiou":
            return False
    elem=x[k]
    for i in range(k):
        if x[i]==elem:
            return False
    return True

def solutie9():
    return True

def afisare9(k):
    print(*x[:k])
def parola(k):
    if k==n:
        if solutie9():
            afisare9(k)
    else:
        if T[k]=='l':
            for j in range(len(L)):
                x[k]=L[j]
                if conditie_posibila9(k):
                    parola(k+1)
        else:
            for j in range(len(S)):
                x[k]=S[j]
                if conditie_posibila9(k):
                    parola(k+1)
n=6
T=['l','s','l','s','l','l']
L=['a','b','c','D']
S=['@','.']
x=[0 for i in range(n+1)]
parola(0)