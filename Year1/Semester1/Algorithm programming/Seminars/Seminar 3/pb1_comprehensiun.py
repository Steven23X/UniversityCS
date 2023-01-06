"""
1. Se citește o propoziție cu cuvintele separate prin spatii (unul sau mai multe).
Să se creeze o listă cu cuvintele care încep cu o vocală (folosind și comprehensiune)
"""

"""Varianta 1- fara comprehension
#prop="In aceasta sala este foarte cald"
prop=input()
l_cuvinte=prop.split()
l_rez=[]
for cuv in l_cuvinte:
    if cuv[0].lower() in "aeiou": #cuv.startswith(tuple("aeiou"))
        l_rez.append(cuv)
print(l_rez)
"""

#Varianta 2- cu comprehension
l_rez=[cuv for cuv in input().split() if cuv[0].lower() in "aeiou"]
print(l_rez)



