#SIRURI DE CARACTERE - Clasa str
#CREARE:
s="un sir"
s='un sir' #nu exista char
s="""un sir
pe mai multe linii"""
s='''un sir
pe mai multe linii'''
#constructor str -pentru conversie
s=str(13.5)
print(s)
s=str(1==2)
print(s)
s=str()
print(s)
#caractere speciale, secv escape \n \t, \'
s='it\'s time \u0103'
print(s)
#este imutabil, nu putem modifica valoarea unui caracter din sir
#s[0]="a" -> NU
#CAUTARE
#find(element, start, end) -similar cu index, dar returneaza -1 daca nu gaseste elemntul in sir
#rfind, rindex - pozitia primei aparitii de la dreapta la stanga
#Exercitiu - toate poz pe care apare un caracter folosind find
s="acesta este un sir"
c="a"
poz=s.find(c)
while poz!=-1:
    print(poz, end=" ")
    poz=s.find(c,poz+1)
print()
#Modificarea unui sir => alt sir
#folosim concatenare de felii - pentru modificari legate de pozitie
#exemplu-stergerea elementului de pe pozitia k
s="un sir"
k=3
s=s[:k]+s[k+1:]
print(s)
#replace(old, new, count) - inlocuieste un subsir cu alt subsir;
# param count este optional; daca nu se specifica sunt inlocuite toate aparitiile
#altfel sunt inlocuite doar primele count aparitii
s="acesta acela"
s=s.replace("a","aa")
print(s)
s=s.replace("a","",2) #doar primele 2 aparitii
print(s)

#transformari la nivel de caracter: lower(), upper(), title()
s=s.upper()
print(s)

#testare - islower(), isupper(),isdigit(), isalnum() => True/False

#DIVIZARE, UNIFICARE
#split(separator) - imparte sirul folosind ca delimitator separatorul specificat ca paramatru
#daca nu se specifica separatorul, implicit se considera separator caracterele albe
#!!!se poate transmite un singur separator/delimitator ca parametru
#returneaza o lista cu cuvintele din sir
prop="aceasta   este o propozitie"
ls=prop.split()
print(ls)
prop="aceasta, este o, propozitie"
ls=prop.split(", ") #separatorul va fi o virgula urmata de spatiu
print(ls)
#putem transmite metodei split si un paramatru maxsplit care specifica cate impartitir sa faca
# (lista returnata va ava cel mult maxsplit+1 cuvinte)
s="Marinescu Ruxandra profesorul de PA"
print(s.split(" ",2))
print(s.split(maxsplit=2))
#exista si rsplit - functioneaza la fel ca split, dar face imartirea de la dreapta
s="Marinescu Ruxandra 1 2 3"
print(s.rsplit(" ",3))
print(s.rsplit(maxsplit=3))

#pentru a concatena elementele unei liiste de cuvinte folosind un delimitator dat
#se poate folosi metoda join: delimitator.join(lista)

s="Marinescu Ruxandra profesorul de PA"
ls=s.split()
s=", ".join(ls)
print(s)
ls=sorted("pauza")
print(ls)
s="".join(ls)
print(ls)

#f-stringuri - siruri de formatare
#campuri de formatare cuprinse intre acolade - pot contine direct variabile sau expresii
x="ab"
y="abcde"
s=f"{x} este subsir al lui {y}"
print(s)
x=8
y=3
#8+3=3+8=11
print(f"{x}+{y}={y}+{x}={x+y}")
x=1.1+2.2
print(f"{x}")
print(f"{x:f}")
print(f"{x:.2f}") #cu 2 zecimale
x=9
print(f"{x}")
print(f"{x:b}")
print(f"{x:16b}") #pe 16 caractere
print(f"{x:016b}") #pe 16 caractere, spatiul ramas se umple cu 0




