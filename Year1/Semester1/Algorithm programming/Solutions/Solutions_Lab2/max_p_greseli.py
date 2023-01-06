prop="Problemele cu șiruri de caracteger nu sunt ggerle daca gerpeti gergulat!"
s="re"
t="ger"
p=8
if prop.count(t)>p:
    print(f"prea multe greseli, doar {p} au fost corectate")

prop=prop.replace(t,s,p) #inlocuieste doar primele p aparitii

print(prop)