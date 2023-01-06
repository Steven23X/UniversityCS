#Deschidere -open(nume_fisier,mod_de_deschidere)
#mod_de_deschidere -optional: valori posibile:
#"r" - pt citire (implicit)
#"w" - pt scriere
#"a" -adaugare la final etc
#Inchidere -close()
f=open("numere.in") #pentru citire
f.close()
#folosind ladeschidere bloc with => nu mai trebuie fisierul inchis explicit,
#se inchide automat la finalul blocului:
with open("numere.in") as f:
    pass
#f se inchide automat
#Citire:
"""
daca o linie se termina cu sfarsit de linie, 
sirul corespunzator returnat la citire se termina cu \n
f.read() - returneaza ca str tot contnutul fisierului
f.readline()- returneaza ca str linia curenta
f.readlines() - returneaza o lista cu liniile din fisier (cu elemente de tip str)
f este iterabil
"""
f=open("numere.in")
s=f.read()
print(s)
print(repr(s))
f.close()

f=open("numere.in")
s=f.readline()
print("prima linie")
print(repr(s))
s=f.readline()
print("a doua linie")
print(repr(s))
f.close()

f=open("numere.in")
lista_linii=f.readlines()
print(lista_linii)
f.close()

#citire linie cu linie
#varianta 1
f=open("numere.in")
linie=f.readline()
while linie!="": #o linie vid din fisier=>"\n"
    print(repr(linie))
    linie=f.readline()
f.close()
#varianta 2
print("cu for (iteram f)")
with open("numere.in") as f:
    for linie in f: #linie cu linie
        print(repr(linie))
#SCRIERE
"""
-doar siruri de caractere
- nu adauga final de linie (!=print) 
f.write(un_sir)
f.writelines(colectie de siruri)
"""
f=open("numere.out","w")
x=15
f.write(str(x))#nu trece la linie noua
f.write("\n")
f.write(f"{x}")
f.close()
#exemplu - suma numerelor de pe fiecare linie dintr-un fisier
with  open("numere_suma.in") as f,open("numer_suma.out","w") as g:
    for linie in f:
        s=sum([int(x) for x in linie.split()])
        g.write(f"{s}\n")


