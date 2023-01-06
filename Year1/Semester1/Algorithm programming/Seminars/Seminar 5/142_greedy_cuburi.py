f=open("cuburi.in")
n,p=[int(x) for x in f.readline().split()]
cuburi=[]
i=1
for linie in f:
    latura,culoare=[int(x) for x in linie.split()]
    cuburi.append((latura,culoare,i)) #si indicele cuburi.append((latura,culoare,i))
    i+=1
f.close()
cuburi.sort(reverse=True)
print(cuburi)
solutie=[]
inaltime=0
for cub in cuburi:
    #daca cubul curent se poate adauga la solutie - culoare diferita de ultimul adaugat la solutie, adica solutie[-1]
    if (len(solutie)==0) or (cub[1]!=solutie[-1][1]):
        solutie.append(cub)
        inaltime+=cub[0]
print(inaltime)
print(solutie)