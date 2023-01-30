def prim(k):
    if k<=1:
        return False
    if k==2:
        return True
    if k%2==0:
        return False
    for d in range(3,k,2):
        if k%d==0:
            return False
    return True


def divizori(*nr):
    d={}
    for numar in nr:
        for div in range(1,numar):
            if numar%div==0 and prim(div):
                if numar not in d.keys():
                    d[numar]=[div]
                else:
                    d[numar].append(div)
    return d

print(divizori(50,21))

#%%
litere_10=[chr(i) for i in range(97,107)]
print(litere_10)      

#%%
def med(k):
    n=len(str(k))
    s=0
    while k:
        s+=k%10
        k=k//10
    return s/n

def numere(*nr):
    d={}
    for numar in nr:
        medie=med(numar)
        if medie not in d.keys():
            d[medie]=[numar]
        else:
            d[medie].append(numar)
            d[medie].sort(key= lambda x: -x)
    return d

print(numere(82375, 201, 51, 73, 3456, 2855, 1021, 90, 153))

#%%
L=[i for i in range(100,1000)]
print(L)
#%%
def litere(*cuvinte):
    d={}
    for cuvant in cuvinte:
        dd={}
        for litera in cuvant:
            if litera in dd.keys():
                dd[litera]+=1
            else:
                dd[litera]=1
        d[cuvant]=dd
    return d

print(litere("programara","teste"))
#%%
numere=[i for i in range(10,100) if i%2==0 and i%6!=0]
print(numere)

#%%
def aparitii(*numere):
    d={}
    for numar in numere:
        d[numar]=[]
        s=set(str(numar))
        for elem in s:
            d[numar].append((int(elem),str(numar).count(elem)))
    return d
d=aparitii(1011,234,8158558)

l=[i for i in d.keys() if len(d[i])>=3]
print(l)

#%%
def palindrom(*cuvinte):
    d={}
    for cuvant in cuvinte:
        n=len(cuvant)
        if cuvant==cuvant[n::-1]:
            voc=[i for i in cuvant if i in "aeiou"]
            cons=[i for i in cuvant if i not in "aeiou"]
            voc.sort()
            cons.sort()
            if len(voc)>len(cons):
                d[cuvant]=list(set(voc))
            else:
                d[cuvant]=list(set(cons))
    return d
d=palindrom("asa","merem","palindrom")    
print(d)

#%%
import math
numere=[i for i in range(10,100) if i%7!=0 and pow(math.sqrt(i),2)!=i]
print(numere)