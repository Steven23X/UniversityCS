"""
Se dă o listă de numere naturale.
Să se șteargă din listă toate zerourile.
"""
"""
#var 1 - cu remove repetat
ls=[int(x) for x in input().split()]
while 0 in ls:
    ls.remove(0) #sterge prima aparitie a lui 0 in lista
print(ls)
"""

ls=[int(x) for x in input().split()]
try:
    poz=0
    while True:
        poz=ls.index(0,poz)
        del ls[poz]

except:
    pass
print(ls)
#cu comprehension
ls=[x for x in ls if x!=0] #!!!obiect nou, nu modifica lista initiala - NU
ls[:]=[x for x in ls if x!=0] #modifica lista initiala