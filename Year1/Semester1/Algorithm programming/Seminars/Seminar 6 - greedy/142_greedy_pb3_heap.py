f=open("intervale.in")

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
print(sali)

