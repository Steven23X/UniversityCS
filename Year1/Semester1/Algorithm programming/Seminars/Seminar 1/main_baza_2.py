p=1
n=0
x=int(input("x=")) #input() returneaza str - sir de caractere - trebuie conversie
aux=x
while x!=0:
    i=x%2
    x=x//2
    n=n+p*i
    p=p*10
print(n)
print(bin(aux))
x=0b10001
print(52&5)
