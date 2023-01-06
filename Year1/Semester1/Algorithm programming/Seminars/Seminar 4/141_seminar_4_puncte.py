f=open("puncte.in")
"""
for linie in f:
    ls=linie.split()
    print(ls)
    x=int(ls[0])
    y=int(ls[1])
    eticheta=" ".join(ls[2:])
    print(x,y,eticheta)
"""
d={}
d1={}
for linie in f:
    ls=linie.split(maxsplit=2)
    x=int(ls[0])
    y=int(ls[1])
    eticheta=ls[2].rstrip("\n")
    print(x,y,repr(eticheta))
    d[(x,y)]=eticheta #d.setdefault((x,y), eticheta) - daca exista deja eticheta, nu o actualizeaza
    if (x,y) not in d1:
        d1[(x,y)]=[eticheta]
    else:
        d1[(x, y)].append(eticheta)
    #d.setdefault((x,y), []).append(eticheta)
f.close()
print(d)
print(d1)
f=open("interogari.in")
for linie in f:
    x,y,tip_operatie=[int(x) for x in linie.split()]
    punct=(x,y)
    if tip_operatie == 1: #interogare= > eticheta sau "nu exista"
        """
        if punct in d:
            print(f"({punct[0]},{punct[1]}) {d[punct]}")
        else:
            print(f"({punct[0]},{punct[1]}) nu exista")
        """
        print(f"({punct[0]},{punct[1]}) {d.get(punct,'nu exista')}")
    else:
        if punct in d:
            del d[punct]
        #d.pop(punct,"")

f.close()
print("punctele ramase")
for punct in d:
    print(f"({punct[0]},{punct[1]}) {d[punct]}")

print("punctele ramase")
for punct,eticheta in d.items():
    print(f"({punct[0]},{punct[1]}) {eticheta}")