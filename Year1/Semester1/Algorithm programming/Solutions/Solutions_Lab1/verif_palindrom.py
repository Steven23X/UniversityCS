x=int(input("x="))
cx=x
rez=0
p10=10
while cx>0:
    c=cx%10
    cx=cx//10
    rez=rez*p10+c

print(rez)

if rez==x:
    print(x," Este Palindrom")
else:
    print(x," Nu este Palindrom")