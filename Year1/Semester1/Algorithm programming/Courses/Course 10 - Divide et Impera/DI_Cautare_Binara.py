def citire_vector_ordonat(nume_fisier):
    f=open(nume_fisier)
    ls=[int(x) for x in f.read().split()]
    return ls


def cautare_binara(x,ls,p,u):
    if p > u:
        return (False,u)
    else:
        mij = (p + u) // 2
        if x == ls[mij]:
            return (True,mij)
        elif x < ls[mij]:
            return cautare_binara(x,ls, p, mij-1)
        else:
            return cautare_binara(x,ls, mij+1, u)

def cautare_binara_nerecursiv(x,ls):
    p=0
    u=len(ls)-1
    while p<=u:
        mij = (p + u) // 2
        if x == ls[mij]:
            return (True, mij)
        elif x < ls[mij]:
            u = mij - 1
        else:
            p = mij + 1
    return (False,u)



def cautare(x,ls):
    n = len(ls)
    return cautare_binara(x,ls,0,n-1)


def cautare(x,ls):
    n=len(ls)
    return cautare_binara(x,ls,0,n-1)

ls=citire_vector_ordonat("vector.in")
x=int(input("Dati valoarea cautata "))
rez=cautare(x,ls)
if rez[0]:
    print(f"{x} gasit pe pozitia {rez[1]}")
else:
    print(f"{x} nu este in vector {rez[1]}")

rez=cautare_binara_nerecursiv(x,ls)
if rez[0]:
    print(f"{x} gasit pe pozitia {rez[1]}")
else:
    print(f"{x} nu este in vector {rez[1]}")