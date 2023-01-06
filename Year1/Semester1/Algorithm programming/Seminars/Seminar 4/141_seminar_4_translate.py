""" Se citește un text conținând separatorii uzuali( ,.;:) Sa se înlocuiască toți separatorii cu spațiu.
"""
separatori=",.;:!"
prop="un cuvant, doua... trei,patru!!"
for c in separatori:
    prop=prop.replace(c," ")
print(prop)

#inlocuiri de caractere simultan - dictionar de "traducere" cheia- ordinul caracterulu iinlocuit, valoarea -cu ce inlocuiesc
prop="un cuvant, doua... trei,patru!!"
#tabelul de traducere- se poate crea cu maketrans- care se poate apela cu str.maktrans (numeclasa.metoda) sau sir.maketrans
#maketrans(x,y,[z]) x=sirul caracterelor pe care le inlocuim, y=sirul corespunzator caracterelor cu care inlocuim
#x[i] se inlocuieste cu y[i], x si y trebuie sa aiba aceeasi lungime
#z-un sir de caractere pe care vrem sa le stergem
tabel=str.maketrans(separatori," "*len(separatori))
print(tabel) #{ord(x[i]:ord(y[i])}
prop=prop.translate(tabel)
print(prop)
#stergerea vocalelor din propozitie
prop="un cuvant, doua... trei,patru!!"
tabel=str.maketrans("","","aeiou") #stergem vocalale
print(tabel) #{ord(x[i]:ord(y[i])}
prop=prop.translate(tabel)
print(prop)

prop="1 2 3 in cuvinte"
#cream dictionar = tabelul de traducere ! cheia trebuie sa fie un caracter caracter:cu ce il inlocuiesc
d={"1":"unu", "2":"doi", "3":"trei"}
tabel=str.maketrans(d)
print(tabel)
prop=prop.translate(tabel)
print(prop)

#pasareasca
prop="un cuvant doua"
vocale="aeiou"
d={x:x+"p"+x for x in vocale}
print(d)
tabel=str.maketrans(d)
print(tabel)
prop=prop.translate(tabel)
print(prop)
