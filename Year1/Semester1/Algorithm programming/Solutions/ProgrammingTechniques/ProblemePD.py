#problema traseu triunghi
#citire triunghi
f=open("triunghi.txt")
t=[[int(x) for x in linie.split()]for linie in f]
print(t)
n=len(t)
#generare triunghi auxiliar
s=[[0]*(i+1) for i in range(n)]

#copiem ultima linie
for i in range(n):
    s[n-1][i]=t[n-1][i]

for i in range(n-2,-1,-1):
    for j in range(i+1):
        s[i][j]=t[i][j]+max(s[i+1][j],s[i+1][j+1])
print(s)
print(f"Suma maxima este {s[0][0]}")

#afisare traseu
j=0
for i in range(n-1):
    print(f"{t[i][j]} : ({i},{j})")
    if s[i+1][j+1]>s[i+1][j]:
        j+=1
print(f"{t[n-1][j]} : ({n-1},{j})")

#%%
#problema rucsacului (discreta)
f=open("obiecte.txt")
G=int(f.readline())
g=[0]
c=[0]
for linie in f:
    aux=linie.split()
    g.append(int(aux[0]))
    c.append(int(aux[1]))
f.close()
#det nr obiecte
n=len(g)-1
#matrice cmax
cmax=[[0 for x in range(G+1)]for x in range(n+1)]
#calculam elem cmax folosinf relatia de recurenta
for i in range(1,n+1):
    for j in range(G+1):
        cmax[i][j]=cmax[i-1][j]
        if g[i]<=j and c[i]+cmax[i-1][j-g[i]] > cmax[i-1][j]:
            cmax[i][j]=c[i]+cmax[i-1][j-g[i]]
print(f"Castigul maxim este:{cmax[n][G]}")
i=n
j=G
while i!=0:
    if cmax[i][j] != cmax[i-1][j]:
        print(i,end=" ")
        j-=g[i]
    i-=1

#%%
#tabla de sah
#citire
f=open("tabla.txt")
aux=f.readline().split()
n=int(aux[0])
m=int(aux[1])
mat=[[int(x) for x in linie.split()] for linie in f]
#gen mat auxiliara
s=[[0 for i in range(m)]for i in range(n)]
s[n-1][m-1]=mat[n-1][m-1]
#gen linie mat auxiliara
for j in range(n-2,-1,-1):
    s[n-1][j]=mat[n-1][j]+s[n-1][j+1]
for i in range(m-2,-1,-1):
    s[i][m-1]=mat[i][m-1]+s[i+1][m-1]

#gen restul matricei auxiliare
for i in range(n-2,-1,-1):
    for j in range(m-2,-1,-1):
        s[i][j]=mat[i][j]+max(s[i+1][j],s[i][j+1])
print(f"Suma maxima este : {s[0][0]}")
i=0
j=0
while i<n and j<m:
    print(f"{mat[i][j]} : ({i+1},{j+1})")
    if s[i+1][j] > s[i][j+1]:
        i+=1
    else:
        j+=1
    if i==n-1:
        while j<m:
            print(f"{mat[i][j]} : ({i+1},{j+1})")
            j+=1
    else:
        while i<n:
            print(f"{mat[i][j]} : ({i+1},{j+1})")
            i+=1
    
#%%
prop="masa carte sac teatru tema rustic sare" #pp cuvintele lung>=2
sir=prop.split()
n=len(sir)
lung=[0 for i in range(n)]
pred=[-1 for i in range(n)]
lung[0]=1 #pred[0]ramane -1
imax=0
for i in range(1,n):
    lmax=0
    for j in range(i):
        if (sir[j][-2:]==sir[i][:2]) and (lung[j]>lmax):
            lmax=lung[j]
            pred[i]=j
    lung[i]=1+lmax
    if lung[i]>lung[imax]:
        imax=i
print(lung)
print(pred)
print(imax)
print("lungime ",lung[imax])
print("un subsir")
rez=[]
while imax!=-1:
    rez.append(sir[imax])
    imax=pred[imax]
print(*rez[::-1])

#%%
prop="unu mama marte carte mare teatru doi" #pp cuvintele lung>=2
sir=prop.split()
n=len(sir)
lung=[0 for i in range(n)]
pred=[-1 for i in range(n)]
d={}
lung[0]=1 #pred[0]ramane -1
imax=0
sufix_cuv=sir[0][-2:]
d[sufix_cuv]=0
print(d)
for i in range(1,n):
    """
    lmax=0
    for j in range(i):
        if (sir[j][-2:]==sir[i][:2]) and (lung[j]>lmax):
            lmax=lung[j]
            pred[i]=j
    lung[i]=1+lmax
    """
    sufix_cuv=sir[i][-2:]
    prefix_cuv=sir[i][:2]
    if  prefix_cuv in d:
        lung[i]= 1 + lung[d[prefix_cuv]]
        pred[i] = d[prefix_cuv]
    else:
        lung[i] = 1

    if lung[i]>lung[imax]:
        imax=i

    #actualizarea dictionarului
    if sufix_cuv in d:
        if lung[i]>lung[d[sufix_cuv]]:
            d[sufix_cuv]=i
    else:
        d[sufix_cuv]=i
    print(d)

print(lung)
print(pred)
print(imax)
print("lungime ",lung[imax])
print("un subsir")
rez=[]
while imax!=-1:
    rez.append(sir[imax])
    imax=pred[imax]
print(*rez[::-1])
def f(x,y):
    return x+y
ls=[8,9]
print(f(*ls))

#%%
'''v = [None, 12, 1, 3, 4, 5, 7]
           i
M = 14


sume:     0      1     2    .....        12        14
i = 0    True                          False
i = 1    True  False  False.......     True  
i = 2                                  True

                                                 True


termen:

termen[i][s] = v[i]


a[i][s] - True / False : pot obtine suma s din primele i elemente

a[i - 1][s]: True 
a[i - 1][s] == False and s >= v[i] and a[i-1][s - v[i]] == True
  a[i][s] = True

'''



     