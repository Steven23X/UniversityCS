def frecv(nume_fisier):
    f=open(nume_fisier,"r")
    linie=f.read().splitlines()
    linie="".join(linie)
    d = {x: linie.count(x) for x in linie}
    return d


d1=(frecv("caractere1.in"))
d2=(frecv("caractere2.in"))

#c).
s1=set(d1)
s2=set(d2)
rez=s1 &s2

for x in rez:
    if d1[x]>d2[x]:
        print(x,"=>",d2[x])
    else:
        print(x, "=>", d1[x])