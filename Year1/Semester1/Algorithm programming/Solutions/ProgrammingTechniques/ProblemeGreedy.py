#%%
#Probleme Greedy
#Planificarea activităților cu minimizarea timpului mediu de așteptare
n=int(input("numar activitati: "))
i=0
t=[(int(x), i:=i+1) for x in input("durate: ").split()]
t.sort()
print(t)
t_total=0
t_anterior=0
print("ordine de executare a activitatilor")
for ti,i in t:
    t_anterior+=ti
    t_total+=t_anterior
    print(f"activitatea {i} a asteptat in total {t_anterior}s")
print(f"timpul mediu este {t_total/n:.2f}")

#%%
#Problema selectării activităților (problema spectacolelor)
def citire_intervale(nume_fisier):
    ls = []
    i=0
    with open(nume_fisier) as f:
        for linie in f:
            i=i+1
            s, t = (int(x) for x in linie.strip("[]\n").split(","))
            ls.append((i,[s,t])) #primul element- indicele activitatii, al doilea -intervalul de desfasurare (putea fi memorat si ca tuplu)
    return ls

def selectie_activitati(ls):
    ls.sort(key= lambda x : x[1][1])
    rez=[ls[0]]
    t_ultima_selectata=ls[0][1][1]
    for i in range(1,len(ls)):
        act_curenta=ls[i]
        if act_curenta[1][0]>t_ultima_selectata:
            t_ultima_selectata=act_curenta[1][1]
            rez.append(act_curenta)
    return rez

ls=citire_intervale("intervale.in")
rez=selectie_activitati(ls)
print(rez)

#%%
#Determinarea numărului minim de resurse necesare pentru a putea desfășura toate activitățile
f=open("intervale1.in")

ls_intervale=[]
for linie in f:
    interv=[int(x) for x in linie.split()]
    ls_intervale.append(interv)
ls_intervale.sort()
h=[]
sali=[]
import heapq
for interval in ls_intervale:
    if len(h)==0: #primul interval
        sala_noua=[interval]
        sali.append(sala_noua)
        heapq.heappush(h,(interval[1],0))
    else:
        t_terminare,indice_sala=heapq.heappop(h) #sala cu timpul de terminare cel mai mic
        if t_terminare<interval[0]: #se poate adauga intervalul curent la ea
            sali[indice_sala].append(interval)
            heapq.heappush(h,(interval[1], indice_sala)) #inseram in heap sala cu noul timp de terminare
        else:
            sala_noua = [interval]
            sali.append(sala_noua)
            heapq.heappush(h,(interval[1], len(sali)-1) ) #indice sala= ultima sala
            heapq.heappush(h,(t_terminare,indice_sala)) #inseram inapoi sala pe care am extras-o asa cum era pt ca nu am adaugat la ea

i=1
for sala in sali:
   print(f"sala {i} :")
   print(*sala)
   i+=1
print(f"Numarul minim de sali este {len(sali)}")

#%%
    

