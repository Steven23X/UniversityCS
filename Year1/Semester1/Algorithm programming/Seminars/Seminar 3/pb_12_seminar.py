"""
Se dă o listă de numere naturale și un număr natural k.
Să se elimine din listă subsecveța de lungime k de sumă minimă
(dacă sunt mai multe se va elimine prima = cea mai din stânga)
– fără a folosi liste suplimentare
"""
v=[int(x) for x in input().split()]
k=int(input())
s=sum(v[:k])
s_min=s
poz_min=0
for i in range(1,len(v)-k+1): #i=pozitia de inceput a subsecventei
    s = s - v[i-1] + v[i+k-1]

    if s<s_min:
        s_min=s
        poz_min=i
del v[poz_min:poz_min+k]
print(v)
