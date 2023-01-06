"""
a) lista cu literele mici
"""
#ord(caracter)=> codul ascii, chr(cod ascii)=>caracterul cu codul dat (caracterul - de tip str)
l_litere=[chr(i) for i in range(ord('a'),ord('z')+1)]
print(l_litere)

nr_litere=ord('z')-ord('a')+1
l_litere=[chr(i+ord('a')) for i in range(0,nr_litere)]
print(l_litere)

import string
print(string.ascii_lowercase)
#conversie str=>list - metoda 1
l_litere=[]
l_litere.extend(string.ascii_lowercase)
print(l_litere)
#conversie str=>list - metoda 2
l_litere=list(string.ascii_lowercase)
print(l_litere)
"""
b) cifrul lui cezar
"""
prop=input()
k=int(input())
"""
varianta 1 - cu comprehension
#(ord(c)-ord('a')+k)%nr_litere- indexul lui c+k modulo nr_litere
prop_cezar="".join([chr((ord(c)-ord('a')+k)%nr_litere+ord('a')) if "a"<=c<="z" else c for c in prop]) #c.isalpha()
print(prop_cezar)
"""
#varianta 2 - fara comprehension - cu append
prop_cezar=[]
for c in prop:
    if "a"<=c<="z":
        indice_c_k=(ord(c)-ord('a')+k)%nr_litere #se putea si cauta in l_litere
        prop_cezar.append(chr(indice_c_k+ord('a'))) #se putea l_litere[indice_c_k]
rezultat="".join(prop_cezar)
print(rezultat)
