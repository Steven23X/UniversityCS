"""Dată o listă de numere naturale și un număr k,
propuneți mai multe modalități de a șterge primele k elemente din listă
"""
ls=[int(x) for x in input().split()]
k=int(input())
"""
#var 1 - ok
del ls[:k]
print(ls)

#var 2 - ok
ls[:k]=[]
print(ls)
"""
"""
#var 3 - ineficient!!!! !!daca k este mai mare decat lungimea lui ls -eroare IndexError
for i in range(k):
    ls.pop(0)
print(ls)
"""
"""var 4 - produce alt obiect
print(id(ls))
ls=ls[k:] #???- nu modifica lista, creeaza un alt obiect - nerecomandat
print(ls,id(ls))
"""
"""var 5 - modifica chiar ls, dar foloseste copiere pt felia ls[k:]
print(id(ls))
ls[:]=ls[k:] #acelasi obiect
print(ls,id(ls))
"""