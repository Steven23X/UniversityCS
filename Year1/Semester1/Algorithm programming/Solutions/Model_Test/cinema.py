
def sterge_ore(d,cinema,film,ora):
    rez=[]
    ls=d[cinema][film]
    for o in ora:
        if o in ls:
            ls.remove(o)
    for filme in d[cinema]:
        if d[cinema][filme]:
            rez.append(filme)

    if d[cinema][film]==[]:
        d[cinema].pop(film)
    return rez



citire=open("cinema.in","r")
d={}
for linie in citire:
    l=linie.split(" % ")
    cinema=l[0]
    film=l[1]
    ore =l[2].split()
    if cinema in d:
        d[cinema][film]= ore
    else:
        d[cinema]={film:ore}
citire.close()
print(d)
'''
f=input("film=")
c=input("cinema=")
o=input("ora=")
print(sterge_ore(d,c,f,{o}))
print(d)
'''

def cinema_film(d,*arg,ora_min,ora_max):
    ls_finala=[]
    for cinema in arg:
        for filme in d[cinema]:
            ls_ore=[]
            for o in d[cinema][filme]:
                if o>=ora_min and o<=ora_max:
                    ls_ore.append(o)
            if ls_ore:
                ls_finala.append((filme,cinema,ls_ore))

    ls_finala=sorted(ls_finala,key= lambda x : (x[0],-len(x[2])))
    return ls_finala








ora_minima=input("ora minima=")
ora_maxima=input("ora maxima=")
sir_cinema1=input("cinema1=")
sir_cinema2=input("cinema2=")

print(cinema_film(d,sir_cinema1,sir_cinema2,ora_min=ora_minima,ora_max=ora_maxima))
