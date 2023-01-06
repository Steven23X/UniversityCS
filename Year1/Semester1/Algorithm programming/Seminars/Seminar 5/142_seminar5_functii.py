"""
Să de ordoneze elementele din vector crescător după suma cifrelor,
iar în caz de egalitate, descrescător după valorile lor
"""
v=[int(x) for x in input().split()]
#sorted(secventa, key=cheie de comparare (o functie- numele ei), reverse =Treu/False- descrescator sau nu) => returneaza o lista (nu modifica secventa)
#lista.sort(key,reverse) - modifica lista
def cheie(x): #cheia unei element
    #return (criteriul 1, criteriul 2,...)
    s=0
    aux=x
    while x>0:
        s+=x%10
        x=x//10
    return (s,-aux)
v.sort(key=cheie) #implicit: if v[i]>v[j] v[i]<-> v[j], daca definim key: if key(v[i])>key(v[j])
print(v)
