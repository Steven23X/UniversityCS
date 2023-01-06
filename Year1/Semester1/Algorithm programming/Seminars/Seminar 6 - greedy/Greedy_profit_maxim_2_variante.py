#varianta 1 O(n^2)
#consideram activitatile descrescator dupa profit
#programam activitatea curenta cat mai aproape de deadline, daca exista slot liber
ls_act = []
with open("profit_maxim.in") as f:
    i = 0
    n = int(f.readline())
    for linie in f:
        i = i + 1
        p, t = [int(x) for x in linie.split()]
        ls_act.append((p, t, i))  # (profit, deadline, indice)
ls_act.sort(reverse=True)

planificare = [None] * n
for p,t,i in ls_act:
    t-=1
    while t>=0 and planificare[t] is not None: #caut slot liber la stanga lui t
        t-=1
    if t>=0:
        planificare[t]=i
print(planificare)

#varianta 2 - cu heap, O(n log n)
import heapq

ls_act = []
with open("profit_maxim.in") as f:
    i = 0
    n = int(f.readline())
    for linie in f:
        i = i + 1
        p, t = [int(x) for x in linie.split()]
        ls_act.append((t, p, i))  # (deadline, profit, indice)
print(ls_act)
ls_act.sort(reverse=True)  # sortat dupa deadline t descrescator
print(ls_act)
h = []
j = 0
planificare = [None] * n  # n spatii pe axa timpului
# idee:
# la momentul t=n-1 alegem activitatea cu profit maxim dintre cele cu deadline n-1
# la momentul t=n-1 alegem activitatea cu profit maxim dintre cele cu deadline n-1 sau n-2 (nealeasa anterior) etc
# pentru aceasta - un max-heap dupa profit in care la momentul t introducem si activitatile cu deadline t
# in max-heap introducem pereche (-profit,indice activitate)
for t in range(n, 0, -1):  # completam de la final la momentul 0 axa timpului; primul interval completat va fi [n-1,n)
    # adaugam in heap activitatile cu deadline = t (profitul se introduce cu minus, pentru a extrage maximul)
    while j < len(ls_act) and ls_act[j][0] == t:
        heapq.heappush(h, (-ls_act[j][1], ls_act[j][2]))  # profit, indice activitate
        j += 1
    if len(h) > 0:
        (profit, indice) = heapq.heappop(h)
        planificare[t - 1] = indice

print(planificare)
