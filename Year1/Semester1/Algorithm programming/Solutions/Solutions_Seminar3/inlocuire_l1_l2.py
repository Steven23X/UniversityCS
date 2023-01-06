l1=[1,2,3,45,6,7,8,21,3]
l2=[0,0,0,0,0,0,0,0,0,0]

for i in range(len(l1)):
    if i%2==0:
        l1[i]=l2[i]

print(l1)
