x=int(input())
s=0
print(bin(x))
while x!=0:
    if x&1==1:
        s+=1
    x>>=1
print(s)

