n=int(input("n="))
a=float(input())
maxi=0
n=n-1
poz=1
while n>0:
    b=float(input())
    if(abs(a-b)>maxi):
        maxi=abs(a-b)
        pozf=poz
    poz+=1
    n=n-1
    a=b

print("Cea mai mare crestere a fost",maxi," Intre zilele",pozf ,"si",pozf+1)