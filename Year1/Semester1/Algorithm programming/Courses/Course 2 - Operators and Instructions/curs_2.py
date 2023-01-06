"""
#INSTRUCTIUNI
#1. Atribuire
x=y=1
print(x,y)
#tuple assignment
x,y=2,4
print(x,y)
x,y=y,x #x,y=(y,x)  x,y=(4,2)
print(x,y)
x,y=y,x+y #evalueaza tuplu din dreapta

#2. Instructiunea de decizie if
#ultima cifra a lui 3**k
k=int(input())
if k%4==0:
    print(1)
elif k%4==1: #pot lipsi
    print(3)
elif k%4==2:
    print(9)
else: #poate lipsi
    print(7)
#2. Instructiunea de decizie multipla match
k=int(input())
match k%4:
    case 0: print(1)
    case 1: print(3)
    case 2: print(9)
    case _: print(7) #default - daca nu se potriveste cu celelalte tipare din case, poate lipsi
x=int(input())
match x:
    case n if n<10: print("are o cifra")
    case n if n < 100: print("are doua cifre")
    case 100 | 101: print("100-101")
    case _: print("multe cifre")
#3.Instructiunea repetitiva cu test initial - while -
i=1
s=0
while i<10:
    s+=i
    i+=1
print(s)
#3.Instructiunea repetitiva cu test final - NU do - while
"""
#4. Instructiunea reptitiva cu nr fix de pasi -for
#for element in colectie:
#for caracter in sir:
#for element in lista:
vocale="aeiou"
for c in vocale:
    print(c, end="")
print()
for i in [0,1,2,3,4]:  #[0,1,2,3,4]-> list (vector)
    print(vocale[i], end="")
#functia range
#range(b)-> genereaza 0,1, ..., b-1 !!!!b exclusiv
#range(a,b) -> a,a+1,...,b-1
#range(a,b,pas) -> a,a+pas, a+2*pas,...
#nu returneaza o lista, genereaza numerele pe rand
print()
print(range(1,10))
print(*range(1,10))
for i in range(len(vocale)-1,-1,-1): #n-1,0,-1
    print(vocale[i], end="")
print()

#break, continue, else si pt structuri repetitive
#exemplu-primul divizor propriu al unui numar dat
x=int(input())
dx=None
for d in range(2,x//2+1):
    if x%d ==0:
        dx=d
        break #opreste for
if dx:
    print(dx)
else:
    print("nu are div proprii")


#else pt o structura repetitiva -se executa daca nu s-a iesit cu break
x=int(input())
#dx=None
for d in range(2,x//2+1):
    if x%d ==0:
        #dx=d
        print(d)
        break #opreste for
else:
    print("nu are div proprii")

if x<0:
    pass
