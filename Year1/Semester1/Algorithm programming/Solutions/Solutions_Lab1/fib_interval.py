a=int(input("a="))
b=int(input("b="))
nr=0
f1=f2=1

if a==1 or b==1 : nr=f1

while nr==0:
    f=f1+f2
    f1=f2
    f2=f
    if f>= a and f<=b: nr=f

print(nr)
