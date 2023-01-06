f=open("numere_comune.in") #citire
"""
f.readline() #citeste o linie din fisier si o returneaza ca str
# !!! daca linia se termina cu un marcaj de sfarsit de linie => sirul intors se terima cu \n 
"""
#intersectie_multimi=set()
intersectie_multimi={int(x) for x in f.readline().split()} #initializam cu multimea de pe primia linie - cititia cu f.readline()
for linie in f:
    #print(linie)
    multime_linie={int(x) for x in linie.split()} #set([int(x) for x in linie.split()])
    print(multime_linie)
    #intersectie_multimi = intersectie_multimi & multime_linie
    intersectie_multimi.intersection_update(multime_linie) #puteam trimite si list ca parametru
print(sorted(intersectie_multimi))
print(*sorted(intersectie_multimi))
f.close()