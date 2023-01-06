#SECVENTE - indexate de la 0
#listele - clasa list
ls = [3,6, 9,"alt element"] #pot fi si neomogene
print(ls, type(ls))
#tupluri - clasa tuple
t = (3,6, 9,"alt element") #pot fi si neomogene
print(t, type(t))
#siruri de caractere - clasa str
s="un sir"
print(s, type(s))

#mutabil/imutabil - pot sau nu modifica valoare
ls[0] =7
print(ls)
"""
s[0]="U" -> eroare, imutabil, la fel si pt tupluri
print(s)
"""

#Functii uzuale: len,max, min
print(len(ls),max(s))
#Accesarea unui element/ unei felii(slice)
#indice 0,len(s) -1 + indici negativi -1  - ultimul element, -2 penultimul...
s="Programarea"
print(s[0],s[-1],s[-2])
#s[i:j] => s[i],...,s[j-1]
#indicii pot lipsi -> considerat inceputul, respectiv sfarsitul secventei
print(s[1:4])
print(s[1:])
k=4
#prefixul de lungime k
print(s[:k])
#se pot folosi si indici negativi la feliere:
print(s[-5:-3])
#sufixul de lungime k
print(s[-k:])
#s[i:j:pas] s[i],s[i+pas]
print(s[::2])
print(s[::-1])
print(s[1:100]) #daca depasim len- este inlocuit cu len
print(s[100]) #eroare - IndexError