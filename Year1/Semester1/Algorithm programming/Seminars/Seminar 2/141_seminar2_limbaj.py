#Sa se verifice dacă un număr dat de la tastatură este pătrat perfect.
import math
x=9
if int(x**0.5)==x**0.5:
    print("este pp")
else:
    print("nu este pp")
if math.sqrt(x).is_integer():
    print("este pp")
else:
    print("nu este pp")
#from math import sqrt - se va apela direct sqrt(x), fara a prefixa cu math (fara numele modulului)


#Ce afiseaza?
for i in range(10):
    print(i, end=" ")
print(i) #ramana cu ultima valoare din secventa parcursa: 0,1,2..,9
print()

for i in range(10):
    print(i, end=" ")
    i="ab"
    print(i, end=" ")
    # i devine umratorul elemnt din secventa parcursa, deci va lua tot la rand valorile 0,1,2..,9
for i in range(10):
    print(i, end=" ")
    i+=2
    print(i)
    #i devine umratorul elemnt din secventa parcursa, deci va lua tot la rand valorile 0,1,2..,9
print(i)

#feliere (sliceing)

s= "acest exemplu"
print(s[0:6])#s[0],...,s[5]
print(s[0:6:2])#s[0],s[2],s[4]
print(s[0:6:-2]) #de la 0 la stanga cu pasul 2=>secventa vida
print(s[0::2])
print(s[::100])#s[0], s[100]-nu exista=> intoarce s[0]
print(s[::-100]) #ultimul element s[-1]
print(s[-3:-1])
print(s[0:4])
print(s[-1:4])
print(s[len(s):])
print(s[::-1])
print(s[-1:-14:-1]) #cu indici pozitivi: s[12:-1:-1] -nu este corect, -1 este indicele ultimului element
print("gata")


#Se citește un cuvânt s. Să se verifice dacă s este palindrom sau semipalindrom (format din două jumătăți egale)
#s="abcba" ->palindrom
#s="abcabc" -> semipalindrom
s=input("un cuvant: ")
if s==s[::-1]:
    print("palindrom")
elif (len(s)&1==0) and (s[:len(s)//2]==s[len(s)//2:]):
    print("semipalindrom")
else:
    print("nu este nici palindrom, nici semipalindrom")

#Dat un sir s si o pozitie k, numeroatate de la 0, sa se stearga elementul de pe pozitia k
s="acest exemplu"
k=2
s=s[:k]+s[k+1:]
print(s)

#Dat un sir s, sa se stearga prima vocala din sir
s="sterg vocala"
#s="bcd"
for i in range(len(s)):
    if s[i] in "aeiou":
        s = s[:i] + s[i + 1:]
        print(s)
        break
else: #se executa doar daca for nu s-a terminat cu break
    print("nu are vocale")

