f=open("activitati.in","r")

s=[tuple(map(int,x.rstrip(")\n").lstrip("(").split(", "))) for x in f.readlines()]

for i in range(len(s)):
    s[i]=tuple(list(s[i])+ [i+1])

s=sorted(s,key= lambda x : x[0])

lungime=0
for x in s:
    inceput=lungime
    final=inceput+x[1]
    lungime+=x[1]
    intarziere=max(0,lungime-x[0])
    print(f"activitatea {x[2]} : intervalul [{inceput},{final}) - intarziere {intarziere}")
