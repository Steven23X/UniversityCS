#citire matrice
m,n=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for i in range(m)]

#det max pe linie
max_linii=[max(linie) for linie in a]

print(max_linii)
