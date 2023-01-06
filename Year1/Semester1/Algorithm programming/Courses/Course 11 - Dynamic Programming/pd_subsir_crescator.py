a=[5,1,6,3,4,2,7,9,8]
n=len(a)
lung=[0 for i in range(n)]
succ=[-1 for i in range(n)]
lung[n-1]=1 #ultimul element => subisr de lungime 1
i_max=n-1
for i in range(n-2,-1,-1):
    max_lung=0
    for j in range(i+1,n):
        if (a[j]>a[i]) and (lung[j]>max_lung):
            max_lung=lung[j]
            succ[i]=j
    lung[i]=1+max_lung
    if lung[i]>lung[i_max]:
        i_max=i
print(lung)
print(succ)
print("Lungimea maxima ",lung[i_max])
i=i_max
while i!=-1:
    print(a[i],end=" ")
    i=succ[i]