# -*- coding: utf-8 -*-
"""
Exercitii Test
"""

#%%
#problema 1
s="Rac, rac ingrat cu rating, eram intr-un car mare de argint cu arc."
d={}
s=s.lower()
for x in ".,;!?":
    s=s.replace(x," ")
ls=s.split()

for cuv in ls:
    key=frozenset(cuv.lower())
    if key in d and cuv not in d[key] :
            d[key].append(cuv)
    else:
        d[key]=[]
        d[key].append(cuv)
print(d)

for x in d.values():
    if len(x) >= 2:
        for i in range(len(x)):
            if i == 0:
                print(f"{x[i]} :")
            else:
                print(f"        {x[i]}")
            
#%%
#problema 2 a).
def rima (nume_fisier,p):
    d={}
    f=open(nume_fisier,"r")
    s=f.read().strip()
    for x in "!.,? ":
      s=s.replace(x," ")
    ls=s.lower().split()
    
    for cuv in ls:
        key=cuv[len(cuv)-p:len(cuv)]
        if len(key)>=p:
            if key in d and cuv not in d[key]:
                d[key].append(cuv)
            else:
                d[key]=[]
                d[key].append(cuv)
    return d

print(rima("date1.in",1))
#%%
#problema 2 b).
def rima1(*fisiere,p):
    d={}
    for fisier in fisiere:
        f=open(fisier,"r")
        s=f.read().strip()
        for x in "!.,?- ":
          s=s.replace(x," ")
        ls=s.lower().split()
        
        for cuv in ls:
            key=cuv[len(cuv)-p:len(cuv)]
            if len(key)>=p:
                if key in d and cuv not in d[key]:
                    d[key].append(cuv)
                else:
                    d[key]=[]
                    d[key].append(cuv)
        
    return d

d=rima1("date1.in","date2.in","date3.in",p=3)
ls=[]
for x in d.values():
    if len(x)>=2:
        ls.append(x)
ls.sort(key= lambda x: -len(x)) 
for grup in ls:
    grup.sort()
    print(",".join(grup))

#%%
#norma euclidiana
import math
def norma(*argv):
    suma=0
    for elem in argv:
        suma+=math.pow(elem,2)
    return math.sqrt(suma)

print(norma(5,3,2,4,5))

#%%
#proza
index=0
ls_final=[]
g=open("mesaje.txt","a")
with open("proza.txt") as f:
    linie=f.readline().strip()
    while linie:
        index+=1
        nr_prop=0
        print(linie)
        for i in range(len(linie)):
            if linie[i].isupper():
                nr_prop+=1
        for x in ",.?! ":
            linie=linie.replace(x," ")
        ls=list(filter(None,linie.split(" ")))
        cuv_max=max(ls)
        nr_carac=len(linie.split())
        ls_final.append((index,nr_prop,cuv_max,nr_carac))
        linie=f.readline().strip()
ls_final.sort(key= lambda x: x[3])
for linie in ls_final:
    g.write(f"Linia numarul {linie[0]} din fisier contine {linie[1]} propozitii si cel mai ling cuvant este {linie[2]}\n")