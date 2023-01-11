#%%
#review later
import heapq
with open("date.in") as f:
    l=f.readlines()
    l=list(map(lambda x: x.strip().split(),l))
    for i in range(len(l)):
        l[i]=list(map(int,l[i]))
    l.sort()
    sali=[[l[0]]]
    heap=[(l[0][1],0)]
    heapq.heapify(heap)
    for i in range(1,len(l)):
        spectacol=heapq.heappop(heap)
        if spectacol[0]<=l[i][0]:
            sali[spectacol[1]].append(l[i])
            heapq.heappush(heap, (l[i][1],spectacol[1]))
        else:
            sali.append(l[i])
            heapq.heappush(heap,spectacol)
            heapq.heappush(heap,(l[i][1],len(sali)-1))
            
    print(sali)

#%%
def prog(m,m0,i,j):
    if i==0 and j==0:
        print(m0[i][j])
    else:
        if i==0:
            prog(m,m0,i,j-1)
            print(m0[i][j])
        elif j==0:
            prog(m,m0,i-1,j)
            print(m0[i][j])
        else:
            if max(m[i-1][j],m[i][j-1])==m[i-1][j]:
                prog(m,m0,i-1,j)
                print(m0[i][j])
            else:
                prog(m,m0,i,j-1)
                print(m0[i][j])
    
mat=[]
with open("numere.in") as f:
    linie=f.readline().split()
    while linie:
        linie=[int(x) for x in linie]
        mat.append(linie)
        linie=f.readline().split()
n=len(mat[0])
mat_sume=[[0 for j in range(n)]for i in range(n)]
mat_sume[0][0]=mat[0][0]
for i in range(1,n):
    mat_sume[0][i]=mat[0][i]+mat_sume[0][i-1]
    mat_sume[i][0]=mat[i][0]+mat_sume[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        mat_sume[i][j]=max(mat_sume[i-1][j],mat_sume[i][j-1])+mat[i][j]

for i in range(0,n):
    print(*mat_sume[i]) #despachetare metrice

prog(mat_sume,mat,n-1,n-1)