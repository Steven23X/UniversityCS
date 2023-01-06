"""
Se consideră o listă de liste (matrice) ls (de exemplu [[4,7, 3], [3,1,20], [5,2,11]] ).
Să se creeze o listă cu toate elementele din ls ordonate crescător (pentru exemplu [1, 2, 3, 3, 4, 5, 7, 11, 20]). (folosind și comprehensiune)
"""

"""METODE DE SORTARE
ls=[9,5,6,7]
ls_sortata=sorted(ls) #ls nu se modifica, se creeaza o lista noua sortata
print(ls,ls_sortata)

ls=[90,5,6,7,12]
ls.sort() #modifica lista
print(ls)
"""

matrice=[[4,7, 3], [3,1,20], [5,2,11]]
for linie in matrice: #linie este o lista
    for x in linie: #parcurgem element cu element linia
        print(f"{x:3}",end="")
    print()
v=[]
for linie in matrice: #linie este o lista
    for x in linie: #parcurgem element cu element linia
        v.append(x)
print(v)

#cu comprehensiune
v=[x for linie in matrice for x in linie]
print(v)

#suplimentar - initializarea unei matrice cu 0
n=3
m=4
mat=[[0 for i in range(m)] for j in range(n)]
print(mat)