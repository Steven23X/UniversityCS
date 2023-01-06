f = open("numere_comune.in","r")
g = open("numere_comune.out","w")
linie=f.readline().strip()
s_i=set(linie.split())
linie=f.readline().strip()

while linie:
    s2 = set(linie.split())
    s_i=s_i & s2
    linie = f.readline().strip()

g.write(" ".join(s_i))