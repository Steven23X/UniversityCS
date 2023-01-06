v=[6,4,5,1]
S=9
n=len(v)
inf=S+1
nr=[inf for i in range(S+1) ]
monede=[0 for i in range(S+1)]
nr[0]=0
for s in range(1,S+1):
    nr_min=inf
    for i in range(n):
        if (v[i]<=s) and (nr_min>1+nr[s-v[i]]):
            nr_min=1+nr[s-v[i]]
            monede[s]=v[i]
    nr[s]=nr_min
print(nr)
print(monede)
if nr[S]<inf:
    print("nr minim monede",nr[S])
    s=S
    while s!=0:
        print(monede[s],end=" ")
        s=s-monede[s]
else:
    print("nu se poate")