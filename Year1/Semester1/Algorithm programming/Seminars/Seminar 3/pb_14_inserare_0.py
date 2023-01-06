"""
Se dă o listă de numere reale
(toate elementele sale se vor da pe o linie separate prin spațiu).
Să se insereze câte un 0 după fiecare element negativ
(fără a folosi liste suplimentare)
"""

#inserare un element pe pozitia i:
#feliere ls[i:i]=[x]
#metode insert(i,x)
v=[int(x) for x in input().split()]
for i in range (len(v)-1, -1, -1):
    if v[i]<=0:
        v[i+1:i+1]=[0]
print(v)


v=[int(x) for x in input().split()]
i=0
while i<len(v):
#nu merge corect cu for i in range(len(ls)), len(ls) se modifica in for, dar range genereaza pana la len(ls) initial
    if v[i]<=0:
        v.insert(i+1,0)#v[i+1:i+1]=[0]
        i+=2
    else:
        i+=1
print(v)