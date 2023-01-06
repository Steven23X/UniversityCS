f=open("litere.in","r")
g=open("litere.out","w")
d={}
sir=f.read().splitlines()
sir="".join(sir)
ls=sir.split()
for x in ls:
    if frozenset(x) in d:
        d[frozenset(x)].add(x)
    else:
        d[frozenset(x)]=set()
        d[frozenset(x)].add(x)

for x in d:
    if list(d[x]).count >=2:
    ls=list(d[x])
    print(ls)


print(d)

