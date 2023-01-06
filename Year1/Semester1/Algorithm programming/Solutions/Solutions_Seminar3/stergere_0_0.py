n=int(input("lungime lista"))
ls=[int(input()) for x in range(n)]
poz=ls.index(0)
del ls[poz:]
print(ls)