def cautare(x, L, cmpValori): #=>ultima aparitie sau None, cmpValori(x,y) =True <=> x==y dupa criteriul nostru
    for i in range(len(L)-1,-1,-1):
        if cmpValori(x,L[i]):#if x==L[i]:
            return i
    return None
ls=[(2,1),(6,5),(3,4), (5,6), (2,7), (9,10)]
#caut perechea  {1,2} - nu conteaza ordinea elementelor, adica (1,2)=(2,1)
# tb sa cautam in ls daca apare (1,2) sau (2,1)
def comp_tuplu(t1,t2):
    if (t1==t2) or (t1==t2[::-1]):
        return True
    return False
    #return (t1==t2) or (t1==t2[::-1])
print(cautare((6,5),ls,comp_tuplu))