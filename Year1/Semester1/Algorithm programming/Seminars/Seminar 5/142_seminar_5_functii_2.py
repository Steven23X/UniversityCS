def pozitiv(x):
    return x>0
def filtreaza(*numere,functie=None): #parametri de dupa param varibil *numere se apeleaza obligatoriu cu nume
    print(numere, type(numere)) #tuplu
    if functie == None:
        return list(numere)
    return [x for x in numere if functie(x)==True]


a = filtreaza(3,-1,6,8,-3,functie=pozitiv)
print(a)
a = filtreaza(3,-1,6,8,-3)
print(a)
a = filtreaza("ana","are","10","mere",functie=str.isalpha)
print(a)