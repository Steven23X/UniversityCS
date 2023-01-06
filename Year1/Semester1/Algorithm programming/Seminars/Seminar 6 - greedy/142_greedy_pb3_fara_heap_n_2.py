#solutia de n2
f=open("intervale.in")

ls_intervale=[]
for linie in f:
    interv=[int(x) for x in linie.split()]
    ls_intervale.append(interv)
f.close()
ls_intervale.sort()
sali=[]
print("Solutie:")
for interv in ls_intervale:
    for s in sali:
        if s[-1][1]<interv[0]:
            s.append(interv)
            break
    else:
        sali.append([interv]) #sala noua
print(*sali, sep="\n")