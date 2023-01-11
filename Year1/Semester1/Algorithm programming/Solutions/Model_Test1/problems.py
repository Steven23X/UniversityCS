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

print(rima1("date1.in","date2.in","date3.in",p=2))
        