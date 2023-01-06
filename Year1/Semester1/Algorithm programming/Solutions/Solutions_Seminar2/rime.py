#a
'''
w=input("w=")
p=int(input("p="))
n=int(input("n="))
rez=""
print(w[:len(w)-p-1:-1])
for i in range(n):
    cuv=input()
    print(cuv[:len(cuv)-p-1:-1])
    if(len(cuv)>=p+2 and w[:len(w)-p-1:-1]==cuv[:len(cuv)-p-1:-1]):
            rez=rez+cuv+" "
print(rez)
'''
#b
w=input("w=")
p=int(input("p="))
sir=(input("sir="))
ls=sir.split()
rez=""
for cuv in ls:
    if (len(cuv) >= p + 2 and w[:len(w) - p - 1:-1] == cuv[:len(cuv) - p - 1:-1]):
        rez=rez+cuv+" "

print(rez)

