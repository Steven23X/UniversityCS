"""
se dau: un cuvant w, un numar p si
 a) un sir de n cuvinte -date cate unul pe linie
 b)o propozitie in care cuvintele sunt separate prin spatii
 Sa se afiseze care dintre cuvintele date sunt p-rime cu w (au ultimele p litere = ultimele p litree din w:
 w="pere"
 p=2
 Ana are mere pere prune si o avere:
 =>are mere pere avere

"""

"""

w=input("cuvant: ")
p=int(input())
#a) :citim n si cate un cuvant pe fiecare linie
n=int(input("numarul de cuvinte: "))
print("dati cuvintele, cate unul pe linie")
sufix_w=w[-p:]
rez=""
for i in range(n):
    cuv=input()
    if cuv[-p:]==sufix_w:
        rez=rez+cuv+" "
print(rez[:-1])
"""
#b)
"""
prop="Ana   are mere pere prune si o avere"
print(prop.split()) #lista cu cuvintele din prop, separator implicit- caractere albe

prop="Ana  are mere pere prune si o avere"
print(prop.split(" ")) #lista cu cuvintele din prop, separator dat ca parametru
"""

w=input("cuvant: ")
p=int(input())
#a) :citim p propozitie
prop=input("propozitie: ")
sufix_w=w[-p:]
rez=""
lista_cuvinte=prop.split()
for cuv in lista_cuvinte:
    if cuv[-p:]==sufix_w:
        rez=rez+cuv+" "
print(rez[:-1])



