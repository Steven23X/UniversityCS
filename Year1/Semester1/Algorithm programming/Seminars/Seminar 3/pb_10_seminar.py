"""
Se dă o listă de numere naturale.
Să se șteargă din listă subsecvența delimitată de primele două zerouri din listă
(inclusiv zerourile)
"""
ls=[int(x) for x in input().split()]

try:
    poz_1=ls.index(0)
    poz_2=ls.index(0,poz_1+1)
    del ls[poz_1:poz_2+1] #ls[poz_1:poz_2+1]=[]
    print(ls)
except:
    print("nu exista cel putin 2 de 0 in lista")
"""
if ls.count(0)>1: #dezavantaj-parcurge lista o data ca sa numere 0
    poz_1=ls.index(0)
    poz_2=ls.index(0,poz_1+1)
    del ls[poz_1:poz_2+1] #ls[poz_1:poz_2+1]=[]
    print(ls)
else:
    print("nu exista cel putin 2 de 0 in lista")
"""